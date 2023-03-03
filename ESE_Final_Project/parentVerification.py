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
from main import *

# Import LCD library
from RPLCD import i2c

# just added for camera testing
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
from datetime import datetime
from picamera import PiCamera
from time import sleep
import os

from firebase import firebase
import pyttsx3
import time
import pyrebase

# parent fob code
from mfrc522 import SimpleMFRC522

# select_button = False
activity_added = 0
# constants to initialise the LCD
activities_list = []

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


def parentFob():
    firebaseConfig ={
        'apiKey': "AIzaSyBPmuCMq_v2euR4n4qW1hBnosQuBTgtW5k",
        'authDomain': "habits-b5b42.firebaseapp.com",
        'databaseURL': "https://habits-b5b42-default-rtdb.firebaseio.com",
        'projectId': "habits-b5b42",
        'storageBucket': "habits-b5b42.appspot.com",
        'messagingSenderId': "134941482333",
        'appId': "1:134941482333:web:b8acc728562e6ad8789cb4",
        'measurementId': "G-YWS3LCTD6E"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    return_data = db.child('Users').get()
    all_data = return_data.val()




    days = []
    data = []
    for x, y in all_data.items():
        days.append(x)

        data.append(y)

    limit = data[-2]

    for x, y in limit.items():
        if x == 'Limit Switch':
            limit_switch = y


    if limit_switch == 1:
        print("BOX WAS NOT OPENED")
    #         wait to recieve parent fob
    #         fobWait()
    #         check streaks and total points
        while True:
            try:
                reader = SimpleMFRC522()
                print("checking")

                id, text = reader.read()
                print(id)
                if(id == 704238721961):
                    print("CORRECT FOB")
                    checkStreakAndActivityPoints()
                else:
                    print("INVALID FOB")
            finally:
                GPIO.cleanup()


    else:
        print("BOX WAS OPENED")
        lcd.close(clear=True)
        lcd.write_string('EMERGENCY STATE!!')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()

        lcd.write_string('BOX WAS OPENED      DURING NIGHT')
