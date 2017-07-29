from lib.system.config import Config

ROWS_PER_BOARD = 2
DIGITS_PER_ROW_PER_BOARD = 4
DIGITS_PER_BOARD = ROWS_PER_BOARD * DIGITS_PER_ROW_PER_BOARD
DRIVERS_PER_BOARD = DIGITS_PER_BOARD + 1
SEGMENTS_PER_DIGIT = 16
SEGMENT_NAMES = "gtsuhkmabncprdfex"  # x = decimal point


def num_boards():
    return Config.getint("display", "boards")


def digits_per_row():
    return num_boards() * DIGITS_PER_ROW_PER_BOARD
