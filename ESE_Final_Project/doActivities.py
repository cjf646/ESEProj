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


from time import sleep
from RPLCD import i2c
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

lcdmode = 'i2c'
cols = 20
rows = 4
charmap = 'A00'
i2c_expander = 'PCF8574'

address = 0x27
port = 1 # 0 on an older Raspberry Pi

lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
                  cols=cols, rows=rows)


import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

from firebase import firebase
import pyttsx3
import time
import pyrebase

#date module
import datetime








def check_alarm(set_hour, set_minute):
    if set_hour == int(hr) and set_minute == int(m):
        while green_button.value() != 1:
            lcd.clear()
            lcd.move_to(4,0)
            lcd.putstr("Wake up!")


def completeActivities(activities_list, activity_added, next_activity):
#     global activities_list
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
    days = []
    alarm_times = []
#     if all_data == None:
    for x, y in all_data.items():
        days.append(x)
        alarm_times.append(y)

    alarm_time = alarm_times[-2]
    for x, y in alarm_time.items():
        if x == 'Alarm Time hour':
            hour = y
        if x == 'Alarm time minute':
            minute = y

    lcd.close(clear=True)
    lcd.write_string('Activity List')
    lcd.crlf()
    lcd.write_string(activities_list[0])
    lcd.crlf()
    GPIO.output(12, GPIO.HIGH)

    if activity_added == 3:
        lcd.write_string(activities_list[1])
        lcd.crlf()
        lcd.write_string(activities_list[2])
        lcd.crlf()
        data = {'Alarm Time hour': hour, 'Alarm time minute': minute, 'Activity 1': activities_list[0],'Activity 2': activities_list[1], 'Activity 3': activities_list[2]}
        db.child("Users").child(days[-2]).set(data)
#         clockNight(hour, minute)

    else:
        lcd.write_string(activities_list[1])
        lcd.crlf()
        data = {'Activity 2': activities_list[1]}
        db.child("Users").child(days[-2]).set(data[2])


    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[10].id)

    engine.say("Hi, I am your superhero coach")
    engine.runAndWait()
    time.sleep(1)
    engine.say("Please say one thing you are grateful for before you go to sleep! ok go")
    engine.runAndWait()

    gratitudeVoiceDeviceInteraction()


def listening():
    listening = True

    while listening:
    #keyword = "activate"
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            recognizer.adjust_for_ambient_noise(source)
            recognizer.dynamic_energy_threshold = 2500


            try:
                print("Listening...")
                GPIO.output(26, GPIO.HIGH)
                audio = recognizer.listen(source)
                GPIO.output(26, GPIO.LOW)
                superhero_name = recognizer.recognize_google(audio)

                return superhero_name

            except sr.UnknownValueError:
                print("Didn't recognize that.")




def gratitudeVoiceDeviceInteraction():
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('voice', voice[10].id)
    engine.say("Hi, I am your superhero coach")
    engine.runAndWait()
    gratitude_text = listening()
    substring = "I am grateful"
    if substring in gratitude_text:

        engine.say("Did you say:" + gratitude_text)
        engine.runAndWait()
        yes_or_no = listening()
        yes = "yes"
        if yes in yes_or_no:
            engine.say("Yes you are very grateful for that. Have a great sleep!")
            engine.runAndWait()

            clockRunningNow()
    else:
        engine.say("That is not what you are supposed to say. Try again")
        engine.runAndWait()
        gratitudeVoiceDeviceInteraction()
    time.sleep(1)
