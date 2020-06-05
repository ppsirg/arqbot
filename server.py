"""
Drone services simulation backend.
"""
from tornado.ioloop import IOLoop
from tornado.web import Application
from dron_services import servicio_videos, servicio_almacenaje_videos


def make_app():
    return Application([
        (r"/stream/(\w+)", servicio_videos),
        (r"/storage/(\w+)", servicio_almacenaje_videos),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()