import sys
sys.path.append('/usr/share/thonny')
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


from picamera import PiCamera
import time
import datetime


from datetime import datetime
from picamera import PiCamera
from time import sleep
import os

import pyrebase

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# GPIO.setup(19, GPIO.IN)
# import sys
# # sys.path.append('/usr/share/thonny')
# from activitiesAlarmSetup import *
# from lcdScreen import *
# from doActivities import *
# from sleep import *
# from morning import *
# from recognizeFeelings import *
# from parentVerification import *
# from boxStart import *
# from streak import *
# 
# 
# from picamera import PiCamera
# import time
# import datetime
# 
# 
# from datetime import datetime
# from picamera import PiCamera
# from time import sleep
# import os
# 
# import pyrebase
# 
# import RPi.GPIO as GPIO
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# # GPIO.setup(19, GPIO.IN)
# # GPIO.setup(22, GPIO.IN)
# 
# # Import LCD library
# from RPLCD import i2c
# 
# lcdmode = 'i2c'
# cols = 20
# rows = 4
# charmap = 'A00'
# i2c_expander = 'PCF8574'
# 
# # Generally 27 is the address;Find yours using: i2cdetect -y 1
# address = 0x27
# port = 1 # 0 on an older Raspberry Pi
# 
# # Initialise the LCD
# lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
#                   cols=cols, rows=rows)
# 
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# 
# 
# if __name__ == '__main__':
# 
#     setupGPIO()
# 
#     boxRun()
#     lockOn()            
#     waitForEvents()
# 
#  

import os
import sys

# Specify absolute paths to all dependencies
dependencies = [
    '/home/cjf646/Desktop/ESE_Final_Project/activitiesAlarmSetup.py',
    '/home/cjf646/Desktop/ESE_Final_Project/path/to/lcdScreen.py',
    '/home/cjf646/Desktop/ESE_Final_Project/path/to/doActivities.py',
    '/home/cjf646/Desktop/ESE_Final_Project/path/to/sleep.py',
    '/home/cjf646/Desktop/ESE_Final_Project/path/to/morning.py',
    '/home/cjf646/Desktop/ESE_Final_Project/path/to/recognizeFeelings.py',
    '/home/cjf646/Desktop/ESE_Final_Project/path/to/parentVerification.py',
    '/home/cjf646/Desktop/ESE_Final_Project/path/to/boxStart.py',
    '/home/cjf646/Desktop/ESE_Final_Project/path/to/streak.py',
]

# Add all dependency paths to sys.path
for dependency in dependencies:
    sys.path.append(dependency)

# Import necessary modules
from activitiesAlarmSetup import *
from lcdScreen import *
from doActivities import *
from sleep import *
from morning import *
from recognizeFeelings import *
from parentVerification import *
from boxStart import *
from streak import *

from picamera import PiCamera
import time
from datetime import datetime

import pyrebase

import RPi.GPIO as GPIO
from RPLCD import i2c

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# GPIO.setup(19, GPIO.IN)
# GPIO.setup(22, GPIO.IN)

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

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

import subprocess
import psutil
import os
time.sleep(3)



# time.sleep(3)
# # Define the name of the program that you want to kill
# PROGRAM_NAME = "/home/cjf646/Desktop/ESE_Final_Project/main.py"
# 
# # Get a list of all running processes
# processes = psutil.process_iter()
# 
# # Iterate through the list of running processes
# for process in processes:
#     try:
#         # Get the name of the process
#         process_name = process.name()
# 
#         # If the name of the process matches the name of the program you want to kill,
#         # terminate the process
#         if process_name == PROGRAM_NAME:
#             process.terminate()
#             print("Terminated previous instance of {}".format(PROGRAM_NAME))
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         pass
# 
# # Start a new instance of the program
# os.system("python {}".format(PROGRAM_NAME))
# 
if __name__ == '__main__':
    
    
    setupGPIO()
    boxRun()
    lockOn()            
    waitForEvents()
    

