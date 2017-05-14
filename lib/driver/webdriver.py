import asyncio
from threading import Thread

import socketio
from aiohttp import web

from lib.driver.driver import Driver


class WebDriver(Driver):
    def __init__(self, port=8080):
        super().__init__()

        self.port = port
        self.thread = Thread(target=self._run)
        self.sio = sio = socketio.AsyncServer()
        self.app = app = web.Application()
        sio.attach(app)

    def setup(self) -> 'WebDriver':
        self.thread.start()
        return self

    def _run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        web.run_app(self.app, port=self.port)

    def output(self, frame: 'Frame') -> 'WebDriver':
        print("webdriver output frame", frame)
        pass

    def join(self) -> 'WebDriver':
        self.thread.join()
        pass
