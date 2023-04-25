import RPi.GPIO as GPIO
import time

GPIO_TRIGGER = 16
GPIO_ECHO = 18


def distance(gpio_trigger, gpio_echo):
    GPIO.output(gpio_trigger, True)
    time.sleep(0.00001)
    GPIO.output(gpio_trigger, False)
    start_time = time.time()
    stop_time = time.time()
    while GPIO.input(gpio_echo) == 0:
        start_time = time.time()
    while GPIO.input(gpio_echo) == 1:
        stop_time = time.time()
    dist = (stop_time - start_time) * 34300.0 / 2.0
    dist = 0.001 if dist > 1000.0 else dist
    return dist


if __name__ == '__main__':

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    try:
        while True:
            distance = distance(GPIO_TRIGGER, GPIO_ECHO)
            print("Distance = %.1f cm" % distance)
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
