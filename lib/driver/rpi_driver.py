import logging
from pathlib import Path

import pigpio

from lib.driver.driver import Driver

SPI_CHANNEL = 0
SPI_FREQ = 4000000
PIN_LE = 22

log = logging.getLogger("RPiDrive")


class RPiDriver(Driver):
    def __init__(self):
        self.pi = pigpio.pi()

        self.pi.set_mode(PIN_LE, pigpio.OUTPUT)
        self.pi.write(PIN_LE, pigpio.LOW)

        self.spi = self.pi.spi_open(SPI_CHANNEL, SPI_FREQ)

    def output(self, frame):
        """
        Output a Frame to the RPi-Interface

        :param frame: Frame to transmit
        :type frame: lib.frame.Frame
        :return: lib.driver.rpi_driver.RPiDriver
        """

        # transmit
        bytes_forward = frame.to_bytes()
        bytes_backward = bytes(reversed(bytes_forward))
        self.pi.spi_write(self.spi, bytes_backward)

        # latch
        self.pi.write(PIN_LE, pigpio.HIGH)
        self.pi.write(PIN_LE, pigpio.LOW)

    @classmethod
    def can_run(cls):
        """
        Examine if this process is running on an RPi with the required
        modules and configuration RPiDriver.

        :return: bool
        """
        return Path("/sys/firmware/devicetree/base/model").exists()
