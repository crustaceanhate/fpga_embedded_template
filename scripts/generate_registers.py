"""Generate HDL, C, Python and HTML artefacts from the canonical TOML register map."""

from pathlib import Path

from hdl_registers.generator.c.header import CHeaderGenerator
from hdl_registers.generator.html.page import HtmlPageGenerator
from hdl_registers.generator.python.accessor import PythonAccessorGenerator
from hdl_registers.generator.vhdl.register_package import VhdlRegisterPackageGenerator
from hdl_registers.parser.toml import from_toml

ROOT = Path(__file__).resolve().parents[1]
REGISTER_NAME = "control_block"
REGISTER_FILE = ROOT / "registers" / f"{REGISTER_NAME}.toml"
OUTPUT_ROOT = ROOT / "build" / "generated" / REGISTER_NAME


def main() -> None:
    register_list = from_toml(name=REGISTER_NAME, toml_file=REGISTER_FILE)

    # Separate output folders keep generated languages/artifacts organised.
    CHeaderGenerator(
        register_list=register_list,
        output_folder=OUTPUT_ROOT / "c",
    ).create()

    HtmlPageGenerator(
        register_list=register_list,
        output_folder=OUTPUT_ROOT / "html",
    ).create()

    PythonAccessorGenerator(
        register_list=register_list,
        output_folder=OUTPUT_ROOT / "python",
    ).create()

    VhdlRegisterPackageGenerator(
        register_list=register_list,
        output_folder=OUTPUT_ROOT / "vhdl",
    ).create()


if __name__ == "__main__":
    main()
