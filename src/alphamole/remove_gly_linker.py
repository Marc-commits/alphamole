#! python3
"""Removes gly-linker from pdb-files."""

from pymol import cmd


_TRIM_NAMES = len("ranked_*")


@cmd.extend
def _remove_gly_linker(length: int = 20, trim_names: int = _TRIM_NAMES) -> None:
    """Renames and removes gly linker."""
    for obj in cmd.get_object_list():
        cmd.set_name(obj, obj[:trim_names])
    cmd.remove(f"""pepseq {"G" * length}""")


@cmd.extend
def remove_gly_linker(
    selection: str,
    output: str = "{name}.pdb",
    **kwargs,
) -> None:
    """Loads selection, calls _remove_gly_linker and saves pdbs."""
    cmd.loadall(selection)
    _remove_gly_linker(**kwargs)
    if output:
        cmd.multifilesave(output)


if __name__ == "__main__":
    remove_gly_linker("*.pdb")
