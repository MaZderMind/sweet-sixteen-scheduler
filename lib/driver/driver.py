class Driver(object):
    def __init__(self):
        self.display = None

    def set_display(self, display: 'Display'):
        self.display = display

    def setup(self) -> 'Driver':
        raise NotImplementedError("setup() needs to be implemented by subclass of Driver")

    def output(self, frame: 'Frame') -> 'Driver':
        raise NotImplementedError("output() needs to be implemented by subclass of Driver")
