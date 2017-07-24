from lib.display import Display
from lib.driver.rpi_driver import RPiDriver
from lib.driver.webdriver import WebDriver
from lib.frame import Frame
from lib.sequence import Sequence
from lib.system import application

application.init()

display = Display(board_count=4)
Sequence.set_default_display(display)

web_driver = WebDriver()
display.add_driver(web_driver)
if RPiDriver.can_run():
    display.add_driver(RPiDriver())

display.setup()

while True:
    Frame() \
        .row(0).col(2) \
        .text("foo") \
        .set_segment(0, True) \
        .repeat(seconds=5) \
        .display()
