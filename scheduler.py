#!/usr/bin/env python
from lib.frame import Frame
from lib.system import application

application.init()

l = 5
i = c = -l
m = 16
while True:
    Frame() \
        .set_wrap(False) \
        .row(0).col(c) \
        .text('HALLO') \
        .row(1).col(m - c - l) \
        .text('WELT!') \
        .set_led(c + l, True) \
        .repeat(seconds=1) \
        .display()

    c = c + 1
    if c > m:
        c = i
