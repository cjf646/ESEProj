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

import pyrebase
from firebase import firebase
# select_button = False
activity_added = 0
activity_done = 0
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

import RPi.GPIO as GPIO
# GPIO.setwarnings(False)

import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[32].id)
def mood():
    
    
    engine.say("Select one of the mood pushbuttons that indicate how you are feeling right now")
    engine.runAndWait()
    feelingRecognizer()
 
def button_pressed(channel):
    if channel == 17:
        print("SAD pressed")
    elif channel == 27:
        print("READY pressed")
    global keep_running
    keep_running = False

# def feelingRecognizer():
#     global keep_running
#     keep_running = True
#     print("hello")
# #     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# 
#     sadPress()
#     readyPress()
#     
#     while keep_running:
#         
#         time.sleep(1)
#         feelingRecognizer()
#     # Clean up GPIO
#     GPIO.cleanup()
def feelingRecognizer():
    global keep_running
    keep_running = True
    print("hello")
    # GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    sad_pressed = False
    ready_pressed = False
    happy_pressed = False
    excited_pressed = False
    worried_pressed = False
    angry_pressed = False
    _pressed = False

    while not (sad_pressed and ready_pressed):
        if GPIO.input(17) == GPIO.LOW:
            print("SAD pressed")
            feeling = "Sad"
            camera(feeling)
            sad_pressed = True
        if GPIO.input(27) == GPIO.LOW:
            print("READY pressed")
            feeling = "Ready"
            camera(feeling)
            ready_pressed = True
        time.sleep(0.1)

    # Clean up GPIO
    GPIO.cleanup()

def camera(feeling):    
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    engine.say("Now draw how you are feeling or what is on your mind on body map, then press green button again.")
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
    
    db = firebase.database()

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
            storage.child(name).put(name)
            url = storage.child(name).get_url(None)
            print("Image sent")
            print(url)
            os.remove(name)
            print("File Removed")
            return_data = db.child('Users').get()
            all_data = return_data.val()
            print("Hello")      
            days = []
            print("Hello")
            for x, y in all_data.items():
                days.append(x)
            print("Hello")
            print(feeling)
            work = {'Drawing Link': url, 'Feeling': feeling}
            db.child("Users").child(days[-2]).update(work)
            print("Hello")
            sleep(5)
            break

      except:
            camera.close()   
        
    parentFob()
    
    
# def readyPress():
#     GPIO.remove_event_detect(27)
#     GPIO.add_event_detect(27, GPIO.FALLING, callback=button_pressed, bouncetime=300)
# def sadPress():
#     GPIO.remove_event_detect(17)
#     GPIO.add_event_detect(17, GPIO.FALLING, callback=button_pressed, bouncetime=300)
#     
