import threading
from pathlib import Path

import flask
import logging
from flask import Flask
from flask_socketio import SocketIO
from lib.driver.driver import Driver
from lib.system.config import Config

log = logging.getLogger('WebDriver')


def static_dir() -> str:
    return str(Path(__file__).parent / 'webdriver-static')


class WebDriver(Driver):
    def __init__(self):
        super().__init__()

        self.thread = threading.Thread(target=self._run)
        self.app = app = Flask(__name__)
        self.sio = sio = SocketIO(app)

        self.port = Config.getint('driver.web', 'port')

        @sio.on('connect')
        def connect():
            sio.emit('setup', {
                'boardCount': Config.getint('display', 'boards'),
                'clientPlugins': [],
            })

        @app.route('/')
        def index():
            return flask.send_from_directory(static_dir(), 'index.html')

        @app.route('/display/<path:path>')
        def display_statics(path):
            return flask.send_from_directory(static_dir(), path)

        self.thread.start()

    def _run(self):
        self.sio.run(self.app, port=self.port)

    def output(self, frame):
        """
        Output a Frame to the Web-Interface.

        :param frame: Frame to transmit
        :type frame: lib.frame.Frame
        :return: lib.driver.webdriver.WebDriver
        """
        self.sio.emit("frame", frame.segments)
        return self

    @classmethod
    def can_run(cls):
        """
        Examine if the WebDriver is enabled in the Config.

        :return: bool
        """
        enabled = Config.getboolean("driver.web", "enabled")
        log.info("Enabled according to config? {}".format(enabled))
        return enabled
