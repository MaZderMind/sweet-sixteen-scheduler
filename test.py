from lib.frame import Frame

Frame() \
    .row(0).col(2) \
    .text("foo") \
    .set_segment(0, True) \
    .repeat(seconds=5) \
    .display()
