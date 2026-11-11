# Register map

The canonical definition is `registers/control_block.toml`, using the native
`hdl-registers` TOML format.

Generate the project artefacts with:

```bash
uv run python scripts/generate_registers.py
```

Outputs are written to `build/generated/control_block/`:

- `c/`: C register header for embedded software.
- `html/`: register and field reference documentation.
- `python/`: Python accessor class (you provide the transport implementation).
- `vhdl/`: VHDL register package.

The generated VHDL package provides register definitions/types; it is not, by
itself, a complete AXI-Lite peripheral. `hdl-registers` also provides an
AXI-Lite wrapper generator and simulation support generators; add those when
you settle the bus and testbench integration for each IP.

Do not edit generated files. Edit the TOML source and regenerate.
