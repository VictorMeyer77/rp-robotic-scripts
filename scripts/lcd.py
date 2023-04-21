"""

                        RASPBERRY   |   BREADBOARD  |   POTENTIOMETER
LCD                         X       | 40 D <-> 55 D |       X
Dupont wire M/F             X       |  55 A -> 55 - |       X
Dupont wire M/F             X       |  54 A -> 54 + |       X
Dupont wire M/F             X       |     53 A      |     CENTER
Dupont wire M/F          GPIO 37    |     52 A      |       X
Dupont wire M/F             X       |  51 A -> 51 - |       X
Dupont wire M/F          GPIO 35    |     50 A      |       X
Dupont wire M/F          GPIO 33    |     45 A      |       X
Dupont wire M/F          GPIO 31    |     44 A      |       X
Dupont wire M/F          GPIO 29    |     43 A      |       X
Dupont wire M/F          GPIO 23    |     42 A      |       X
Dupont wire M/F             X       |  41 A -> 41 + |       X
Dupont wire M/F             X       |  40 A -> 40 - |       X
Dupont wire M/F          GPIO 6     |     35 -      |       X
Dupont wire M/F          GPIO 2     |     30 +      |       X
Dupont wire M/F             X       |     15 -      |     RIGHT
Dupont wire M/F             X       |     10 +      |     LEFT

"""

from RPLCD.gpio import CharLCD
from RPi import GPIO
import time


def display(char_lcd):
    char_lcd.write_string("HELLO,\nWORLD !!!!")
    time.sleep(5)


def shutdown(char_lcd):
    char_lcd.clear()
    GPIO.cleanup()


if __name__ == "__main__":
    GPIO.setwarnings(False)
    lcd = CharLCD(cols=16,
                  rows=2,
                  pin_rs=37,
                  pin_e=35,
                  pins_data=[33, 31, 29, 23],
                  numbering_mode=GPIO.BOARD,
                  auto_linebreaks=True)
    display(lcd)
    shutdown(lcd)
