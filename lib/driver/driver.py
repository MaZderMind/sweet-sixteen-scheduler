class Driver(object):
    def __init__(self):
        pass

    def setup(self) -> 'Driver':
        raise NotImplementedError("setup() needs to be implemented by subclass of Driver")

    def output(self, frame: 'Frame') -> 'Driver':
        raise NotImplementedError("output() needs to be implemented by subclass of Driver")
