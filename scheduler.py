#!/usr/bin/env python
from lib.frame import Frame
from lib.system import application

application.init()

flag = False
while True:
    flag = not flag
    print("flag", flag)
    Frame() \
        .row(0).col(0) \
        .text("!") \
        .repeat(seconds=5) \
        .display()

# .text("ABC ABC ABC" if flag else "AAABBBAAA") \
# .row(1).col(1) \
# .text("CCC!")
