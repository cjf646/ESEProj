from welcome import *
from activitiesAlarmSetup import *
from lcdScreen import *

from picamera import PiCamera
from time import sleep

# added for camera
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
from datetime import datetime
from picamera import PiCamera
from time import sleep
import os

import pyrebase


if __name__ == '__main__':

#      GPIO.setup(19, GPIO.OUT)
#      GPIO.output(19, GPIO.HIGH)

#      time.sleep(3)
#      GPIO.output(19, GPIO.LOW)
#      GPIO.cleanup()


#     firebaseConfig = {
#   'apiKey': "AIzaSyBPmuCMq_v2euR4n4qW1hBnosQuBTgtW5k",
#   'authDomain': "habits-b5b42.firebaseapp.com",
#   'databaseURL': "https://habits-b5b42-default-rtdb.firebaseio.com",
#   'projectId': "habits-b5b42",
#   'storageBucket': "habits-b5b42.appspot.com",
#   'messagingSenderId': "134941482333",
#   'appId': "1:134941482333:web:b8acc728562e6ad8789cb4",
#   'measurementId': "G-YWS3LCTD6E"
# }
#
#     firebase = pyrebase.initialize_app(firebaseConfig)
#
#     storage = firebase.storage()
#
#     camera = PiCamera()
#
#     while True:
#       try:
#         if GPIO.input(19) == GPIO.LOW:
#             print("pushed")
#             now = datetime.now()
#             dt = now.strftime("%d%m%Y%H:%M:%S")
#             name = dt+".jpg"
#             camera.capture(name)
#             print(name+" saved")
#             storage.child(name).put(name)
#             print("Image sent")
#             os.remove(name)
#             print("File Removed")
#             sleep(2)
#
#
#       except:
#             camera.close()
#





#     camera = PiCamera()
#     camera.start_preview()
#     sleep(30)
#     camera.stop_preview()

# lock box code running
    setupGPIO()
    detectPhoneInBox()
    waitForEvents()




#     superhero_name, name = deviceSetUp()

#     print(superhero_name)
#     print(name)
#
#
#     storeName(superhero_name, name)
