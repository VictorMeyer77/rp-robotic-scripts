"""
    sudo apt-get install python3-picamera
"""

import time
import picamera
import datetime
import os

OUTPUT_DIR = "resources/output/image/camera"


def image(camera, output_dir):
    camera.capture(os.path.join(output_dir, str(datetime.datetime.now()) + '.jpg'))


def video(camera, output_dir):
    name = os.path.join(output_dir, time.strftime("%d.%m.%Y-%Hh%Mm%Ss"))
    camera.start_recording(name + ".h264")
    time.sleep(10)
    camera.stop_recording()
    command = "MP4Box -add " + name + ".h264 " + name + ".mp4"
    os.system(command)


if __name__ == "__main__":
    cam = picamera.PiCamera()
    cam.resolution = (2592, 1944)
    image(cam, OUTPUT_DIR)
    video(cam, OUTPUT_DIR)
