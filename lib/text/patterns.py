def generate_pattern(enabled_segments=""):
    segment_list = []
    for segment in "gtsuhkmabncprdfe.":
        segment_list.append(segment in enabled_segments)

    return segment_list


patterns = {
    # " "
    0x20: generate_pattern(),

    # !
    0x21: generate_pattern("cd."),

    # "
    0x22: generate_pattern("mc"),

    # #
    0x23: generate_pattern("hgumsp"),

    # $
    0x24: generate_pattern("abhupdfems"),

    # %
    0x25: generate_pattern("ahupdemsnt"),

    # &
    0x26: generate_pattern("akmugfer"),

    # '
    0x27: generate_pattern("m"),

    # …

    # A
    0x41: generate_pattern("ghabcdup"),

    # B
    0x42: generate_pattern("abcdefmsp"),

    # C
    0x43: generate_pattern("abhgfe"),
}


def get(byte):
    if byte in patterns:
        return patterns[byte]

    return patterns[0x21]  # !
