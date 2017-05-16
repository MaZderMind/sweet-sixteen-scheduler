import threading
from pathlib import Path

import flask
from flask import Flask
from flask_socketio import SocketIO
from lib.driver.driver import Driver


def static_dir() -> str:
    return str(Path(__file__).parent / 'webdriver-static')


class WebDriver(Driver):
    def __init__(self, port=8080):
        super().__init__()

        self.thread = threading.Thread(target=self._run)
        self.app = app = Flask(__name__)
        self.sio = sio = SocketIO(app)

        self.port = port

        @sio.on('connect')
        def connect():
            print("connect")
            sio.emit('setup', {
                'boardCount': self.display.board_count,
                'clientPlugins': [],
            })

        @app.route('/')
        def index():
            return flask.send_from_directory(static_dir(), 'index.html')

        @app.route('/display/<path:path>')
        def display_statics(path):
            return flask.send_from_directory(static_dir(), path)

    def setup(self) -> 'WebDriver':
        self.thread.start()
        return self

    def _run(self):
        self.sio.run(self.app, port=self.port)
        print("run to completion")

    def output(self, frame: 'Frame') -> 'WebDriver':
        self.sio.emit("frame", frame.segments)
        return self

    def join(self) -> 'WebDriver':
        self.thread.join()
        pass
