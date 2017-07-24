from lib.direction import Direction


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

    def text(self, text):
        """
        Render Text into the Frame on the Coordinates configured before.

        :type self: lib.frame.Frame
        :param text: Text to render
        :type text: str
        :return: lib.frame.Frame
        """
        print("text @", self._row, self._col, text)
        self.set_segment(42, True).set_segment(32, True)
        return self

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
