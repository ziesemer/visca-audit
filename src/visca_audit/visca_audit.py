# Mark A. Ziesemer, www.ziesemer.com - 2026-07-29, 2026-08-01

import asyncio
import sys
import time
import typing

import machine

MsgHandler = typing.Callable[[bytearray, int], typing.Awaitable[None]]
StdInRead = typing.Callable[[], typing.Awaitable[bytearray]]

class Blank():

	@typing.override
	def __str__(self) -> str:
		return "_"

	@typing.override
	def __repr__(self) -> str:
		return "_"

class TestResult():

	def __init__(self, name: str):
		self.name = name
		self.print_summary_on_complete = True
		self.reset()

	def reset(self):
		pass

	def print_summary(self):
		print(f"{self.name}:")

class TimeResult(TestResult):

	def __init__(self, name: str):
		self.time  = float('nan')

		super().__init__(name)

	def hit(self, result_time: float):
		self.time = result_time

	@typing.override
	def print_summary(self):
		super().print_summary()
		print(f"  time: {self.time:2.2f}s")

class RangeResult(TestResult):

	def __init__(self, name: str, max_expect: int, min_expect = 0):
		self.max_expect = max_expect
		self.min_expect = min_expect
		self.range_expect = max_expect - min_expect + 1
		self.min_hit: None | int
		self.max_hit: None | int
		super().__init__(name)

	@typing.override
	def reset(self):
		self.min_hit = None
		self.max_hit = None

	def hp(self, value: int):
		self.hit(value)
		self.print(value)

	def hit(self, value: int):
		if self.min_hit is None or value < self.min_hit:
			self.min_hit = value
		if self.max_hit is None or value > self.max_hit:
			self.max_hit = value

	def print(self, value: int):
		print(f"call: {value} - {self.min_hit} / {self.max_hit}")

	@typing.override
	def print_summary(self):
		super().print_summary()
		range_hit = self.max_hit - self.min_hit + 1 \
			if self.max_hit is not None and self.min_hit is not None else 0
		if self.max_hit is not None and self.min_hit is not None:
			print(f"       Hit min-max/range: 0x{self.min_hit:02x} - 0x{self.max_hit:02x}"
				+ f" ({self.min_hit:02d}₁₀ - {self.max_hit:02d}₁₀) / {range_hit:02d}₁₀.")
		else:
			print("       Hit min-max/range: 0x   - 0x  "
				+ f" (  ₁₀ -   ₁₀) / {range_hit:02d}₁₀.")
		print(f"  Expected min-max/range: 0x{self.min_expect:02x} - 0x{self.max_expect:02x}"
			+ f" ({self.min_expect:02d}₁₀ - {self.max_expect:02d}₁₀) / {self.range_expect:02d}₁₀.")

class SpeedStatsResult(RangeResult):

	def __init__(self, name: str, max_expect: int, min_expect = 0):
		self.hits: typing.List[int | Blank]
		super().__init__(name, max_expect, min_expect)

	@typing.override
	def reset(self):
		super().reset()
		self.hits = [Blank()] * (self.max_expect + 1)

	def get_covered(self):
		return sum(1 for s in self.hits if isinstance(s, int))

	@typing.override
	def hit(self, value: int):
		super().hit(value)
		self.hits[value] = value

	@typing.override
	def print(self, value: int):
		covered = self.get_covered() / self.range_expect
		print(f"speed: {value} {self.hits} - {self.min_hit} / {self.max_hit} - {covered:.2%}")

	@typing.override
	def print_summary(self):
		super().print_summary()
		covered = self.get_covered()
		covered_pct = covered / self.range_expect
		range_hit = self.max_hit - self.min_hit + 1 \
			if self.max_hit is not None and self.min_hit is not None else 0
		print(f"  {self.hits}")
		if self.max_hit is not None and self.min_hit is not None:
			print(f"       Hit min-max/range/coverage: 0x{self.min_hit:02x} - 0x{self.max_hit:02x}"
				+ f" ({self.min_hit:02d}₁₀ - {self.max_hit:02d}₁₀) / {range_hit:02d}₁₀ / {covered:02d}₁₀.")
		else:
			print("       Hit min-max/range/coverage: 0x   - 0x  "
				+ f" (  ₁₀ -   ₁₀) / {range_hit:02d}₁₀ / {covered:02d}₁₀.")
		print(f"  Expected min-max/range/coverage: 0x{self.min_expect:02x} - 0x{self.max_expect:02x}"
			+ f" ({self.min_expect:02d}₁₀ - {self.max_expect:02d}₁₀) / {self.range_expect:02d}₁₀ / {self.range_expect:02d}₁₀.")
		print(f"                    Covered range: {covered_pct:.2%}")

class ViscaTest():
	def __init__(self, result: TestResult):
		self.result = result

	async def start(self, stdin: StdInRead):
		pass

	async def mh(self, b: bytearray, c: int):
		pass

class TestPowerOnTime(ViscaTest):
	def __init__(self):
		self.result: TimeResult
		self._time: typing.Any
		super().__init__(TimeResult("power on time"))
		self.result.print_summary_on_complete = False

	@typing.override
	async def start(self, stdin: StdInRead):
		print("Press 'c' and power on the controller at the same time, then start continuously circling the joystick.")
		await stdin()
		self._time = time.ticks_ms()

	@typing.override
	async def mh(self, b: bytearray, c: int):
		if c == 9:
			if (b[0] & 0xF0 == 0x80) and (b[1] == 0x01):
				td = time.ticks_diff(time.ticks_ms(), self._time)
				if self._time:
					self.result.hit(td / 1000)
					self.result.print_summary()
					self._time = None

class TestPan(ViscaTest):

	def __init__(self, dir_oct: int, dir_name: str):
		self.dir_oct = dir_oct
		self.result: SpeedStatsResult
		super().__init__(SpeedStatsResult(f"pan {dir_name}", 0x18, 0x1))

	@typing.override
	async def mh(self, b: bytearray, c: int):
		if c == 9:
			if (b[0] & 0xF0 == 0x80) and (b[1] == 0x01):
				# Camera Command
				if (b[2] == 6) and (b[3] == 1) and (b[6] == self.dir_oct):
					speed = b[4]
					self.result.hp(speed)

class TestTilt(ViscaTest):

	def __init__(self, dir_oct: int, dir_name: str):
		self.dir_oct = dir_oct
		self.result: SpeedStatsResult
		super().__init__(SpeedStatsResult(f"tilt {dir_name}", 0x18, 0x1))

	@typing.override
	async def mh(self, b: bytearray, c: int):
		if c == 9:
			if (b[0] & 0xF0 == 0x80) and (b[1] == 0x01):
				# Camera Command
				if (b[2] == 6) and (b[3] == 1) and (b[7] == self.dir_oct):
					speed = b[5]
					self.result.hp(speed)

class TestZoom(ViscaTest):

	def __init__(self, dir_oct: int, dir_name: str, control: str):
		self.dir_oct = dir_oct
		self.result: SpeedStatsResult
		super().__init__(SpeedStatsResult(f"zoom {dir_name} {control}", 7))

	@typing.override
	async def mh(self, b: bytearray, c: int):
		if c == 6:
			if (b[0] & 0xF0 == 0x80) and (b[1] == 0x01):
				# Camera Command
				if (b[2] == 4) and (b[3] == 7) and (b[4] & 0xF0 == self.dir_oct):
					speed = b[4] & 0x0F
					self.result.hp(speed)

class TestPresetCalls(ViscaTest):

	def __init__(self):
		self.result: RangeResult
		super().__init__(RangeResult("preset calls", 254))

	@typing.override
	async def mh(self, b: bytearray, c: int):
		if c == 7:
			if (b[0] & 0xF0 == 0x80) and (b[1] == 0x01):
				# Camera Command
				if (b[2] == 4) and (b[3] == 0x3f) and (b[4] == 2):
					preset = b[5]
					self.result.hp(preset)

class ViscaAudit():

	def __init__(self, *args, **kwargs):
		self._uart_sr: asyncio.StreamReader
		self._stdin_sr: asyncio.StreamReader
		self._msg_handler: MsgHandler = self.none

	async def none(self, b: bytearray, i: int):
		print(b[:i].hex(" "))

	async def run(self, uart_id: machine.ID_T = 0, baud: int = 9600):
		print("Starting...")

		self._uart_sr = asyncio.StreamReader(
			machine.UART(uart_id, baudrate=baud, timeout=0))

		asyncio.create_task(self._read_loop())

		tests: typing.List[ViscaTest] = [
			TestPowerOnTime(),
			TestPan(0x01, "left"),
			TestPan(0x02, "right"),
			TestTilt(0x01, "up"),
			TestTilt(0x02, "down"),
			TestZoom(0x20, "tele", "seesaw"),
			TestZoom(0x30, "wide", "seesaw"),
			TestZoom(0x20, "tele", "joystick"),
			TestZoom(0x30, "wide", "joystick"),
			TestPresetCalls()
		]

		prompt = "Press 'c' when complete to continue, 'r' to repeat, or 'q' to quit."

		test_results: typing.List[TestResult] = []
		test_quit = False
		for test in tests:
			self._msg_handler = test.mh
			result = test.result

			test_loop = True
			while test_loop:
				await test.start(self._stdin_read)
				print(f"{result.name}.  {prompt}")
				p = await self._stdin_read()
				if result.print_summary_on_complete:
					result.print_summary()

				while True:
					if p[0] == ord("c"):
						test_loop = False
						test_results.append(result)
						break
					if p[0] == ord("r"):
						result.reset()
						break
					if p[0] == ord("q"):
						test_loop = False
						test_quit = True
						break
					print(prompt)
					p = await self._stdin_read()

			if test_quit:
				break

		print()
		print("=== Final Stats ===")
		print()
		print("visca_audit.py 2026-08-01")
		print()

		covered_sum = 0
		range_expect_sum = 0
		for tr in test_results:
			tr.print_summary()
			if isinstance(tr, SpeedStatsResult):
				covered_sum += tr.get_covered()
				range_expect_sum += tr.range_expect
			print()

		if range_expect_sum:
			total_coverage = covered_sum / range_expect_sum
			print(f"Total PTZ coverage: {total_coverage:.2%}")
			print()

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
					await self._msg_handler(buffer, pos)
					pos = 0
			else:
				raise AssertionError("readinto(), but no bytes read.")

	async def _stdin_read(self):
		sr = asyncio.StreamReader(sys.stdin)

		buf_1 = bytearray(1)

		read = await sr.readinto(buf_1)
		if read:
			return buf_1
		raise AssertionError("readinto(), but no bytes read.")

def main(uart_id: machine.ID_T = 0, baud: int = 9600):
	try:
		asyncio.run(ViscaAudit().run(uart_id, baud))
	except KeyboardInterrupt:
		print("KeyboardInterrupt.")
	finally:
		asyncio.new_event_loop()

if __name__ == "__main__":
	main()
