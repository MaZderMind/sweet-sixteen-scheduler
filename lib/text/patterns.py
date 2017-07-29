patterns = {
    # " "
    0x20: "",

    # !
    0x21: "cdx",

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

    # (
    0x28: "nr",

    # )
    0x29: "kt",

    # *
    0x2A: "kmcprstu",

    # +
    0x2B: "mpsu",

    # ,
    0x2C: "t",

    # -
    0x2D: "up",

    # .
    0x2E: "x",

    # /
    0x2F: "tn",

    # 0
    0x30: "abcdefghtn",  # "abcdefgh" maybe?

    # 1
    0x31: "ncd",

    # 2
    0x32: "abcpugfe",

    # 3
    0x33: "abcdefp",

    # 4
    0x34: "hupcd",

    # 5
    0x35: "abhupdef",

    # 6
    0x36: "ahupdefg",

    # 7
    0x37: "abcd",

    # 8
    0x38: "abcdefghup",

    # 9
    0x39: "abcpuhde",

    # :
    0x3A: "ms",

    # ;
    0x3B: "mt",

    # <
    0x3C: "tf",

    # =
    0x3D: "upfe",

    # >
    0x3E: "re",

    # ?
    0x3F: "abcpsx",

    # @
    0x40: "abcpnhgfe",

    # A
    0x41: "ghabcdup",

    # B
    0x42: "abcdefmsp",

    # C
    0x43: "abhgfe",

    # D
    0x44: "abcdefms",

    # E
    0x45: "abhgfeu",

    # F
    0x46: "abhgu",

    # G
    0x47: "abhgfdp",

    # H
    0x48: "hgcdup",

    # I
    0x49: "abmsfe",

    # J
    0x4A: "cdefg",

    # K
    0x4B: "hgunr",

    # L
    0x4C: "hgfe",

    # M
    0x4D: "hgkncd",

    # N
    0x4E: "hgkrdc",

    # O
    0x4F: "abcdefgh",

    # P
    0x50: "abcpuhgfe",

    # Q
    0x51: "abcdefghr",

    # R
    0x52: "abcpuhgr",

    # S
    0x53: "abcpugfe",

    # T
    0x54: "abms",

    # U
    0x55: "hgfedc",

    # V
    0x56: "hgtn",

    # W
    0x57: "hgtrdc",

    # X
    0x58: "ktrn",

    # Y
    0x59: "huspc",

    # Z
    0x5A: "abntfe",

    # [
    0x5B: "bmse",

    # \
    0x5C: "kr",

    # ]
    0x5D: "amsf",

    # ^
    0x5E: "hk",  # "tr" maybe?

    # _
    0x5F: "fe",

    # `
    0x60: "k",

    # a
    0x61: "gusfr",  # "gusfk" maybe?

    # b
    0x62: "hgfsu",

    # c
    0x63: "ugf",

    # d
    0x64: "ugfsm",

    # e
    0x65: "ugtfe",  # "ugtf" maybe?

    # f
    0x66: "bmsup",

    # g
    0x67: "ahumsf",

    # h
    0x68: "hgus",

    # i
    0x69: "s",

    # j
    0x6A: "msfg",

    # k
    0x6B: "msnr",

    # l
    0x6C: "ms",

    # m
    0x6D: "guspd",

    # n
    0x6E: "gus",

    # o
    0x6F: "gusf",

    # p
    0x70: "hgamu",

    # q
    0x71: "hamus",

    # r
    0x72: "gu",

    # s
    0x73: "ahusf",

    # t
    0x74: "msup",

    # u
    0x75: "gfs",

    # v
    0x76: "gt",

    # w
    0x77: "gtrd",

    # x
    0x78: "ktrn",

    # y
    0x79: "ksn",

    # z
    0x7A: "utf",

    # {
    0x7B: "bmuse",

    # |
    0x7C: "ms",  # maybe "hg"

    # }
    0x7D: "ampsf",

    # ~
    0x7E: "up",
}


def get(byte):
    if byte in patterns:
        return patterns[byte]

    return patterns[0x20]
