#! python3
"""Creates chainbows- and b-factors- .pse."""

from pymol import cmd
from pymol import util


_TRIM_NAMES = len("ranked_*")


@cmd.extend
def _chainbows_and_bfactors(
    selection: str, trim_names: int = _TRIM_NAMES, **kwargs
) -> None:
    """Renames and colors objects."""
    for obj in cmd.get_object_list():
        cmd.set_name(obj, obj[:trim_names])
    for obj in cmd.get_object_list():
        util.chainbow(obj)
        cmd.copy(obj + "_b", obj)
        cmd.spectrum("b", selection=selection, **kwargs)


@cmd.extend
def chainbows_and_bfactors(
    selection: str = "ranked_*_gly.pdb",
    save: bool = True,
    output: str = "model_gly.pse",
    **kwargs
) -> None:
    """Loads selection, calls _chainbows_and_bfactors and saves as .pse."""
    cmd.loadall(selection)
    _chainbows_and_bfactors(selection, **kwargs)
    if save:
        cmd.save(output)


if __name__ == "__main__":
    chainbows_and_bfactors()
