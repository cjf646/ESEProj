import time
import datetime
from firebase import firebase
import pyttsx3
import time
import pyrebase

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


def clock():
    while(1):
        tim = time.localtime()
        current_time = time.strftime("%I:%M %p", tim)
        lcd.close(clear=True)
        lcd.write_string("Current Time")
        lcd.crlf()
        lcd.write_string(current_time)


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
        actual_minute = tim.tm_min
        actual_hour = tim.tm_hour
        firebase = pyrebase.initialize_app(firebaseConfig)
        db = firebase.database()

        Users = db.child("Users").get()
        alarm_time = []
        for user in Users.each():
            alarm = user.val()
            print("what is this????", alarm)
            alarm_time.append(alarm)

        print(alarm_time[0])
        print(alarm_time[1])
        print(actual_minute)
        print(actual_hour)
        if actual_minute == alarm_time[1] and actual_hour == alarm_time[0]:
            print("WORKING")
        else:
            print("NOT WORKING")



#         hour = db.child("Users").get("Alarm Time hour")
#         minute = db.child("Users").get("Alarm time minute")
#         print(hour.val())
#         print(minute.val())
        time.sleep(60)

#         actual_minute = tim.tm_min
#         actual_hour = tim.tm_hour
#
#         print(set_minute)
#         print(set_hour)
#
#         if actual_minute == set_minute and actual_hour == set_hour:
#             print("WORKING")
#         else:
#             print("NOT WORKING")
