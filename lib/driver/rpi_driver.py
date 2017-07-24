from lib.driver.driver import Driver


class RPiDriver(Driver):
    def setup(self):
        """
        Setup the RPi-Interface

        :return: lib.driver.rpi_driver.RPiDriver
        """
        pass

    def output(self, frame):
        """
        Output a Frame to the RPi-Interface

        :param frame: Frame to transmit
        :type frame: lib.frame.Frame
        :return: lib.driver.rpi_driver.RPiDriver
        """
        pass

    @classmethod
    def can_run(cls):
        """
        Examine if this process is running on an RPi with the required
        modules and configuration RPiDriver.

        :return: bool
        """
        return False
