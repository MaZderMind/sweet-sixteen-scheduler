import asyncio
from pathlib import Path
from threading import Thread

import socketio
from aiohttp import web
from aiohttp_index import IndexMiddleware

from lib.driver.driver import Driver

DISPLAY = '/display'


class WebDriver(Driver):
    namespace = '/display'

    def __init__(self, port=8080):
        super().__init__()

        self.port = port
        self.thread = Thread(target=self._run)
        self.sio = sio = socketio.AsyncServer(async_mode='aiohttp')
        self.app = app = web.Application(middlewares=[
            IndexMiddleware(),
        ])
        sio.attach(app)
        self._setup_app(app)

        @sio.on('connect', namespace=WebDriver.namespace)
        def connect(sid, environ):
            print("connect ", sid)
            yield from sio.emit('setup', {
                'foo': 'bar'
            }, namespace=WebDriver.namespace)

    def _static_dir(self) -> str:
        return str(Path(__file__).parent / 'webdriver-static')

    def _setup_app(self, app):
        self.app.router.add_static(
            '/',
            path=self._static_dir(),
            name='static')

    def setup(self) -> 'WebDriver':
        self.thread.start()
        return self

    def _run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        web.run_app(self.app, port=self.port)

    def output(self, frame: 'Frame') -> 'WebDriver':
        #self.sio.emit("frame", frame, namespace='/display')
        pass

    def join(self) -> 'WebDriver':
        self.thread.join()
        pass
