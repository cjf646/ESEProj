import numpy as np
import matplotlib.pyplot as plt

from gpiozero import MotionSensor 
from datetime import datetime
from firebase import firebase
import pyttsx3
import time
import pyrebase
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_dht

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


# each value is measured every 30 minutes
    from gpiozero import MotionSensor
    from datetime import datetime
    import time
    
    
    limit_switch = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.IN)
    
#   gas sensor variables
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1015(i2c)
    channels = [AnalogIn(ads, ADS.P0), AnalogIn(ads, ADS.P1), AnalogIn(ads, ADS.P2)]
    gas_counter = 0
    lpg_sum = 0
    co2_sum = 0
    smoke_sum = 0
    ZERO_LPG = 500
    ZERO_CO2 = 500
    ZERO_SMOKE = 500
    
#   light variables
    readPIN = 14
    light_counter = 0
    value = 0
    conv = 0
    GPIO.setmode (GPIO.BCM) 
    GPIO.setup(readPIN, GPIO.IN)
    
#	motion variables
    pir = MotionSensor(17) 
    motion_counter = 0
    plot = "1"
    zero = "0"

#   temp/humid variables
    dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)
    th_counter = 0
    sum_temp = 0.0
    sum_humid = 0.0
    

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
        alarm_times.append(y)
        
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
    
# current time display during user sleeping
    while(1):
#         DISPLAY CURRENT TIME
        tim = time.localtime()
        current_time = time.strftime("%I:%M %p", tim)
        lcd.close(clear=True)
        lcd.write_string("Current Time")
        lcd.crlf()
        lcd.write_string(current_time)
        #gas_code
        lpg = channels[0].value
        co2 = channels[1].value
        smoke = channels[2].value

        lpg_conc = (lpg - ZERO_LPG) / 10.0
        co2_conc = (co2 - ZERO_CO2) / 10.0
        smoke_conc = (smoke - ZERO_SMOKE) / 10.0
                
        gas_counter += 1

        lpg_sum = lpg_sum + lpg_conc
        co2_sum = co2_sum + co2_conc
        smoke_sum = smoke_sum + smoke_conc

        average_lpg = int(lpg_sum/gas_counter)        
        average_co2 = int(co2_sum/gas_counter)          
        average_smoke = int(smoke_sum/gas_counter) 
                
        lpg_conv = str(lpg_conc)
        co2_conv = str(co2_conc)
        smoke_conv = str(smoke_conc)

        now = (datetime.now())
        tstamp = "{0:%H}{0:%M}{0:%S}".format(now)

        file = open("gas_log.txt", "a")
        file.write(lpg_conv + " ") 
        file.write(co2_conv + " ") 
        file.write(smoke_conv + " ")    
        file.write(tstamp + "\n")         

        print('LPG Concentration: {:.2f} ppm'.format(lpg_conc))
        print('CO2 Concentration: {:.2f} ppm'.format(co2_conc))
        print('Smoke Concentration: {:.2f} ppm'.format(smoke_conc))
        print('Average LPG Concentration: {:.2f} ppm'.format(average_lpg))
        print('Average CO2 Concentration: {:.2f} ppm'.format(average_co2))
        print('Average Smoke Concentration: {:.2f} ppm'.format(average_smoke))
        print('\n')
        time.sleep(2)
        file.close()
        
        #Light code
        value = str(GPIO.input(readPIN))
        conv = int(value)
        if(conv == 1): 
          light_counter += 1
          print(light_counter)
          log_value = '1'
        else:
          log_value = '0'
        file = open("light_log.txt", "a")
        file.write(log_value + " " + tstamp + "\n")
        time.sleep(2)
        file.close()
        
        #motion code 
        if pir.motion_detected:
            motion_counter += 1
            print("YES")
            with open("motion_log.txt", "a") as file:
                file.write(plot + " " + tstamp + "\n")
                time.sleep(2)
        else:
            print("NO")
            with open("motion_log.txt", "a") as file:
                file.write(zero + " " + tstamp + "\n")
                time.sleep(2)
        file.close()
        
#       temp/humid code
        try:
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))
            temp = str(temperature_c) 
            humid = str(humidity)
            conv_temp = float(temp) 
            conv_humid = float(humid) 
            file = open("temp-humid_log.txt", "a") 
            file.write(temp + " ")
            file.write(humid + " ")
            sum_temp = sum_temp + conv_temp 
            sum_humid = sum_humid + conv_humid
            th_counter += 1
            average_temp = sum_temp/th_counter 
            average_humid = sum_humid/th_counter
            print("Average Temperature={0:0.1f}C Average Humidity={1:0.1f}%".format(average_temp, average_humid))
            now = (datetime.now())
            tstamp = "{0:%H}{0:%M}{0:%S}".format(now)
            file.write(tstamp + "\n")

        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        file.close()
        time.sleep(2)
        
#         check to see if box is opened
        state_ls = GPIO.input(22)
        if state_ls == GPIO.LOW:
            limit_switch += 1
            print(limit_switch)


#         tim = time.localtime()
#         current_time = time.strftime("%I:%M %p", tim)
#         lcd.close(clear=True)
#         lcd.write_string("Current Time")
#         lcd.crlf()
#         lcd.write_string(current_time)
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
            firebase = pyrebase.initialize_app(firebaseConfig)
            GPIO.setup(24, GPIO.OUT)
            GPIO.output(24, GPIO.HIGH)
            
            print("WORKING")
            now = datetime.now()
            month = now.strftime("%m")
            day = now.strftime("%d")
            year = now.strftime("%Y")
            
#           gas graph
            data = np.loadtxt('gas_log.txt')
            now = (datetime.now())
            tstamp = "{0:%Y},{0:%m},{0:%d}".format(now)
            storage = firebase.storage()
            x = []
            for timestamp in data[:, 3]:
                time_str = str(int(timestamp))
                formatted_time_str = ':'.join([time_str[i:i+2] for i in range(0, len(time_str), 2)])
                x.append(formatted_time_str)
            y1 = data[:, 0]
            y2 = data[:, 1]
            y3 = data[:, 2]
            plt.title('Gas Graph for ' + tstamp)
            plt.ylabel('Concentration (ppm)')
            plt.xlabel('Time')
            plt.plot(x, y1, 'r--')
            plt.plot(x, y2, 'r--')
            plt.plot(x, y3, 'r--')
            plt.xticks(rotation=45, ha='right')
            plt.gcf().set_size_inches(19.20, 10.80)
            plt.savefig(tstamp + '_gas.png', dpi=100)
            gas_name = tstamp + '_gas.png'
            storage.child(gas_name).put(gas_name)           
            gas_url = storage.child(gas_name).get_url(None)
            print("Image sent")
            print(gas_url)
            plt.clf()
#           temp graph
            data = np.loadtxt('temp-humid_log.txt')
            now = (datetime.now())
            tstamp = "{0:%Y},{0:%m},{0:%d}".format(now)

            a = []
            for timestamp in data[:, 2]:
                time_str = str(int(timestamp))
                formatted_time_str = ':'.join([time_str[i:i+2] for i in range(0, len(time_str), 2)])
                a.append(formatted_time_str)
            b = data[:, 0]
            plt.title('Temperature Graph for ' + tstamp)
            plt.ylabel('Temperature (deg C)')
            plt.xlabel('Time')
            plt.plot(a, b, 'r--')
            plt.xticks(rotation=45, ha='right')
            plt.gcf().set_size_inches(19.20, 10.80)
            plt.savefig(tstamp + '_temp.png', dpi=100)
            temp_name = tstamp + '_temp.png'
            storage.child(temp_name).put(temp_name)           
            temp_url = storage.child(temp_name).get_url(None)
            print("Image sent")
            print(temp_url)
            plt.clf()
#           humid graph
            data = np.loadtxt('temp-humid_log.txt')
            now = (datetime.now())
            tstamp = "{0:%Y},{0:%m},{0:%d}".format(now)

            c = []
            for timestamp in data[:, 2]:
                time_str = str(int(timestamp))
                formatted_time_str = ':'.join([time_str[i:i+2] for i in range(0, len(time_str), 2)])
                c.append(formatted_time_str)
            d = data[:, 1]
            plt.title('Humidity Graph for ' + tstamp)
            plt.ylabel('Humidity (%)')
            plt.xlabel('Time')
            plt.plot(c, d, 'r--')
            plt.xticks(rotation=45, ha='right')
            plt.gcf().set_size_inches(19.20, 10.80)
            plt.savefig(tstamp + '_humid.png', dpi=100)
            humid_name = tstamp + '_humid.png'
            storage.child(humid_name).put(humid_name)           
            humid_url = storage.child(humid_name).get_url(None)
            print("Image sent")
            print(humid_url)
            plt.clf()
#			light graph
            data = np.loadtxt('light_log.txt')
            now = (datetime.now())
            tstamp = "{0:%Y},{0:%m},{0:%d}".format(now)

            e = []
            for timestamp in data[:, 1]:
                time_str = str(int(timestamp))
                formatted_time_str = ':'.join([time_str[i:i+2] for i in range(0, len(time_str), 2)])
                e.append(formatted_time_str)
            f = data[:, 0]
            plt.title('Light Graph for ' + tstamp)
            plt.ylabel('Light Threshold')
            plt.xlabel('Time')
            plt.plot(e, f, 'r--')
            plt.xticks(rotation=45, ha='right')
            plt.gcf().set_size_inches(19.20, 10.80)
            plt.savefig(tstamp + '_light.png', dpi=100)
            light_name = tstamp + '_light.png'
            storage.child(light_name).put(light_name)           
            light_url = storage.child(light_name).get_url(None)
            print("Image sent")
            print(light_url)
            plt.clf()
#			motion graph
            g = []
            for timestamp in data[:, 1]:
                time_str = str(int(timestamp))
                formatted_time_str = ':'.join([time_str[i:i+2] for i in range(0, len(time_str), 2)])
                g.append(formatted_time_str)
            h = data[:, 0]
            plt.title('Motion Graph for ' + tstamp)
            plt.ylabel('Movement')
            plt.xlabel('Time')
            plt.plot(g, h, 'r--')
            plt.xticks(rotation=45, ha='right')
            plt.gcf().set_size_inches(19.20, 10.80)
            plt.savefig(tstamp + '_motion.png', dpi=100)
            motion_name = tstamp + '_motion.png'
            storage.child(motion_name).put(motion_name)           
            motion_url = storage.child(motion_name).get_url(None)
            print("Image sent")
            print(motion_url)
            plt.clf()
            data = {'Gas graph': gas_url, 'Temperature graph': temp_url,'Humidity graph': humid_url, 'Light graph': light_url, 'Motion graph': motion_url, 'Limit Switch': limit_switch, 'Day': day, 'Month': month, 'Year': year, 'Current Time': current_time,'Movements': motion_counter, 'Average Temperature': average_temp, 'Average humidity': average_humid, 'Light triggered': light_counter, 'LPG Concentration': average_lpg, 'CO2 Concentration': average_co2, 'Smoke Concentration': average_smoke, 'Alarm Time hour': hour, 'Alarm time minute': minute, 'Activity 1': activity1,'Activity 2': activity2, 'Activity 3': activity3}
            db.child("CurtisFicor").child(days[-2]).set(data)
            db.child("Users").child(days[-2]).set(data)
            time.sleep(5)
            beginMorning()
            
            
            
            break
            
            
# Activation of Speaker
            

        else:
            print("NOT WORKING. MONITOR YOUR SLEEP NOW. HASSAN THIS IS WHERE YOUR FUNCTION WILL GO")

        time.sleep(2)
      
    file.close()
    
    
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
        return hour
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
        return minute
    else:
        return minute        

