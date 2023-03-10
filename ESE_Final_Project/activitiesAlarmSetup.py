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

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time
import datetime

from firebase import firebase
import pyttsx3
import pyrebase
from time import sleep
import subprocess


# tim = time.localtime()
# current_time = time.strftime("%I:%M %p", tim)
# hour = 7
minute = 0

activate_lcd_screen = False
count = 0

set_hour = 7
set_minute = 60
    
def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    
    
#     gpio 26 is ref light indicator when wireless charger is activated
    GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
#     wired to a green LED
    GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
#     sends signal to start screen when phone is in box
#     GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     red pusbutton to navigate between time and activities
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     green pushbutton to select time and activities, etc
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    lockOff()

 



def lockOn(ev=None):
#     GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)
    
    time.sleep(3)
#     subprocess.call(['/home/cjf646/run_again.sh'])
    setClockHour()
    
    
#     lockOff()
#     time.sleep(3)
#     lockOn()
#     

def lockOff(ev=None):
#     GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.LOW)
    
    
def setClockHour(ev=None):
    tim = time.localtime()
    current_time = time.strftime("%I:%M %p", tim)
    lcd.close(clear=True)
    lcd.write_string('SET ALARM HOUR')
    lcd.crlf()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    lcd.write_string(' ')
    lcd.crlf() 
#     hour = tim.tm_hour
    lcd.write_string(f"Set hour:{set_hour}")
    lcd.crlf()
    detectNextHourPress()
    detectNextPress()
    
#     print(hour)
    minute = tim.tm_min
    
    
    t = datetime.time(14,30)
    lcd.write_string('')
    lcd.crlf()
    
def setClockMinute():
    tim = time.localtime()
    current_time = time.strftime("%I:%M %p", tim)
    lcd.close(clear=True)
    lcd.write_string('SET ALARM MINUTE')
    lcd.crlf()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    lcd.write_string(' ')
    lcd.crlf() 
#     hour = tim.tm_hour
    lcd.write_string(f"Set minute:{set_minute}")
    lcd.crlf()
    detectNextMinutePress()
    detectDonePress()
    
#     print(hour)
    minute = tim.tm_min
    
    
    t = datetime.time(14,30)
    lcd.write_string('')
    lcd.crlf()    
    
def switch(ev=None):
    global activate_lcd_screen, count
    activate_lcd_screen = not activate_lcd_screen
    count+= 1
    
    if activate_lcd_screen == True:    
        setClockHour()
        
def switch2(ev=None):
#     RED_Buton = False
    global set_hour
#     RED_Button = not RED_Button
    set_hour += 1
    if set_hour == 13:
        set_hour = 1
        setClockHour()
    setClockHour()
    
def switch3(ev=None):
#     RED_Buton = False
    global set_minute
#     RED_Button = not RED_Button
    
    set_minute += 1
    
    if set_minute == 61:
        set_minute = 0
        setClockMinute()   
    setClockMinute()
def detectNextHourPress():
    GPIO.remove_event_detect(13)
    GPIO.add_event_detect(13, GPIO.FALLING, callback=switch2, bouncetime=300)

def detectNextMinutePress():
    GPIO.remove_event_detect(13)
    GPIO.add_event_detect(13, GPIO.FALLING, callback=switch3, bouncetime=300)

    
def detectNextPress():
    GPIO.remove_event_detect(6)
    GPIO.add_event_detect(6, GPIO.FALLING, callback=switch3, bouncetime=300)
def detectDonePress():
    GPIO.remove_event_detect(6)
    GPIO.add_event_detect(6, GPIO.FALLING, callback=confirmTime, bouncetime=300)

def confirmTime(ev=None):
    lcd.close(clear=True)
    lcd.write_string('CONFIRM TIME')
    lcd.crlf()

    if set_minute == 0:
        lcd.write_string(f'{set_hour}:{set_minute}0 ')
        lcd.crlf()
    elif set_minute < 10 and set_minute > 0:
        lcd.write_string(f'{set_hour}:0{set_minute} ')
        lcd.crlf()
        
    else:
        lcd.write_string(f'{set_hour}:{set_minute} ')
        lcd.crlf()
        

    lcd.write_string('')
    detectConfirmPress(set_hour, set_minute)
    detectDeclinePress()
def detectDeclinePress():
    GPIO.remove_event_detect(13)
    GPIO.add_event_detect(13, GPIO.FALLING, callback=setClockHour, bouncetime=300)
def detectConfirmPress(set_hour, set_minute):
    GPIO.remove_event_detect(6)
    GPIO.add_event_detect(6, GPIO.FALLING, callback=save_data, bouncetime=300)
    
    
def save_data(ev=None):
    
    
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
    
    tim = time.localtime()
    current_time = time.strftime("%I:%M %p", tim)
    hour = set_hour
    minute = set_minute
        
    
    data = {'Alarm Time hour': hour, 'Alarm time minute': minute}
#     db.child("Users").child("initialization").set(data)
#     FBConn = firebase.FirebaseApplication('https://habits-b5b42-default-rtdb.firebaseio.com', None)
    return_data = db.child('Users').get()
    all_data = return_data.val()
    days = []
    
    for x, y in all_data.items():
        days.append(x)
    if len(days) == 1:
        db.child("Users").child(int(1)).set(data)
        run_screen()
    else:    
        new_day = int(days[-2]) + int(1)   
        db.child("Users").child(new_day).set(data)
        run_screen()
        
    
def waitForEvents():
        while True:
            time.sleep(1)


