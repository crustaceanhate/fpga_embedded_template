import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def reset_and_count(dut):
    dut.clk.value = 0
    dut.rst.value = 1

    async def tick():
        dut.clk.value = 0
        await Timer(5, unit="ns")
        dut.clk.value = 1
        await Timer(1, unit="ns")

    for _ in range(2):
        await tick()

    dut.rst.value = 0

    # The default counter is 4 bits: pulse on the 16th active edge after reset.
    for _ in range(15):
        await tick()
        assert int(dut.pulse.value) == 0

    await tick()
    assert int(dut.pulse.value) == 1
