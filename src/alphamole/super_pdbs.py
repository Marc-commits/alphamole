#! python3
"""Supers pdb-files."""

from pymol import cmd


_TRIM_NAMES = len("ranked_*")


@cmd.extend
def _super_pdbs(
    reference_model: str = "ranked_0", trim_names: int = _TRIM_NAMES, **kwargs
) -> None:
    """Renames objects and supers them."""
    for obj in cmd.get_object_list():
        cmd.set_name(obj, obj[:trim_names])
    cmd.extra_fit(reference=reference_model, method="super", **kwargs)


@cmd.extend
def super_pdbs(selection: str, output: str = "{name}.pdb", **kwargs) -> None:
    """Loads selection, calls _super_pdbs and saves."""
    cmd.loadall(selection)
    _super_pdbs(**kwargs)
    if output:
        cmd.multifilesave(output)


if __name__ == "__main__":
    super_pdbs("*.pdb")
