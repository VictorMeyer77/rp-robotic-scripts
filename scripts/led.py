"""

                        RASPBERRY   |   BREADBOARD
Dupont wire M/F         GPIO 11     |   16 A
Dupont wire M/F         GPIO 9      |   10 A
Resistance Right           X        |   15 D
Resistance Left            X        |   10 D
Led anode                  X        |   16 C
Led cathode                X        |   15 C

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
