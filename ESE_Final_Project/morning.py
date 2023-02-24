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

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


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
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

#     try:
#         return_data = db.child('Users').get()
#         all_data = return_data.val()
# 
#     # If there's an exception, retry the operation after waiting 5 seconds
#     except Exception as e:
#         print(f"Error reading data from database: {e}. Retrying in 5 seconds...")
#         time.sleep(5)
#         addActivity()



days = []
user_data = []
#     if all_data == None:
for x, y in all_data.items():
    days.append(x)
    user_data.append(y)
global run
run = True    
#     get user data of the most recent day
user_data = user_data[-2]
global activity1, activity2, activity3
for x, y in user_data.items():
    if x == 'Activity 1':
        activity1 = y
        print(activity1)
    if x == 'Activity 2':
        activity2 = y
        print(activity2)
    if x == 'Activity 3':
        activity3 = y
        print(activity3)



def beginMorning():
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[32].id)
    engine.say("Time to complete your activities! Press green button to start")
    engine.runAndWait()
    
    beginMorningRoutine()
    


def beginMorningRoutine():
    
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    
    awake = False

    while not (awake):
        if GPIO.input(6) == GPIO.LOW:
            switch3()
        
        time.sleep(0.1)

    # Clean up GPIO
    GPIO.cleanup()
#     detectActivitySelect()
#     while run:
#         
#         time.sleep(1)
#         beginMorningRoutine()
#     # Clean up GPIO
#     GPIO.cleanup()
# #     GPIO.add_event_detect(6, GPIO.FALLING, callback=switch3, bouncetime=1500)
# 
# #     GPIO.remove_event_detect(6)
# #     GPIO.add_event_detect(6, GPIO.FALLING, callback=switch3, bouncetime=1500)
        
def addActivity():   
    global activity1, activity2, activity3
    
#     detectActivitySelect()
#     detectDone()
    if activity_added == 1:
        activity_1 = False
        lcd.close(clear=True)
        lcd.write_string('   DO ACTIVITY')
        lcd.crlf()
        lcd.write_string(activity1)
        while not (activity_1):
            if GPIO.input(6) == GPIO.LOW:
                switch3()
            
            time.sleep(0.1)

        # Clean up GPIO
        GPIO.cleanup()
    
    if activity_added == 2:
        lcd.close(clear=True)
        lcd.write_string(activity1+"-DONE")
        lcd.crlf()
        lcd.write_string(activity2)
        lcd.crlf()
        print("?????????????????")
        activity_2 = False

        while not (activity_2):
            if GPIO.input(6) == GPIO.LOW:
                switch3()
            
            time.sleep(0.1)

        # Clean up GPIO
        GPIO.cleanup()
#         GPIO.remove_event_detect(13)
#         GPIO.add_event_detect(13, GPIO.FALLING, callback=donePresses, bouncetime=1500)
#         detectDone()
#         detectActivitySelect()
        
    if activity_added == 3:
        lcd.close(clear=True)
        lcd.write_string(activity1+"-DONE")
        lcd.crlf()
        lcd.write_string(activity2+"-DONE")
        lcd.crlf()
        lcd.write_string(activity3)
        lcd.crlf()
        activity_3 = False

        while not (activity_3):
            if GPIO.input(6) == GPIO.LOW:
                switch3()
            
            time.sleep(0.1)

        # Clean up GPIO
        GPIO.cleanup()
#         GPIO.remove_event_detect(13)
#         GPIO.add_event_detect(13, GPIO.FALLING, callback=donePresses, bouncetime=1500)
# #         detectDone()
#         detectActivitySelect()
    if activity_added == 4:
        lcd.close(clear=True)
        lcd.write_string(activity1+"-DONE")
        lcd.crlf()
        lcd.write_string(activity2+"-DONE")
        lcd.crlf()
        lcd.write_string(activity3+"-DONE")
        lcd.crlf()
        mood()

        
#         GPIO.remove_event_detect(13)
#         GPIO.add_event_detect(13, GPIO.FALLING, callback=donePresses, bouncetime=1500) 
#     detectDone()   
#         detectActivitySelect()
#         GPIO.remove_event_detect(6)
#         setupGPIO()
        
    
        
def switch3(ev=None):
    
    select_button = False
#     global select_button, activity
    global activity_added
    select_button = not select_button
    
    
    if select_button == True:
        activity_added += 1
        print("activities added =", activity_added)
        engine = pyttsx3.init()
        voice = engine.getProperty('voices')
        engine.setProperty('voice', voice[32].id)
        if activity_added == 1:
            engine.say("Awesome, you are up. Now do the current activity on screen, and press the green button again when complete.")
            engine.runAndWait()
        addActivity()       
        sleep(1)

def donePresses(ev=None):
    
    select_button = False
#     global select_button, activity
    global activity_done
    select_button = not select_button
    
    
    if select_button == True:
        activity_done += 1
               
        addActivity()       
        sleep(1)

    
def detectActivitySelect():
    GPIO.remove_event_detect(6)
    GPIO.add_event_detect(6, GPIO.FALLING, callback=switch3, bouncetime=1500)



def detectDone():
    GPIO.remove_event_detect(13)
    GPIO.add_event_detect(13, GPIO.FALLING, callback=donePresses, bouncetime=1500)
    
def waitForEvents():
        while True:
            sleep(1)





def waitForEvents():
        while True:
            sleep(1)
