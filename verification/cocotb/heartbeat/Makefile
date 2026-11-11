TOPLEVEL_LANG := vhdl
SIM ?= ghdl
TOPLEVEL := heartbeat
COCOTB_TEST_MODULES := test_heartbeat
VHDL_SOURCES := $(abspath ../../../rtl/common/heartbeat.vhd)
include $(shell cocotb-config --makefiles)/Makefile.sim
