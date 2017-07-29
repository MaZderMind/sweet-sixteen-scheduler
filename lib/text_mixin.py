import codecs
import logging

# noinspection PyUnresolvedReferences
import translitcodec

from lib.constants import *
from lib.direction import Direction
from lib.system.config import Config
from lib.text import patterns

log = logging.getLogger("TextMixin")


def clean(text):
    cleaned = codecs.encode(text, 'translit/long').encode('ascii', 'ignore')
    log.debug("cleaned {} to {}".format(text, cleaned))
    return cleaned


class TextMixin(object):
    """
    Mixin included by lib.frame.Frame, providing Logic for Text-Output and
    -Animation.
    """

    def __init__(self):
        """
        Initialize internal Data-Structures of the TextMixin.

        :type self: lib.frame.Frame
        """
        self._row = 0
        self._col = 0
        self._wrap = True

    def set_wrap(self, value):
        """
        Set if text that overflows the first row should wrap into the second and vice/versa

        :type self: lib.frame.Frame
        :param value: Should text wrap
        :type value: bool
        :return: lib.frame.Frame
        """
        self._wrap = value
        return self

    def text(self, text):
        """
        Render Text into the Frame on the Coordinates configured before.

        :type self: lib.frame.Frame
        :param text: Text to render
        :type text: str
        :return: lib.frame.Frame
        """
        log.debug("text={} @ {}/{}".format(text, self._row, self._col))
        clean_text_bytes = clean(text)

        for byte in clean_text_bytes:
            pattern = patterns.get(byte)
            self.set_digit(self._row, self._col, pattern)
            self._increment_col_with_wrap()

        return self

    def _increment_col_with_wrap(self):
        self._col += 1

        if not self._wrap:
            return

        if self._col >= digits_per_row():
            self._col = 0
            self._row += 1

        if self._row >= ROWS_PER_BOARD:
            self._row = 0

    def row(self, row):
        """
        Selects the row to place following text on.

        :type self: lib.frame.Frame
        :param row: Row to select
        :type row: int
        :return: lib.frame.Frame
        """
        self._row = row
        return self

    def col(self, col: int):
        """
        Selects the column to place following text on.

        :type self: lib.frame.Frame
        :param col: Column to select
        :type col: int
        :return: lib.frame.Frame
        """
        self._col = col
        return self

    def scroll_out(self, direction):
        """
        Create a scrolling-animation

        :param direction: Direction in which to scroll.
        :type direction: Direction
        :return: lib.frame.Frame
        """
        return None
