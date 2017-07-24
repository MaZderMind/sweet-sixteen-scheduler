import logging
import time

from lib.driver import manager
from lib.system.config import Config

log = logging.getLogger('Sequence')


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

    def __iter__(self):
        return self.generator()

    def display(self):
        """
        Play this Sequence now back onto the Display

        :return: lib.sequence.Sequence
        """
        for frame in self.generator():
            manager.output(frame)
            time.sleep(1 / Config.getfloat("display", "framerate"))

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
