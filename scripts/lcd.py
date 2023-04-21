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
    lcd = CharLCD(cols=16,
                  rows=2,
                  pin_rs=37,
                  pin_e=35,
                  pins_data=[33, 31, 29, 23],
                  numbering_mode=GPIO.BOARD,
                  auto_linebreaks=True)
    display(lcd)
    shutdown(lcd)
