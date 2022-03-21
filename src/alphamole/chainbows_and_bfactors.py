#! python3
"""Creates chainbows- and b-factors- .pse."""

from pymol import cmd
from pymol import util


_TRIM_NAMES = len("ranked_*")


@cmd.extend
def _chainbows_and_bfactors(trim_names: int = _TRIM_NAMES, **kwargs) -> None:
    """Renames and colors objects."""
    for obj in cmd.get_object_list():
        cmd.set_name(obj, obj[:trim_names])
    for obj in cmd.get_object_list():
        util.chainbow(obj)
        cmd.copy(obj + "_b", obj)
        cmd.spectrum("b", selection="*_b", **kwargs)


@cmd.extend
def chainbows_and_bfactors(
    selection: str, output: str = "chainbows_and_bfactors.pse", **kwargs
) -> None:
    """Loads selection, calls _chainbows_and_bfactors and saves as .pse."""
    cmd.loadall(selection)
    _chainbows_and_bfactors(**kwargs)
    if output:
        cmd.save(output)


if __name__ == "__main__":
    chainbows_and_bfactors("*.pdb")
