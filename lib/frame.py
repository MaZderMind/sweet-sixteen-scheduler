from datetime import datetime, timedelta

from lib.constants import *
from lib.driver.to_bytes_mixin import ToBytesMixin
from lib.sequence import Sequence
from lib.text_mixin import TextMixin


class Frame(TextMixin, ToBytesMixin):
    """
    Represents a displayable State of the LED-Display.
    A Frame is constituted by the State of all Segments on the Display. Each
    Segment can be on, off or transparent. Transparent Segments are important
    when combining multiples Frames by applying one on top of another. When
    sent to the Display, transparent Segments are interpreted as being off.
    """

    def __init__(self):
        """
        Initialize internal Data-Structures of the Frame and its Mixins.
        Initializes all Segments to transparen
        """
        TextMixin.__init__(self)
        ToBytesMixin.__init__(self)

        self.rows = []
        for rowId in range(0, ROWS_PER_BOARD):
            self.rows.append([])
            for digitId in range(0, digits_per_row()):
                self.rows[rowId].append([])
                self.rows[rowId][digitId] = {
                    name: None
                    for name in SEGMENT_NAMES
                }

        self.leds = [None] * num_leds()

    def set_segment(self, row, col, segment, value):
        """
        Set a Segment to a given Value

        :param row: Row-Index of the Digit to change
        :type row: int

        :param col: Col-Index of the Digit to change
        :type col: int

        :param segment: Name of the Segment to set
        :type segment: str

        :param value: Value to set the Segment to.
            True = LED is on,
            False = LED is off
        :type value: bool

        :return: lib.frame.Frame
        """
        if segment in SEGMENT_NAMES and \
                    0 <= row < ROWS_PER_BOARD and \
                    0 <= col < digits_per_row():
            self.rows[row][col][segment] = value

        return self

    def clear_segment(self, row, col, segment):
        """
        Clear a Segment by setting it transparent.

        :param row: Row-Index of the Digit to change
        :type row: int

        :param col: Col-Index of the Digit to change
        :type col: int

        :param segment: Name of the Segment to set
        :type segment: str

        :return: lib.frame.Frame
        """
        return self.set_segment(row, col, segment, None)

    def set_digit(self, row, col, segments):
        """
        Set multiple Segments of a Digit to on

        :param row: Row-Index of the Digit to change
        :type row: int

        :param col: Col-Index of the Digit to change
        :type col: int

        :param segments: String containing the names of the Segments to turn on
        :type segments: str

        :return: lib.frame.Frame
        """
        for segment in segments:
            self.set_segment(row, col, segment, True)

        return self

    def set_led(self, index, value):
        """
        Set an LED to a given Value

        :param index: Index of the LED to change
        :type index: int

        :param value: Value to set the LED to.
            True = LED is on,
            False = LED is off
        :type value: bool

        :return: lib.frame.Frame

        """
        if 0 <= index < num_leds():
            self.leds[index] = value

        return self

    def clear_led(self, index):
        """
        Clear a Segment by setting it transparent.

        :param index: Index of the LED to change
        :type index: int

        :return: lib.frame.Frame

        """
        return self.set_led(index, None)

    def fill_transparent(self):
        """
        Set all transparent Segments to off, removing any remaining
        transparency.

        :return: lib.frame.Frame
        """
        for rowId in range(0, ROWS_PER_BOARD):
            for digitId in range(0, digits_per_row()):
                self.rows[rowId][digitId] = {
                    name: bool(self.rows[rowId][digitId][name])
                    for name in SEGMENT_NAMES
                }

        self.leds = [bool(value) for value in self.leds]

        return self

    def copy_non_transparent(self):
        """
        Copy the Frame and set all transparent Segments to off, removing any
        remaining transparency.

        :return: lib.frame.Frame
        """
        copy = Frame.from_frame(self)
        copy.fill_transparent()
        return copy

    def repeat(self, seconds=0, minutes=0):
        """
        Create a Sequence from this Frame, which repeats the current Frame for
        the given amount of Time.

        :param seconds: Seconds-Part of the Duration
        :type seconds: int
        :param minutes: Minutes-Part of the Duration
        :type minutes: int
        :return: lib.sequence.Sequence
        """
        time_delta = timedelta(seconds=seconds, minutes=minutes)
        end_time = datetime.now() + time_delta

        def generator():
            """
            Generator-Function, repeating the Frame for the given amount of
            time.
            """
            while datetime.now() < end_time:
                yield Frame.from_frame(self)

        return Sequence(generator)

    @classmethod
    def from_frame(cls, frame):
        """
        Create a new Frame initialized with the specified Segments of
        the specified Frame

        :param frame: Frame to copy
        :type frame: lib.frame.Frame
        :return: lib.frame.Frame
        """
        new_frame = Frame()
        new_frame.rows = []

        for rowId in range(0, ROWS_PER_BOARD):
            new_frame.rows.append([])
            for digitId in range(0, digits_per_row()):
                new_frame.rows[rowId].append([])
                new_frame.rows[rowId][digitId] = {
                    name: frame.rows[rowId][digitId][name]
                    for name in SEGMENT_NAMES
                }

        new_frame.leds = [value for value in frame.leds]

        return new_frame
