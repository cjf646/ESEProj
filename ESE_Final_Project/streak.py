import time
import datetime
from firebase import firebase
import pyttsx3
import time
import pyrebase
import os

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
GPIO.setmode(GPIO.BCM)
import sys
import importlib
completed_tasks = 0
import subprocess


def checkStreakAndActivityPoints():
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, GPIO.LOW)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.LOW)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, GPIO.LOW)
    time.sleep(2)
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[32].id)
    
    
    
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
        if x == "Average Temperature":
            Average_Temperature = y
        if x == "Average humidity":
            Average_Humidity = y
        if x == "Light triggered":
            Light_Triggered = y
        if x == "Movements":
            Motion_Sensor_Triggered = y
        if x == "LPG Concentration":
            LPG_Concentration = y
        if x == "CO2 Concentration":
            CO2_Concentration = y
        if x == "Smoke Concentration":
            Smoke_Concentration = y
        
            
    
    
    print("points from today", points_earned_today)
    previous_day = inside_each_day[-3]
    total_points = 0
    for x, y in previous_day.items():
        if x == "Total Points":
            total_points = y
            
    alltime_total_points = total_points + points_earned_today            
    print("All-Time Point Total: ",alltime_total_points)
    
    points_data = {'Streak': total_streak, 'Total Points': alltime_total_points}
    db.child("Users").child(days[-2]).update(points_data)
    
    
    
    lcd.clear()
    lcd.close(clear=True)
    lcd.write_string('')
    lcd.crlf()
    
    lcd.write_string("Current streak:" + str(total_streak))
    lcd.crlf()
    lcd.write_string("Point Total:" + str(alltime_total_points))
    lcd.crlf()
    
    engine.say("Good job. You can get your phone back now. You can also see your current streak and total points.")
    engine.runAndWait()
    engine.say("Check out the EmotionMirror app for more of your data.")
    engine.runAndWait()
    
    
    lcd.clear()
    lcd.close(clear=True)
    lcd.write_string("AVG LPG: " + str(LPG_Concentration) + " ppm")
    lcd.crlf()
    
    lcd.write_string("AVG CO2: " + str(CO2_Concentration)+ " ppm")
    lcd.crlf()
    lcd.write_string("AVG SMOKE: " + str(Smoke_Concentration)+ " ppm")
    lcd.crlf()
    
    time.sleep(10)
    
    lcd.clear()
    lcd.close(clear=True)
    lcd.write_string("AVG TEMP: " + str(Average_Temperature)+ " C")
    lcd.crlf()
    lcd.write_string("AVG HUMID: " + str(Average_Humidity)+ " %")
    lcd.crlf()
    lcd.write_string("LIGHT COUNT: " + str(Light_Triggered))
    lcd.crlf()
    lcd.write_string("MOTION COUNT: " + str(Motion_Sensor_Triggered))
    lcd.crlf()
    
    time.sleep(10)    
    
    
    
    os.system("sudo reboot")
#     os.call(['reboot'])
    
#	Delete txt files
    file_path1 = "/home/cjf646/gas_log.txt"
    file_path2 = "/home/cjf646/light_log.txt"
    file_path3 = "/home/cjf646/motion_log.txt"
    file_path4 = "/home/cjf646/temp-humid_log.txt"

    os.remove(file_path1)
    os.remove(file_path2)
    os.remove(file_path3)
    os.remove(file_path4)
    GPIO.cleanup()
    time.sleep(5)
#     subprocess.call("/usr/bin/sudo reboot")
    
    
#     # Define the message to display
#     message = '| Current streak: {} | Point Total: {} | LPG Concentration: {} | CO2 Concentration: {} | Smoke Concentration: {} | Average Temperature: {} | Average Humidity: {} | Light: {} | Motion: {} |'.format(total_streak, alltime_total_points, LPG_Concentration, CO2_Concentration, Smoke_Concentration, Average_Temperature, Average_Humidity, Light_Triggered, Motion_Sensor_Triggered)
#                                                                                                 
#     start_time = time.time()
#     # Scroll the message to the left every second
#     while True:
#         for i in range(len(message) - cols + 1):
#             lcd.write_string(message[i:i+cols])
#             time.sleep(0.3)
#             lcd.clear()
#             if time.time() > start_time + 25:
#                 break
#         if time.time() > start_time + 25:
#             break
#         
#     lcd.clear()


    
#     lcd.close(clear=True)
#     lcd.write_string('CO2 Concentration' + str(air_quality_co2))
#     lcd.crlf()
#     lcd.write_string('Light: ' + str(light))
#     lcd.crlf()
#     
#     lcd.write_string("Current streak:" + str(total_streak))
#     lcd.crlf()
#     lcd.write_string("Point Total:" + str(alltime_total_points))
#     lcd.crlf()
#     
#     subprocess.call(['/home/cjf646/run_again.sh'])
    # Stop the program
        

