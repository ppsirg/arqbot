"""
Simulate a dron video stream given its id and server url.
python dron_sim.py --id dr123 --host http://localhost:8888
"""
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import aiohttp
import asyncio


# initialize the video stream and allow the camera sensor to
# warmup
vs = VideoStream(src=0).start()
time.sleep(2.0)


def generate():
    # loop over frames from the output stream
    while True:
        # read an image from video stream
        frame = vs.read()
        # reduce image to 400px
        frame = imutils.resize(frame, width=400)
        # put timestamp in video
        timestamp = datetime.datetime.now()
        cv2.putText(
            frame, timestamp.strftime("%A %d %B %Y %I:%M:%S%p"),
            (10, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1
            )
        # encode the frame in JPEG format
        flag, encodedImage = cv2.imencode(".jpg", frame)
        # ensure the frame was successfully encoded
        if not flag:
            continue
        # yield the output frame in the byte format
        yield(bytearray(encodedImage))


async def send_stream(client, url, data):
    async with client.post(url, data=data) as resp:
        return await resp.text()


async def main():
    # get drone config
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--id", type=str, required=True, help="dron id")
    ap.add_argument("-o", "--host", type=str, required=True, help="drone service url")
    args = vars(ap.parse_args())
    url = f'{args["host"]}/stream/{args["id"]}'
    # broadcast video feed
    async with aiohttp.ClientSession() as client:
        for chunk in generate():
            html = await send_stream(client, url, chunk)
            print(html)
            await asyncio.sleep(0.2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())