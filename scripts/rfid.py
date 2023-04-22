import RPi.GPIO as GPIO
from pirc522 import RFID
import time

USER = (
    ("user_a", [3, 92, 150, 6, 207]),
    ("user_b", [12, 160, 66, 99, 141]),
)


def authentication(user_list, badge_uid):
    match_user = list(filter(lambda user: user[1] == badge_uid, user_list))
    return "" if match_user == [] else match_user[0][0]


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

rc522 = RFID()

print("En attente d'un badge (pour quitter, Ctrl + c): ")

while True:

    rc522.wait_for_tag()
    (error, tag_type) = rc522.request()

    if not error:
        print(tag_type)
        (error, uid) = rc522.anticoll()

        if not error:
            print("Vous avez passé le badge avec l'id : {}".format(uid))

            user = authentication(USER, uid)
            if user == "":
                print("Vous êtes inconnu, dégagez !")
            else:
                print(f"Bonjour {user}")

            time.sleep(1)
