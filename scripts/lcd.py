from RPLCD.gpio import CharLCD
from RPi import GPIO
import time

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)

lcd.write_string("TAIVE!!!!")
time.sleep(5)
lcd.clear()
