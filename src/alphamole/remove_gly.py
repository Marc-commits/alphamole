#! python3
"""Removes gly-linker from pdb-files."""

from constants import _TRIM_NAMES
from pymol import cmd


@cmd.extend
def _remove_gly_linker(length: int = 20, trim_names: int = _TRIM_NAMES) -> None:
    """Renames and removes gly linker."""
    for obj in cmd.get_object_list():
        cmd.set_name(obj, obj[:trim_names])
    cmd.remove(f"""pepseq {"G" * length}""")


@cmd.extend
def remove_gly_linker(
    selection: str = "ranked_*_gly.pdb",
    save: bool = True,
    output: str = "{name}_-gly.pdb",
    **kwargs,
) -> None:
    """Loads selection, calls _remove_gly_linker and saves pdbs."""
    cmd.loadall(selection)
    _remove_gly_linker(**kwargs)
    if save:
        cmd.multifilesave(output)


if __name__ == "__main__":
    remove_gly_linker()
