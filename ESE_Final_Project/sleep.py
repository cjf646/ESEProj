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



def clockRunningNow():

# Hassan sleep sensor data
#  temp_data = tempMonitoring()
# each value is measured every 30 minutes
    from gpiozero import MotionSensor
    from datetime import datetime
    import time
# motion sensor activation
#     pir = MotionSensor(17)
    
    movements = 0
    avg_temp = 22
    avg_humidity = 60
    light_count = 10
    air_quality = 35
    feeling = "Happy"
    limit_switch = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.IN)
    
#     while True:
#       pir.wait_for_motion()
#       if (pir):
#         motion_count += 1
#         print(motion_count)
#       now1 = (datetime.now())
#       tstamp1 = "{0:%Y}-{0:%m}-{0:%d}_{0:%H}.{0:%M}.{0:%S}".format(now1)
#       filename = tstamp1 + "motion log.txt"
#       file = open("motion_log.txt", "a")
#       file.write("Motion detected " + tstamp1 + "\n")
#       pir.wait_for_no_motion()
#       print("STOPPED")
#       now2 = (datetime.now())
#       tstamp2 = "{0:%Y}-{0:%m}-{0:%d}_{0:%H}.{0:%M}.{0:%S}".format(now2)
#       file = open("motion_log.txt", "a")
#       file.write("Motion stopped " + tstamp2 + "\n")
#       time.sleep(1)
#     file.close()

    # after alarm goes off, store data
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
    alarm_times = []
    for x, y in all_data.items():
        days.append(x)
        print("what isd this", days)
        alarm_times.append(y)
        print("hello:", alarm_times)
        
    alarm_time = alarm_times[-2]
    
    for x, y in alarm_time.items():
        if x == 'Alarm Time hour':
            hour = y
        if x == 'Alarm time minute':
            minute = y
        if x == 'Activity 1':
            activity1 = y
        if x == 'Activity 2':
            activity2 = y
        if x == 'Activity 3':
            activity3 = y    
    
    print(hour)
    print(minute)
#     print("working?", alarm_time)
#     for x, y in alarm_time.items():
#         if x == 'Alarm Time hour':
#             hour = y
#         if x == 'Alarm time minute':
#             minute = y
#         if x == 'Activity 1':
#             activity1 = y
#         if x == 'Activity 2':
#             activity2 = y
#         if x == 'Activity 3':
#             activity3 = y
#     print(hour)
#     print(minute)
#     data = {'Temperature Data': temp_data, 'Alarm Time hour': hour, 'Alarm time minute': minute, 'Activity 1': activity1,'Activity 2': activity2, 'Activity 3': activity3}
#     db.child("Users").child(days[-2]).set(data)









# current time display during user sleeping

    while(1):
#         check to see if box is opened
        state_ls = GPIO.input(22)
        if state_ls == GPIO.LOW:
            limit_switch += 1
            print(limit_switch)
#         motion sensor code
#         pir.wait_for_motion()
#         if (pir):
#             movements += 1
#             print(movements)
#         now1 = (datetime.now())
#         tstamp1 = "{0:%Y}-{0:%m}-{0:%d}_{0:%H}.{0:%M}.{0:%S}".format(now1)
#         filename = tstamp1 + "motion log.txt"
#         file = open("motion_log.txt", "a")
#         file.write("Motion detected " + tstamp1 + "\n")
#         pir.wait_for_no_motion()
#         print("STOPPED")
#         now2 = (datetime.now())
#         tstamp2 = "{0:%Y}-{0:%m}-{0:%d}_{0:%H}.{0:%M}.{0:%S}".format(now2)
#         file = open("motion_log.txt", "a")
#         file.write("Motion stopped " + tstamp2 + "\n")
#         time.sleep(1)

        tim = time.localtime()
        current_time = time.strftime("%I:%M %p", tim)
        lcd.close(clear=True)
        lcd.write_string("Current Time")
        lcd.crlf()
        lcd.write_string(current_time)
        current_hour = str(time.strftime("%I", tim))
        current_minute = str(time.strftime("%M", tim))
        print(current_hour)
        print(current_minute)
        #setting hour to contain a zero at the start if needed
        hour = str(adjustHour(hour))
        minute = str(adjustMinute(minute))
        current_hour = str(current_hour)
        current_minute = str(current_minute)
        print("alarm hour", hour)
        print("current_hour", current_hour)
        print("alarm minute", minute)
        print("current minute", current_minute)

        if (current_hour == hour) and (current_minute == minute):
#             turning on LED light strips
            GPIO.setup(24, GPIO.OUT)
            GPIO.output(24, GPIO.HIGH)
            
            print("WORKING")
            now = datetime.now()
            month = now.strftime("%m")
            day = now.strftime("%d")
            year = now.strftime("%Y")
            
            data = {'Limit Switch': limit_switch, 'Day': day, 'Month': month, 'Year': year, 'Current Time': current_time, 'Feeling': feeling, 'Movements': movements, 'Average Temperature': avg_temp, 'Average humidity': avg_humidity, 'Light triggered': light_count, 'Air quality': air_quality, 'Alarm Time hour': hour, 'Alarm time minute': minute, 'Activity 1': activity1,'Activity 2': activity2, 'Activity 3': activity3}
            db.child("CurtisFicor").child(days[-2]).set(data)
            db.child("Users").child(days[-2]).set(data)      
            beginMorning()
            
            
            
            break
            
            
# Activation of Speaker
            

        else:
            print("NOT WORKING. MONITOR YOUR SLEEP NOW. HASSAN THIS IS WHERE YOUR FUNCTION WILL GO")

        time.sleep(2)
      
#     file.close()
    
    
#          
#         firebaseConfig = {
#   'apiKey': "AIzaSyBPmuCMq_v2euR4n4qW1hBnosQuBTgtW5k",
#   'authDomain': "habits-b5b42.firebaseapp.com",
#   'databaseURL': "https://habits-b5b42-default-rtdb.firebaseio.com",
#   'projectId': "habits-b5b42",
#   'storageBucket': "habits-b5b42.appspot.com",
#   'messagingSenderId': "134941482333",
#   'appId': "1:134941482333:web:b8acc728562e6ad8789cb4",
#   'measurementId': "G-YWS3LCTD6E"
# }
#         actual_minute = tim.tm_min
#         actual_hour = tim.tm_hour
#         firebase = pyrebase.initialize_app(firebaseConfig)
#         db = firebase.database()
#         
#         Users = db.child("Users").get()
#         alarm_time = []
#         for user in Users.each():
#             alarm = user.val()
#             print("what is this????", alarm)
#             alarm_time.append(alarm)
#         
#         print(alarm_time[0])
#         print(alarm_time[1])
#         print(actual_minute)
#         print(actual_hour)
#         if actual_minute == alarm_time[1] and actual_hour == alarm_time[0]:
#             print("WORKING")
#         else:
#             print("NOT WORKING")          
# 
#          time.sleep(60)
# 






        
        
#         hour = db.child("Users").get("Alarm Time hour")
#         minute = db.child("Users").get("Alarm time minute")
#         print(hour.val())
#         print(minute.val())        
        
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








def adjustHour(hour):
    if hour == 1:
        hour = "{:02d}".format(hour)
        return hour
    if hour == 2:
        hour = "{:02d}".format(hour)
        return hour
    if hour == 3:
        hour = "{:02d}".format(hour)
        return hour
    if hour == 4:
        hour = "{:02d}".format(hour)
        return hour
    if hour == 5:
        hour = "{:02d}".format(hour)
        return hour
    if hour == 6:
        hour = "{:02d}".format(hour)
        return hour
    if hour == 7:
        hour = "{:02d}".format(hour)
        return hour
    if hour == 8:
        hour = "{:02d}".format(hour)
        return hour
    if hour == 9:
        hour = "{:02d}".format(hour)
        
    else:
        return hour
    
def adjustMinute(minute):
    if minute == 0:
        minute = "{:02d}".format(minute)
        return minute
    if minute == 1:
        minute = "{:02d}".format(minute)
        return minute
    if minute == 2:
        minute = "{:02d}".format(minute)
        return minute
    if minute == 3:
        minute = "{:02d}".format(minute)
        return minute
    if minute == 4:
        minute = "{:02d}".format(minute)
        return minute
    if minute == 5:
        minute = "{:02d}".format(minute)
        return minute
    if minute == 6:
        minute = "{:02d}".format(minute)
        return minute
    if minute == 7:
        minute = "{:02d}".format(minute)
        return minute
    if minute == 8:
        minute = "{:02d}".format(minute)
        return minute
    if minute == 9:
        minute = "{:02d}".format(minute)
        
    else:
        return minute        
