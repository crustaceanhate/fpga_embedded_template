# FPGA + embedded software template

A minimal mixed VHDL, Python and embedded-C project. Python dependencies are managed
from the repository root with **uv**. The example HDL is intentionally tiny; use it
as a pattern for adding independently verified IP blocks.

## Prerequisites

Install these separately (they are not Python packages and are not managed by uv):

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- [GHDL](https://ghdl.github.io/ghdl/) and [NVC](https://www.nickg.me.uk/nvc/)
- GNU Make (for the cocotb Makefile example)
- A target C/C++ toolchain when building embedded firmware

Vivado/Vitis, MATLAB/Simulink and vendor board tools are also external dependencies.

## Setup

```bash
uv sync
```

This creates `.venv/` and resolves `uv.lock`. Commit both `pyproject.toml` and
`uv.lock` to make developer and CI environments reproducible.

## Run the examples

Python unit tests:

```bash
uv run pytest
```

VUnit regression with either simulator:

```bash
uv run python verification/vunit/run.py --simulator=ghdl
uv run python verification/vunit/run.py --simulator=nvc
```

cocotb test with either simulator:

```bash
make -C verification/cocotb/heartbeat SIM=ghdl
make -C verification/cocotb/heartbeat SIM=nvc
```

Sphinx HTML documentation:

```bash
uv run sphinx-build -b html docs docs/_build/html
```

Generate register artefacts from the canonical TOML file:

```bash
uv run python scripts/generate_registers.py
```

See `docs/registers.md` for the generated outputs and integration notes.

## Layout

- `rtl/`: portable synthesizable VHDL.
- `verification/`: HDL verification, reference models and vectors.
- `tests/`: tests for ordinary Python package/application code.
- `src/`: reusable Python code.
- `software/`: embedded C/C++ source.
- `registers/`: canonical machine-readable register definitions.
- `docs/`: Sphinx documentation.
- `fpga/`: board-specific integration, constraints and build scripts.
