import logging

from lib.driver.rpi_driver import RPiDriver
from lib.driver.webdriver import WebDriver

log = logging.getLogger('DriverManager')
drivers = []
__all__ = ['init', 'setup', 'output']


def init():
    for driver_cls in [WebDriver, RPiDriver]:
        driver_name = driver_cls.__name__
        log.info('testing if {} can run'.format(driver_name))

        if driver_cls.can_run():
            log.info('enabling {}'.format(driver_name))
            drivers.append(driver_cls())
        else:
            log.info('NOT enabling {} because it described itself as '
                     'not runnable'.format(driver_name))


def output(frame):
    """
    Send a Frame to a Drivers' Output.

    :param frame: Frame to transmit
    :type frame: lib.frame.Frame
    """
    for driver in drivers:
        driver.output(frame)
