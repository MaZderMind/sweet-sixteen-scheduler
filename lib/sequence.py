import time

from lib.display import Display


class Sequence(object):
    """
    A Sequence is a Generator that generates Frames. It can be asked for a new
    Frame as often as required by the desired Frame-Rate, as its
    Generator-Function will time itself based on Wall-Clock time, not on
    number of Calls to the Generator-Funktion.
    """
    default_display = None

    def __init__(self, generator):
        """
        Initialize internal Data-Structures of the Sequence.

        :param generator: A Generator-Function which will Yield Frame-Objects
        :type generator: Generator[lib.frame.Frame]
        """
        self.generator = generator
        print("sequence init")

    def __iter__(self):
        return self.generator()

    def display(self, display=None):
        """
        Play this Sequence now back onto the Display

        :return: lib.sequence.Sequence
        """
        if not display:
            display = Sequence.default_display

        if not display:
            raise RuntimeError("display() called but no Display configured "
                               "or passed")

        for frame in self.generator():
            frame.fill_transparent()
            display.output(frame)
            time.sleep(1 / display.frames_per_second)

        return self

    def next_frame(self):
        """
        Return a pointer to the first Frame after this Sequence as a
        starting-Point of a new animation.

        TODO: Describe when this Frame is created and what happens when it
        is not used.

        :return: lib.frame.Frame
        """
        pass

    @classmethod
    # FIXME use global config, rename lib -> display or sth.
    def set_default_display(cls, display: Display):
        cls.default_display = display
        pass
