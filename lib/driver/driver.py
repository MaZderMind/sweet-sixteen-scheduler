class Driver(object):
    def output(self, frame):
        """
        Send a Frame to a Drivers' Output.

        :param frame: Frame to transmit
        :type frame: lib.frame.Frame
        :return: lib.driver.driver.Driver
        """
        raise NotImplementedError("output() needs to be implemented "
                                  "by subclass of Driver")
