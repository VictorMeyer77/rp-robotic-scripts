import RPi.GPIO as GPIO
from pirc522 import RFID
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

rc522 = RFID()

print("En attente d'un badge (pour quitter, Ctrl + c): ")

while True:

    rc522.wait_for_tag()
    (error, tag_type) = rc522.request()

    if not error:
        (error, uid) = rc522.anticoll()

        if not error:
            print("Vous avez passé le badge avec l'id : {}".format(uid))
            time.sleep(1)
