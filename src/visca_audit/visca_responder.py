# Mark A. Ziesemer, www.ziesemer.com - 2026-07-29, 2026-08-01

import asyncio

import machine

class ViscaResponder():

	def __init__(self, *args, **kwargs):
		self._uart_sr: asyncio.StreamReader
		self._uart_sw: asyncio.StreamWriter

	async def run(self, uart_id: machine.ID_T = 0, baud: int = 9600):
		print("Starting...")

		self._uart_sr = asyncio.StreamReader(
			machine.UART(uart_id, baudrate=baud, timeout=0))
			# As documented at https://docs.micropython.org/en/latest/library/asyncio.html#asyncio.Stream :
			#  - asyncio.Stream : To minimize code this class implements both a reader and a writer,
			# 		and both StreamReader and StreamWriter alias to this class.
			# Benefit from this to avoid otherwise needing double instantiations,
			# 	while maintaining typing benefits:
		self._uart_sw = self._uart_sr # type: ignore

		loop = asyncio.get_event_loop()
		t = loop.create_task(self._read_loop())
		loop.run_until_complete(t)
		print("done")

	def write(self, b: bytes):
		self._uart_sw.write(b)
		print("  > " + b.hex(" "))

	async def handle(self, b: bytearray, c: int):
		print("<   " + b[:c].hex(" "))

		sw = self._uart_sw

		if c >= 4:
			if (b[0] & 0xF0 == 0x80):
				# Response Address
				ra = bytes([((b[0] & 0x0F) + 8) << 4])

				if (b[1] == 0x01):
					if (b[2] == 0x04):
						if c == 6:
							if (b[3] == 0x07 or b[3] == 0x08) and (b[4] == 0x00):
								# Stop any in-flight focus or zoom.
								self.write(ra + b"\x41\xff")
								self.write(ra + b"\x51\xff")
								await sw.drain()
					elif (b[2] == 0x06):
						if c == 9:
							if (b[3] == 0x01) and (b[4] == 0x01) and (b[5] == 0x01) and (b[6] == 0x03) and (b[7] == 0x03):
								# Stop any in-flight P/T.
								self.write(ra + b"\x41\xff")
								self.write(ra + b"\x51\xff")
								await sw.drain()
				elif (b[1] == 0x09):
					# Inquiries
					if c == 5:
						if (b[2] == 0x04):
							if (b[3] == 0x38):
								self.write(ra + b"\x50\x02\xff")
								await sw.drain()
							elif (b[3] == 0x39):
								self.write(ra + b"\x50\x00\xff")
								await sw.drain()

	async def _read_loop(self):
		sr = self._uart_sr

		max_len = 16
		buffer = bytearray(max_len)
		buf_1 = bytearray(1)
		pos = 0

		while True:
			read = await sr.readinto(buf_1)
			if read:
				b = buf_1[0]
				buffer[pos] = b
				pos = pos + 1
				if (b == 0xFF) or (pos == max_len):
					await self.handle(buffer, pos)
					pos = 0
			else:
				raise AssertionError("readinto(), but no bytes read.")

def main(uart_id: machine.ID_T = 0, baud: int = 9600):
	try:
		asyncio.run(ViscaResponder().run(baud=baud))
	except KeyboardInterrupt:
		print("KeyboardInterrupt.")
	finally:
		asyncio.new_event_loop()

if __name__ == "__main__":
	main()
