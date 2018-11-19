import logging
from pathlib import Path

import eventlet.tpool
import eventlet.wsgi
import flask
import socketio

from lib.constants import *
from lib.driver.driver import Driver
from lib.system.config import Config

log = logging.getLogger('WebDriver')


def static_dir() -> str:
    return str(Path(__file__).parent / 'webdriver-static')


class WebDriver(Driver):
    def __init__(self):
        super().__init__()

        self.sio = sio = socketio.Server()
        self.app = app = flask.Flask(__name__)

        host = Config.get('driver.web', 'host')
        port = Config.getint('driver.web', 'port')
        self.addr = (host, port,)

        # wrap Flask application with engineio's middleware
        self.app = socketio.Middleware(sio, app)

        @sio.on('connect')
        def connect(sid, environ):
            sio.emit('setup', {
                'boardCount': num_boards(),
                'clientPlugins': [],
            })

        @app.route('/')
        def index():
            return flask.send_from_directory(static_dir(), 'index.html')

        @app.route('/display/<path:path>')
        def display_statics(path):
            return flask.send_from_directory(static_dir(), path)

        eventlet.spawn(self._run)
        eventlet.sleep(0)

    def _run(self):
        # deploy as an eventlet WSGI server
        log.info("deploying wsgi server")
        eventlet.wsgi.server(eventlet.listen(self.addr), self.app)
        log.erro("wsgi server stopped")

    def output(self, frame):
        """
        Output a Frame to the Web-Interface.

        :param frame: Frame to transmit
        :type frame: lib.frame.Frame
        :return: lib.driver.webdriver.WebDriver
        """
        self.sio.emit("frame", {
            "rows": frame.rows,
            "leds": frame.leds
        })
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
