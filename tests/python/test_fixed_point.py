from fpga_embedded.fixed_point import signed_wrap


def test_signed_wrap():
    assert signed_wrap(7, 4) == 7
    assert signed_wrap(8, 4) == -8
    assert signed_wrap(17, 4) == 1
