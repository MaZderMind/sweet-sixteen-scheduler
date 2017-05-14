from lib.display import Display
from lib.driver.rpi_driver import RPiDriver
from lib.driver.webdriver import WebDriver
from lib.frame import Frame
from lib.sequence import Sequence

display = Display()
Sequence.set_default_display(display)

display.add_driver(WebDriver())
if RPiDriver.can_run():
    display.add_driver(RPiDriver())

display.setup()

Frame() \
    .row(0).col(2) \
    .text("foo") \
    .set_segment(0, True) \
    .repeat(seconds=5) \
    .display()

# keeps Websocket-Server running until killed with Ctrl-C
