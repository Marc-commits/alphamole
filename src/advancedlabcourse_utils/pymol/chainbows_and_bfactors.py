#! python3
"""Creates chainbows- and b-factors- .pse."""

from pymol import cmd
from pymol import util


@cmd.extend
def chainbows_and_bfactors(
    selection: str = "ranked_*_gly.pdb",
    save: bool = True,
    output: str = "model_gly.pse",
    trim_names: int = 8,
) -> None:
    """Loads all ranked_*_gly.pdb, colors, and saves as .pse."""
    cmd.loadall(selection)
    for obj in cmd.get_object_list():
        cmd.set_name(obj, obj[:trim_names])
    for obj in cmd.get_object_list():
        util.chainbow(obj)
        cmd.copy(obj + "_b", obj)
        cmd.spectrum("b", selection="ranked_*_b")
    if save:
        cmd.save(output)


if __name__ == "__main__":
    chainbows_and_bfactors(trim_names=len("ranked_*"))
