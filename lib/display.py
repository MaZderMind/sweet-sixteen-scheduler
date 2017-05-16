from lib.driver.driver import Driver


class Display(object):
    def __init__(self, board_count=1):
        self.frames_per_second = 2
        self.board_count = board_count
        self.drivers = []

    def add_driver(self, driver: Driver) -> 'Display':
        self.drivers.append(driver)
        driver.set_display(self)
        return self

    def set_frame_rate(self, frames_per_second: int) -> 'Display':
        self.frames_per_second = frames_per_second
        return self

    def setup(self) -> 'Display':
        for driver in self.drivers:
            driver.setup()

        return self

    def output(self, frame: 'Frame') -> 'Display':
        for driver in self.drivers:
            driver.output(frame)

        return self
