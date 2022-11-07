from lcdScreen import *

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time




activate_lcd_screen = False
count = 0
    
def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    
def switch(ev=None):
    global activate_lcd_screen, count
    activate_lcd_screen = not activate_lcd_screen
    count+= 1
    
    if activate_lcd_screen == True:
        print("Turning On\tcount: " + str(count))
        GPIO.output(26, GPIO.HIGH)
        run_screen()
    else:
        print("Turning Off\tcount: " + str(count))
        GPIO.output(26, GPIO.LOW)
        
    
def detectPhoneInBox():
    GPIO.add_event_detect(19, GPIO.FALLING, callback=switch, bouncetime=300)


def waitForEvents():
        while True:
            time.sleep(1)
