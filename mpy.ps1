Param(
	[Parameter(Mandatory=$true)]
	[string]$port
)

function mpr {
	param([Parameter(ValueFromRemainingArguments=$true)]$Args)
	& mpremote connect $port @Args
}

# - https://micropython-stubs.readthedocs.io/en/main/typing_mpy.html#install-the-typing-modules-to-your-mcu
# - https://github.com/Josverl/micropython-stubs/issues/911
mpr mip install github:josverl/micropython-stubs/mip/typing.mpy
