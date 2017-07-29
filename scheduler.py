#!/usr/bin/env python
from lib.frame import Frame
from lib.system import application

application.init()

i = c = -3
m = 16
while True:
    Frame() \
        .set_wrap(False) \
        .row(0).col(c) \
        .text('AB!') \
        .row(1).col(m - c - 3) \
        .text('CCC') \
        .set_led(c + 3, True) \
        .repeat(seconds=1) \
        .display()

    c = c + 1
    if c > m:
        c = i
