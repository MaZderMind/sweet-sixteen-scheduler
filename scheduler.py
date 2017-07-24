#!/usr/bin/env python
from lib.frame import Frame
from lib.system import application

application.init()

top = "ABC"
bottom = "             CBA"
while True:
    top = " " + top
    bottom = bottom[1:]
    if len(bottom) == 0:
        top = "ABC"
        bottom = "             CBA"

    print(top)
    print(bottom)
    Frame() \
        .row(0).col(0) \
        .text(top) \
        .row(1).col(0) \
        .text(bottom) \
        .repeat(seconds=1 / 10) \
        .display()
