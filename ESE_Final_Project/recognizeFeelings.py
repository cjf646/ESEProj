from welcome import *
from activitiesAlarmSetup import *
from lcdScreen import *
from doActivities import *
from sleep import *
from activitiesAlarmSetup import *

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

import pyrebase

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




def feelingRecognizer():

    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[32].id)




    engine.say("Select one of the mood pushbuttons that indicate how you are feeling right now")
    engine.runAndWait()

    firebaseConfig = {
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

    storage = firebase.storage()

    camera = PiCamera()

    while True:
      try:
        if GPIO.input(6) == GPIO.LOW:
            print("pushed")
            now = datetime.now()
            dt = now.strftime("%d%m%Y%H:%M:%S")
            name = dt+".jpg"
            camera.capture(name)
            print(name+" saved")
            storage.child(name).put(name)
            url = storage.child(name).get_url(None)
            print("Image sent. URL:", url)
            print("Image sent")
            os.remove(name)
            print("File Removed")
            sleep(5)


      except:
            camera.close()
