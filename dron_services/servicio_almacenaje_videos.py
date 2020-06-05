"""
Drone services simulation backend.
"""
from tornado.web import RequestHandler
from tornado.gen import sleep
from tornado.ioloop import IOLoop
from time import time
from aiofile import AIOFile
import os
from subprocess import call

rootFolder =  os.path.dirname(os.path.abspath(os.path.dirname(__file__)))


class servicio_almacenaje_videos(RequestHandler):
    """
    Get data from drones and serves it to clients if they are allowed to.
    """
    timestamps = {}
    rootFolder =  os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

    def get(self, dt):
        self.write({
            'videos': self.catalogo_videos(dt)
        })

    async def post(self, dt):
        """
        Get info from drones and save it for streaming.
        """
        if dt not in servicio_almacenaje_videos.timestamps:
            # check if stream is ok
            IOLoop.current().spawn_callback(self.monitoreo_servicio, dt)
            # build directory to save images to make video later
            if not os.path.exists(dt):
                os.mkdir(dt)
            servicio_almacenaje_videos.timestamps[dt] = time(), 0
        # save chunk for later use as file to generate video
        await self.constructor_video_almacenaje(dt, self.request.body)
        self.write(dt)

    async def constructor_video_almacenaje(self, dt, new_chunk):
        """
        Save any chunk as image in disk as video frame.
        """
        count = servicio_almacenaje_videos.timestamps[dt][1] + 1
        servicio_almacenaje_videos.timestamps[dt] = time(), count
        new_file = os.path.join(os.path.abspath(dt),f'{count}.jpg')
        # save image in async non-blocking way
        async with AIOFile(new_file, 'ab') as fl:
            await fl.write(new_chunk)

    async def constructor_video_compilador(self, fl):
        """
        Buid mp4 video once drone streamin is finished.
        """
        tsp = time()
        order = f'ffmpeg -r 4 -i {fl}/%d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p {fl}_{tsp}.mp4'
        generateord = order.split(' ')
        call(generateord)
        call(f'rm -rf {fl}'.split(' '))

    async def monitoreo_servicio(self, dt):
        """Close drone conection if server dont get new information in less than 9 seconds.
        """
        while dt in servicio_almacenaje_videos.timestamps:
            if time() - servicio_almacenaje_videos.timestamps[dt][0] > 9:
                servicio_almacenaje_videos.timestamps.pop(dt)
                await self.constructor_video_compilador(dt)
            await sleep(3)

    def catalogo_videos(self, dt):
        """
        Return videos that belongs to a drone.
        """
        return [a for a in os.listdir(rootFolder) if a.endswith('.mp4') and a.startswith(dt)]
