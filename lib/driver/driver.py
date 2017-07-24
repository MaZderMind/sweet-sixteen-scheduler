class Driver(object):
    def __init__(self):
        self.display = None

    def set_display(self, display):
        """
        :return: lib.driver.driver.Driver
        """
        self.display = display

    def setup(self):
        """
        :return: lib.driver.driver.Driver
        """
        raise NotImplementedError("setup() needs to be implemented "
                                  "by subclass of Driver")

    def output(self, frame):
        """
        Send a Frame to a Drivers' Output.

        :param frame: Frame to transmit
        :type frame: lib.frame.Frame
        :return: lib.driver.driver.Driver
        """
        raise NotImplementedError("output() needs to be implemented "
                                  "by subclass of Driver")
