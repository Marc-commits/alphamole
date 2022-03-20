#! python3
"""Assigns chainnames based on gaps."""

import itertools

from more_itertools import split_when
from pymol import cmd


_TRIM_NAMES = len("ranked_*")


@cmd.extend
def _alter_chains(
    reference_model: str = "ranked_0", chains: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
) -> None:
    """Gets residue numbers, splits where next residue isn't +1 and renames chain."""
    for obj in cmd.get_object_list():
        cmd.set_name(obj, obj[:_TRIM_NAMES])
    res_numbers = []
    cmd.iterate(
        reference_model, "res_numbers.append(resv)", space={"res_numbers": res_numbers}
    )
    split = list(split_when(list(set(res_numbers)), lambda x, y: y > x + 1))
    minima = [min(lst) for lst in split]
    for first_residue, chain_name in zip(minima, itertools.cycle(chains)):
        cmd.alter(
            f"bm. resi {first_residue}",
            f"""chain={chain_name}""",
            space={i: i for i in chains},
        )


@cmd.extend
def alter_chains(
    selection: str,
    output: str = "{name}.pdb",
    **kwargs,
) -> None:
    """Loads selection, calls _alter_chains and saves pdbs."""
    cmd.loadall(selection)
    _alter_chains(**kwargs)
    if output:
        cmd.multifilesave(output)


if __name__ == "__main__":
    alter_chains("*.pdb")
