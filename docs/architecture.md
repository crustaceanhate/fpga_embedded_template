# Architecture

- **RTL** is portable synthesizable VHDL.
- **Verification** contains simulator-driven tests and reference models.
- **Software** contains target-side embedded code.
- **Registers** is the intended single source of truth for the memory map.
- **FPGA** contains board-specific integration and constraints.

The same VHDL can be simulated with GHDL or NVC. VUnit provides VHDL-native
regression tests; cocotb provides Python-driven tests and access to numerical
libraries such as NumPy.
