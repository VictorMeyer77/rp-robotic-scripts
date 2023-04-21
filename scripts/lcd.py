from RPLCD.gpio import CharLCD
from RPi import GPIO
import time


lcd = CharLCD(cols=16,
              rows=2,
              pin_rs=37,
              pin_e=35,
              pins_data=[33, 31, 29, 23],
              numbering_mode=GPIO.BOARD,
              auto_linebreaks=True)

lcd.write_string("\tHELLO,\n \tWORLD !!!! 😀")
time.sleep(5)
lcd.clear()
GPIO.cleanup()
