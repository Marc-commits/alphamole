"""Command-line interface."""
import click
from pymol import cmd

from . import alter_chains
from . import chainbows_and_bfactors
from . import color_prots
from . import remove_gly_linker
from . import super_pdbs


@click.command()
@click.version_option()
def main() -> None:
    """Alphamole."""
    super_pdbs.super_pdbs("ranked_*.pdb", output="{name}_gly.pdb")
    remove_gly_linker.remove_gly_linker("ranked_*_gly.pdb", output="{name}_-gly.pdb")
    alter_chains.alter_chains("ranked_*_-gly.pdb", output="{name}_-gly.pdb")
    super_pdbs.super_pdbs("ranked_*_-gly.pdb", output="{name}_-gly.pdb")
    cmd.delete("*")
    chainbows_and_bfactors.chainbows_and_bfactors("ranked_*_-gly.pdb")
    cmd.delete("*")
    color_prots.color_prots("ranked_*_-gly.pdb")


if __name__ == "__main__":
    main(prog_name="alphamole")  # pragma: no cover
