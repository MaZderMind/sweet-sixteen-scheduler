patterns = {
    # " "
    0x20: "",

    # !
    0x21: "cd.",

    # "
    0x22: "mc",

    # #
    0x23: "hgumsp",

    # $
    0x24: "abhupdfems",

    # %
    0x25: "ahupdemsnt",

    # &
    0x26: "akmugfer",

    # '
    0x27: "m",

    # …

    # A
    0x41: "ghabcdup",

    # B
    0x42: "abcdefmsp",

    # C
    0x43: "abhgfe",
}


def get(byte):
    if byte in patterns:
        return patterns[byte]

    return patterns[0x21]  # !
