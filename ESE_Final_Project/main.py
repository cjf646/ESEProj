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


if __name__ == '__main__':
#     engine = pyttsx3.init()
#     voice = engine.getProperty('voices')
#     engine.setProperty('voice', voice[32].id)
#     
#     engine.say("Hi, I am your superhero coach")
#     engine.runAndWait()
#     time.sleep(1)
#     engine.say("Please say one thing you are grateful for before you go to sleep! ok go")
#     engine.runAndWait()
#     setupGPIO()
#     gratitudeVoiceDeviceInteraction()
    
#     checkStreakAndActivityPoints()
    
#     setupGPIO()
#     
#     beginMorning()
    

#     
    
    setupGPIO()
    boxRun()
    time.sleep(1)
    lockOn()
           
    waitForEvents()


