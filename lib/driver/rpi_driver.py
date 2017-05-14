from lib.driver.driver import Driver


class RPiDriver(Driver):
    def setup(self) -> 'Driver':
        pass

    def output(self, frame: 'Frame') -> 'Driver':
        pass

    @classmethod
    def can_run(cls) -> bool:
        return False