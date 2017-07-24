#!/usr/bin/env python
from lib.frame import Frame
from lib.system import application

application.init()

while True:
  Frame() \
    .row(0).col(0) \
    .text("CAA") \
    .row(1).col(0) \
    .text("BBB") \
    .repeat(seconds=1 / 10) \
    .display()
