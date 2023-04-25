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
