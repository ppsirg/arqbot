"""
Servicio videos.
"""
from tornado.web import RequestHandler
from tornado.gen import sleep
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from time import time
import os
from subprocess import call

rootFolder =  os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# load placeholder image for video widget
with open('src/assets/placeholder.jpeg', 'br') as t:
    cat_jpg = t.read()


class servicio_videos(RequestHandler):
    """
    Get data from drones and serves it to clients if they are allowed to.
    """
    frames = {}
    timestamps = {}

    def build_chunk(self, dt):
        """Build a video chunk, if not video, return placeholder image.
        """
        # if drone is not broadcasting, send a placeholder chunk instead
        if not dt:
            chunk = cat_jpg
        else:
            chunk = self.frames[dt]
        return b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + chunk + b'\r\n'

    async def get(self, dt):
        """Show video stream to users.
        """
        self.set_header('content-type', "multipart/x-mixed-replace; boundary=frame")
        while True:
            chunk = self.build_chunk(dt if dt in self.frames else None)
            self.write(chunk)
            self.flush()
            # if drone is broadcasting, send new pic every 0.2 sec, otherwise
            # send updates every 2 seconds
            await sleep(0.2 if dt in self.frames else 2)

    async def post(self, dt):
        """
        Get info from drones and save it for streaming.
        """
        if dt not in servicio_videos.frames:
            # check if stream is ok
            IOLoop.current().spawn_callback(self.monitoreo_servicio, dt)
            # build directory to save images to make video later
            if not os.path.exists(dt):
                os.mkdir(dt)
            servicio_videos.timestamps[dt] = time(), 0
        new_chunk = self.request.body
        # save new chunk to be consumed
        servicio_videos.frames[dt] = new_chunk
        # save chunk for later use as file to generate video
        await self.send_chunk_to_almacenaje(dt, new_chunk)
        self.write(dt)

    async def monitoreo_servicio(self, dt):
        """
        Close drone conection if server dont get new information in less than 10 seconds.
        """
        while dt in servicio_videos.timestamps:
            if time() - servicio_videos.timestamps[dt][0] > 9:
                servicio_videos.timestamps.pop(dt)
                servicio_videos.frames.pop(dt)
            await sleep(3)

    async def send_chunk_to_almacenaje(self, dt, new_chunk):
        client = AsyncHTTPClient()
        await client.fetch(
            f'http://localhost:8888/storage/{dt}',
            method='POST',
            body=new_chunk
            )

    