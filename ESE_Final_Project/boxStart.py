from welcome import *
from activitiesAlarmSetup import *
from lcdScreen import *
from doActivities import *
from sleep import *
from morning import *
from recognizeFeelings import *
from parentVerification import *
from boxStart import *
from streak import *
# from globalVars import limit_triggered
from main import *

from picamera import PiCamera
import time
import datetime


from datetime import datetime
from picamera import PiCamera
from time import sleep
import os

import pyrebase

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# GPIO.setup(19, GPIO.IN)
# GPIO.setup(22, GPIO.IN)

# Import LCD library
from RPLCD import i2c

lcdmode = 'i2c'
cols = 20
rows = 4
charmap = 'A00'
i2c_expander = 'PCF8574'

# Generally 27 is the address;Find yours using: i2cdetect -y 1
address = 0x27
port = 1 # 0 on an older Raspberry Pi

# Initialise the LCD
lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
                  cols=cols, rows=rows)

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def boxRun():
    
    def limit_activation(ev=None):
        global checking
        print("Limit activated!")
        GPIO.remove_event_detect(19)
        checking += 1
        

    try:
        while True:
            # Do other stuff here
            print("in loop")
            time.sleep(1)
            tim = time.localtime()
            current_time = time.strftime("%I:%M %p", tim)
            lcd.close(clear=True)
            lcd.write_string("Current Time")
            lcd.crlf()
            lcd.write_string(current_time)
            if GPIO.input(19):
                GPIO.remove_event_detect(19)
                print("Pin 19 activated, checking pin 22...")
               
                if GPIO.input(22):
                                   
                    print("Limit activated!")
                    GPIO.remove_event_detect(22)
#                     lockOn()
                    break
#                     limit_activation()
            
#             break
    except:
        
        GPIO.cleanup()
    
