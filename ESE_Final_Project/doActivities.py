from lcdScreen import *
from activitiesAlarmSetup import *
from welcome import *

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
    for x, y in all_data.items():
        days.append(x)
        print(days)


#     data = {'Activity 1': activities_list[0]}
#     db.child("Users").child(days[-2]).set(data)

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
        data = {'Activity 1': activities_list[0],'Activity 2': activities_list[1], 'Activity 3': activities_list[2]}
        db.child("Users").child(days[-2]).set(data)
    else:
        lcd.write_string(activities_list[1])
        lcd.crlf()
        data = {'Activity 2': activities_list[1]}
        db.child("Users").child(days[-2]).set(data)

#     gratitudeVoiceDeviceInteraction()
