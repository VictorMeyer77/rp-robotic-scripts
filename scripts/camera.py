from time import sleep
from picamera import PiCamera
#import cv2
#import os

OUTPUT_DIR = "resources/output/image/camera"

"""
def image(cam, output_dir):
    ret, frame = cam.read()
    cv2.imwrite(os.path.join(output_dir, "image_buffer.png"), frame)


if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    image(camera, OUTPUT_DIR)
    camera.release()

"""
camera = PiCamera()
camera.resolution = (64, 64)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture("resources/output/image/camera/test.jpg")