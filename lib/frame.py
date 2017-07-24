from datetime import datetime, timedelta

from lib.sequence import Sequence
from lib.text_mixin import TextMixin


class Frame(TextMixin):
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
        self.segments = [None] * 9 * 16 * 4  # FIXME access number of Boards

    def set_segment(self, segment, value):
        """
        Set a Segment to a given Value

        :param segment: Index of the Segment to set
        :type segment: int
        :param value: Value to set the Segment to.
            True = LED is on,
            False = LED is off
        :type value: bool
        :return: lib.frame.Frame
        """
        self.segments[segment] = value
        return self

    def clear_segment(self, segment):
        """
        Clear a Segment by setting it transparent.

        :param segment: Index of the Segment to clear
        :type segment: int
        :return: lib.frame.Frame
        """
        self.segments[segment] = None
        return self

    def fill_transparent(self):
        """
        Set all transparent Segments to off, removing any remaining
        transparency.

        :return: lib.frame.Frame
        """
        self.segments = [False if segment is None else segment
                         for segment in self.segments]
        return self

    def repeat(self, seconds=0, minutes=0):
        """
        Create a Sequence from this Frame, which repeats the current Frame for
        the given amount of Time.

        :param seconds: Seconds-Part of the Duration
        :type seconds: int
        :param minutes: Seconds-Part of the Duration
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
                yield Frame.from_segments(self.segments)

        return Sequence(generator)

    @classmethod
    def from_segments(cls, segments):
        """
        Create a new Frame initialized with the specified Segment
        configuration.

        :param segments: List of Segments
        :type segments: iterable[bool|None]
        :return: lib.frame.Frame
        """
        frame = Frame()
        frame.segments = segments  # FIXME ensure list layout and types
        return frame
