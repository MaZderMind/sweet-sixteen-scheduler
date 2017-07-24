import sys
import signal
import logging

from lib.driver import manager
from lib.system import config
from lib.system.args import Args
from lib.system.loghandler import LogHandler

log = logging.getLogger('Application')


def init():
    log.debug('configuring Logging')

    # configure logging
    docolor = (Args.color == 'always') or (Args.color == 'auto' and
                                           sys.stderr.isatty())

    handler = LogHandler(docolor, Args.timestamp)
    logging.root.addHandler(handler)

    if Args.verbose >= 2:
        level = logging.DEBUG
    elif Args.verbose == 1:
        level = logging.INFO
    else:
        level = logging.WARNING

    logging.root.setLevel(level)

    # make killable by ctrl-c
    log.debug('setting SIGINT handler')
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    log.info('Python Version: %s', sys.version_info)

    log.debug('loading Configuration')
    config.load()

    log.debug('Initializing DriverManager')
    manager.init()
