#! python3
"""Supers pdb-files."""

from pymol import cmd


@cmd.extend
def super_pdbs(
    selection: str = "ranked_*.pdb",
    reference_model: str = "ranked_0",
    save: bool = True,
    output: str = "{name}_gly.pdb",
    trim_names: int = 8,
) -> None:
    """Loads all pdbs, renames, calls super and saves."""
    cmd.loadall(selection)
    for obj in cmd.get_object_list():
        cmd.set_name(obj, obj[:trim_names])
    cmd.extra_fit(reference=reference_model, method="super")
    if save:
        cmd.multifilesave(output)


if __name__ == "__main__":
    super_pdbs()
