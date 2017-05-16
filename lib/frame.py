from datetime import datetime, timedelta

from lib.sequence import Sequence
from lib.text_mixin import TextMixin


class Frame(TextMixin):
    def __init__(self: 'Frame'):
        TextMixin.__init__(self)
        self.segments = [None] * 9 * 16 * 4

    def set_segment(self: 'Frame', segment: int, value: bool) -> 'Frame':
        self.segments[segment] = value
        return self

    def clear_segment(self: 'Frame', segment: int) -> 'Frame':
        self.segments[segment] = None
        return self

    def fill_transparent(self: 'Frame') -> 'Frame':
        self.segments = [False if segment is None else segment for segment in self.segments];
        return self

    def repeat(self: 'Frame', seconds: int = 0, minutes: int = 0) -> Sequence:
        time_delta = timedelta(seconds=seconds, minutes=minutes)
        end_time = datetime.now() + time_delta

        def generator():
            while datetime.now() < end_time:
                yield Frame.from_segments(self.segments)

        return Sequence(generator)

    @classmethod
    def from_segments(cls, segments) -> 'Frame':
        frame = Frame()
        frame.segments = segments
        return frame
