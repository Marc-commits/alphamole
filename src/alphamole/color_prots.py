#! python3
"""Colors a sequence with provided color.

Idea: Florian Schneider, 16.03.2022
"""

from collections import Counter
from collections import OrderedDict

from pymol import cmd


NIFB = "".join(
    """
MELSVLGQNNGGQHSAGGCSSSSCGSTHDQLSHLPENIRAKVQNHPCYSEEAHHYFARM
HVAVAPACNIQCHYCNRKYDCANESRPGVVSEVLTPEQAVKKVKAVAAAIPQMSVLGIA
GPGDPLANPKRTLDTFRMLSEQAPDIKLCVSTNGLALPECVEELAKHNIDHVTITINCV
DPEIGAKIYPWIYWNNKRIRGVKAAKILIEQQQKGLEMLVARGILVKVNSVMIPGVNDE
HLKEVSKIVKAKGAFLHNVMPLIAEPEHGTFYGVMGQRSPEPEELQDLQDACAGDMNMM
RHCRQCRADAVGMLGEDRGDEFTLDKIESMEIDYEAAMVKRAAIHAAIKEELDEKAAKK
ERLAGLSVASVQNGTSGRYRPVLMAVATSGGGLINQHFGHATEFLVYEASPSGVRFIGH
RRVDQYCVGNDTCGEKESALAGSIRALKGCEAVLCSKIGFEPWSDLETAGIQPNGEHAM
EPIEEAVMAVYREMIESGRLENDGALLQAKA
""".split(
        "\n"
    )
)
NIFBX = "".join(
    """
MEIDYEAAMVKRAAIHAAIKEELDEKAAKKERLAGLSVASVQNGTSGRYRPVLMAVATS
GGGLINQHFGHATEFLVYEASPSGVRFIGHRRVDQYCVGNDTCGEKESALAGSIRALKG
CEAVLCSKIGFEPWSDLETAGIQPNGEHAMEPIEEAVMAVYREMIESGRLENDGAL
LQAKA
""".split(
        "\n"
    )
)
NIFBDELTABX = "".join(
    """
MELSVLGQNNGGQHSAGGCSSSSCGSTHDQLSHLPENIRAKVQNHPCYSEEAHHYFARM
HVAVAPACNIQCHYCNRKYDCANESRPGVVSEVLTPEQAVKKVKAVAAAIPQMSVLGIA
GPGDPLANPKRTLDTFRMLSEQAPDIKLCVSTNGLALPECVEELAKHNIDHVTITINCV
DPEIGAKIYPWIYWNNKRIRGVKAAKILIEQQQKGLEMLVARGILVKVNSVMIPGVNDE
HLKEVSKIVKAKGAFLHNVMPLIAEPEHGTFYGVMGQRSPEPEELQDLQDACAGDMNMM
RHCRQCRADAVGMLGEDRGDEFTLDKIES
""".split(
        "\n"
    )
)
NAFV = "".join(
    """
MALKIVESCVNCWACVDVCPSEAISLAGPHFEISASKCTECDGDYAEKQCASICPVEGA
ILLADGTPANPPGSLTGIPPERLAEAMREIQAR
""".split(
        "\n"
    )
)
NAFF = "".join(
    """
MITLTESAKSAVTRFISSTGKPIAGLRIRVEGGGCSGLKYSLKLEEAGAEDDQLVDCDG
ITLLIDSASAPLLDGVTMDFVESMEGSGFTFVNPNATNSCGCGKSFAC
""".split(
        "\n"
    )
)

SEQUENCES = OrderedDict(
    {
        "nifb": (NIFB, "bluewhite"),
        "nifbdeltabx": (NIFBDELTABX, "deepteal"),
        "nifbx": (NIFBX, "limegreen"),
        "nafv": (NAFV, "firebrick"),
        "naff": (NAFF, "deeppurple"),
    }
)


@cmd.extend
def color_seq(sequence: str, color: str, temp_name: str = "tmp_color") -> None:
    """Colors sequence with color."""
    cmd.select(temp_name, f"elem C & pepseq {sequence}")
    cmd.color(color, temp_name)


@cmd.extend
def color_prot(name: str, color: str = "") -> None:
    """Colors known protein with color."""
    name = name.lower()
    sequence = SEQUENCES[name][0]
    colour = color or SEQUENCES[name][1]
    color_seq(sequence, colour)


@cmd.extend
def color_prots(unique_sequences: bool = True, mapping: dict = SEQUENCES) -> None:
    """Colors known sequences with default colors."""
    if unique_sequences:
        for protein, (sequence, color) in mapping.items():
            sequences = [i[1][0] for i in mapping.items()]
            sequence_in_mapping = Counter([sequence in j for j in sequences])[True]
            if not sequence_in_mapping > 1:
                color_prot(protein, color)
    else:
        for protein in mapping:
            color_prot(protein)


if __name__ == "__main__":
    color_prots()
