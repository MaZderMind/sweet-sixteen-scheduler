from datetime import datetime

from lib.sequence import Sequence
from lib.text_mixin import TextMixin


class Frame(TextMixin):
    def __init__(self):
        TextMixin.__init__(self)
        self.registers = [0] * 9

    def set_register(self, register, value):
        self.registers[register] = value;
        return self

    def repeat(self, amount, time_unit):
        """
        :type amount: int
        :type time_unit: TimeUnit
        :return: Sequence
        """
        time_delta = time_unit.to_timedelta(amount)
        end_time = datetime.now() + time_delta

        def generator():
            while datetime.now() < end_time:
                yield self.registers

        return Sequence(generator)
