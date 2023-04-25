"""

                        RASPBERRY   |   BREADBOARD
HC-SR04                     X       | 29 J <-> 32 J
Dupont wire M/F             2       |     32 F
Dupont wire M/F             16      |     31 F
Dupont wire M/F             X       | 29 F -> 23 E
Dupont wire M/F             39      |     23 B
Dupont wire M/F             18      |     30 C
Resistance                  X       | 23 A -> 30 A
Resistance                  X       | 30 G -> 30 D

Note: HC-SR04 in front of the outside

"""

import RPi.GPIO as GPIO
import time

GPIO_TRIGGER = 16
GPIO_ECHO = 18


def ultrasound_distance(gpio_trigger, gpio_echo):
    GPIO.output(gpio_trigger, True)
    time.sleep(0.00001)
    GPIO.output(gpio_trigger, False)
    start_time = time.time()
    stop_time = time.time()
    while GPIO.input(gpio_echo) == 0:
        start_time = time.time()
    while GPIO.input(gpio_echo) == 1:
        stop_time = time.time()
    return (stop_time - start_time) * 34300.0 / 2.0


if __name__ == '__main__':

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    try:
        while True:
            print("Distance = {:.1f} cm".format(ultrasound_distance(GPIO_TRIGGER, GPIO_ECHO)))
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
