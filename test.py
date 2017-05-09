import time

from lib.time_unit import TimeUnit
from lib.frame import Frame

Frame() \
    .row(0).col(2) \
    .text("foo") \
    .repeat(2, TimeUnit.SECONDS) \
    .display()
