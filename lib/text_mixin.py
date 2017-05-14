from lib.direction import Direction
from lib.sequence import Sequence


class TextMixin(object):
    def __init__(self: 'Frame'):
        print("text init")
        self._row = 0
        self._col = 0

    def text(self: 'Frame', text: str) -> 'Frame':
        print("text @", self._row, self._col, text)
        self.set_segment(42, True).set_segment(32, False)
        return self

    def row(self: 'Frame', row: int) -> 'Frame':
        self._row = row
        return self

    def col(self: 'Frame', col: int) -> 'Frame':
        self._col = col
        return self

    def scroll_out(self: 'Frame', direction: Direction) -> Sequence:
        return None
