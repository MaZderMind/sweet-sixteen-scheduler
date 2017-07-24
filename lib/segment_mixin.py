import logging

from lib.constants import *

log = logging.getLogger("SegmentMixin")


def _offset(row, col):
    board = int(col / DIGITS_PER_ROW)
    board_col = col % DIGITS_PER_ROW

    if row == 1:
        board_col = 3 - board_col

    segment = (DRIVERS_PER_BOARD * board) + (row * DIGITS_PER_ROW)
    return (board_col + segment) * SEGMENTS_PER_DIGIT


def _dp_offset(row, col):
    board = int(col / DIGITS_PER_ROW)
    board_col = col % DIGITS_PER_ROW

    if row == 1:
        board_col = 3 - board_col

    return 0


class SegmentMixin(object):
    """
    Mixin included by lib.frame.Frame, providing Logic for Per-Digit-Output.
    """

    def set_digit(self, row, col, digit):
        """
        Set all Segments associated with a Digit to the specified Values.
        The order of the Segments as required by the board layout (
        "gtsuhkmabncprdfe") followed by the DP.

        :type self: lib.frame.Frame
        :param row: 0 for top-row, 1 for bottom row
        :param col: Column fo Digit to set, startign with 0 up to 4 * the
            number of configured boards
        :param digit: 17-Tuple of True/False/None values. True/False set the
            associated Segment to the respective Value while None keeps it at
            the existing Value
        :return: lib.sequence.Frame
        """
        if len(digit) != 17:
            raise RuntimeError("set_digit called with a digint of len != 17: "
                               "{}".format(digit))

        offset = _offset(row, col)
        dp_offset = _dp_offset(row, col)

        log.debug("row/col {}/{} = offset {}, dp_offset = {}"
                  .format(row, col, offset, dp_offset))

        for idx in range(0, 16):
            if digit[idx] is not None:
                self.set_segment(offset + idx, digit[idx])

                self.set_segment(dp_offset, digit[16])
