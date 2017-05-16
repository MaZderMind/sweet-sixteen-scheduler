import time

from lib.display import Display


class Sequence(object):
    default_display = None

    def __init__(self, generator):
        self.generator = generator
        print("sequence init")

    def __iter__(self):
        return self.generator()

    def display(self, display: Display = None) -> 'Sequence':
        if not display:
            display = Sequence.default_display

        if not display:
            raise RuntimeError("display() called but no Display configured or passed")

        for frame in self.generator():
            frame.fill_transparent()
            display.output(frame)
            time.sleep(1 / display.frames_per_second)

        return self

    def next_frame(self) -> 'Frame':
        pass

    @classmethod
    # FIXME use global config, rename lib -> display or sth.
    def set_default_display(cls, display: Display):
        cls.default_display = display
        pass
