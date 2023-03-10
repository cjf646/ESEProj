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
# GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)




def mood():
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[32].id)
    lcd.close(clear=True)
    lcd.write_string('SELECT A MOOD')
    lcd.crlf()
    lcd.write_string('PUSHBUTTON. OR GREEN')
    lcd.crlf()
    lcd.write_string('BUTTON FOR READY')
    lcd.crlf()
    
    engine.say("Select one of the mood pushbuttons that indicate how you are feeling right now. Or press green button if you are ready to start the day.")
    engine.runAndWait()
    feelingRecognizer()
 
# def button_pressed(channel):
#     if channel == 17:
#         print("SAD pressed")
#     elif channel == 27:
#         print("READY pressed")
#     global keep_running
#     keep_running = False
    
    

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
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    sad_pressed = False
    ready_pressed = False
    happy_pressed = False
    excited_pressed = False
    worried_pressed = False
    angry_pressed = False
    scared_pressed = False

    while not (sad_pressed and ready_pressed and worried_pressed and excited_pressed and angry_pressed and happy_pressed and scared_pressed):
        if GPIO.input(23) == GPIO.LOW:
            print("SAD pressed")
            feeling = "Sad"
            camera(feeling)
            sad_pressed = True
        if GPIO.input(6) == GPIO.LOW:
            print("READY pressed")
            feeling = "Ready"
            camera(feeling)
            ready_pressed = True
        if GPIO.input(7) == GPIO.LOW:
            print("WORRIED pressed")
            feeling = "Worried"
            camera(feeling)
            worried_pressed = True
        if GPIO.input(12) == GPIO.LOW:
            print("EXCITED pressed")
            feeling = "Excited"
            camera(feeling)
            excited_pressed = True
        if GPIO.input(16) == GPIO.LOW:
            print("ANGRY pressed")
            feeling = "Angry"
            camera(feeling)
            angry_pressed = True
        if GPIO.input(21) == GPIO.LOW:
            print("HAPPY pressed")
            feeling = "Happy"
            camera(feeling)
            happy_pressed = True
        if GPIO.input(20) == GPIO.LOW:
            print("SCARED pressed")
            feeling = "Scared"
            camera(feeling)
            scared_pressed = True
        time.sleep(0.1)

    # Clean up GPIO
    GPIO.cleanup()

def camera(feeling):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[32].id)

    lcd.close(clear=True)
    lcd.write_string('DRAW HOW YOU FEEL')
    lcd.crlf()
    lcd.write_string('ON BODY MAP. PRESS')
    lcd.crlf()
    lcd.write_string('GREEN BUTTON AFTER')
    lcd.crlf()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    engine.say("Now draw how you are feeling or what is on your mind on body map, then press green button again to snap a picture of your work.")
    engine.runAndWait()
    time.sleep(2)
    
    
    
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
            engine.say("Nice. Now get your parent to open the box with their fob!")
            engine.runAndWait()
            print("pushed")
            now = datetime.now()
            dt = now.strftime("%d%m%Y%H:%M:%S")
            name = dt+".jpg"
            camera.capture(name)
            print(name+" saved")
            storage.child(name).put(name)
#             storage.child(name).put(name)
            url = storage.child(name).get_url(None)
            print("Image sent")
            print(url)
            os.remove(name)
            print("File Removed")
            return_data = db.child('Users').get()
            all_data = return_data.val()      
            days = []     
            for x, y in all_data.items():
                days.append(x)
            
            print(feeling)
            work = {'Drawing Link': url, 'Feeling': feeling}
            db.child("Users").child(days[-2]).update(work)
            
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
