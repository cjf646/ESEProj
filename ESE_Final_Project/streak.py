import time
import datetime
from firebase import firebase
import pyttsx3
import time
import pyrebase

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
import sys
import importlib
completed_tasks = 0
def checkStreakAndActivityPoints():
    global completed_tasks

    completed_tasks += 1
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
    db = firebase.database()
    return_data = db.child('Users').get()
    all_data = return_data.val()
    print(all_data)
    
    
    
    
    days = []
    inside_each_day = []
    for x, y in all_data.items():
        days.append(x)
        
        inside_each_day.append(y)
    
    previous_day = inside_each_day[-3]
    previous_day_streak = 0
    for x, y in previous_day.items():
        if x == "Streak":
            previous_day_streak = y
            
    total_streak = previous_day_streak + completed_tasks            
    print("Current day streak:", total_streak)
    
    
    previous_day = inside_each_day[-2]
    points_earned_today = 0
    for x, y in previous_day.items():
        if x == "Gratitude":
            points_earned_today += 1
        if x == "Activity 1":
            points_earned_today += 1
        if x == "Activity 2":
            points_earned_today += 1            
        if x == "Activity 3":
            points_earned_today += 1
        if x == "Feeling":
            points_earned_today += 1          
        if x == "Drawing Link":
            points_earned_today += 1
            
         
    print("points from today", points_earned_today)
    previous_day = inside_each_day[-3]
    previous_day_points = 0
    for x, y in previous_day.items():
        if x == "Total Points":
            total_points = y
            
    alltime_total_points = previous_day_points + points_earned_today            
    print("All-Time Point Total: ",alltime_total_points)
    
    lcd.close(clear=True)
    lcd.write_string('')
    lcd.crlf()
    lcd.write_string('')
    lcd.crlf()
    lcd.write_string("Current streak:" + str(total_streak))
    lcd.crlf()
    lcd.write_string("Point Total:" + str(alltime_total_points))
    lcd.crlf()
    main()
#     importlib.reload(sys.modules['__main__'])
