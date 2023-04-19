"""

* resistance - RPI 9 - BB (-1)

* note: anode (long leg of the led) should connect to the positive circuit, cathode to the negative (ground)

"""

import RPi.GPIO as GPIO
import time

GPIO_PIN = 11


def flashing(pin):
    state = GPIO.input(pin)
    if state:
        GPIO.output(pin, GPIO.LOW)
    else:
        GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)


if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    while True:
        flashing(GPIO_PIN)
