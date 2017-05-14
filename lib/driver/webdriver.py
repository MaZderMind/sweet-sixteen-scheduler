from lib.driver.driver import Driver


class WebDriver(Driver):
    def setup(self) -> 'Driver':
        pass

    def output(self, frame: 'Frame') -> 'Driver':
        print("webdriver output frame", frame)


