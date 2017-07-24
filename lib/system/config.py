import os.path
import logging
from lib.system.args import Args
from configparser import ConfigParser

__all__ = ['Config']
Config = ConfigParser()


def load():
    dirname = os.path.dirname(os.path.realpath(__file__))
    files = [
        os.path.join(dirname, '../../default-config.ini'),
        os.path.join(dirname, '../../config.ini'),
        '/etc/sweet-sixteen.ini',
        os.path.expanduser('~/.config/sweet-sixteen.ini'),
    ]

    if Args.ini_file is not None:
        files.append(Args.ini_file)

    global Config
    read_files = Config.read(files)

    log = logging.getLogger('ConfigParser')
    log.debug('considered config-files: \n%s',
              "\n".join(["\t\t" + os.path.normpath(file)
                         for file in files]))

    log.debug('successfully parsed config-files: \n%s',
              "\n".join(["\t\t" + os.path.normpath(file)
                         for file in read_files]))
