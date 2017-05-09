from lib.sequence import Sequence


class TextMixin(object):
    def __init__(self):
        print("text init")
        self._row = 0
        self._col = 0

    def text(self, text):
        """
        @type self: Frame
        """
        print("text @", self._row, self._col, text)
        self.set_register(1, 0xFF00).set_register(2, 0x1010)
        return self

    def row(self, row):
        self._row = row
        return self

    def col(self, col):
        self._col = col
        return self

    def scroll_out(self, direction):
        pass

