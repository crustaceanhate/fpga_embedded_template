"""VUnit runner for the VHDL-native regression."""

from pathlib import Path

from vunit import VUnit

ROOT = Path(__file__).resolve().parents[2]

vu = VUnit.from_argv()
lib = vu.add_library("fpga_lib")
lib.add_source_files(str(ROOT / "rtl/common/*.vhd"))
lib.add_source_files(str(ROOT / "verification/vunit/**/*.vhd"))
vu.main()
