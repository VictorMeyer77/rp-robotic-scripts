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


def read_badge(user_list):
    (error, tag_type) = rc522.request()
    if not error:
        (error, uid) = rc522.anticoll()
        if not error:
            user = authentication(user_list, uid)
            if user == "":
                print("Unknown badge, get out !")
            else:
                print(f"Hello {user} !")
            time.sleep(1)


if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    rc522 = RFID()
    print("Waiting for badge (Quit: Ctrl + c): ")
    while True:
        read_badge(USER)
