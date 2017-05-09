from datetime import timedelta
from enum import Enum


class TimeUnit(Enum):
    SECOND = 's'
    SECONDS = 's'
    MINUTE = 'm'
    MINUTES = 'm'

    def to_timedelta(self, amount):
        if self == TimeUnit.SECOND or self == TimeUnit.SECONDS:
            return timedelta(0, amount)
        elif self == TimeUnit.MINUTE or self == TimeUnit.MINUTES:
            return timedelta(0, 0, 0, 0, amount)
        else:
            raise TypeError("Unexpected Value for time_unit:" + self)
