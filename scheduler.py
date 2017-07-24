#!/usr/bin/env python
from lib.frame import Frame
from lib.system import application


application.init()

while True:
    Frame() \
        .row(0).col(2) \
        .text("foo") \
        .set_segment(0, True) \
        .repeat(seconds=5) \
        .display()
