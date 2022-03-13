#! python3
"""Removes gly-linker from pdb-files."""

from pymol import cmd


@cmd.extend
def remove_gly_linker(
    selection: str = "ranked_*_gly.pdb",
    length: int = 20,
    save: bool = True,
    output: str = "{name}_-gly.pdb",
    trim_names: int = 8,
) -> None:
    """Removes gly-linker from pdb-files."""
    cmd.loadall(selection)
    for obj in cmd.get_object_list():
        cmd.set_name(obj, obj[:trim_names])
    cmd.remove(f"""pepseq {"G" * length}""")
    if save:
        cmd.multifilesave(output)


if __name__ == "__main__":
    remove_gly_linker()
