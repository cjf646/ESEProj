# Import LCD library
from RPLCD import i2c

# Import sleep library
from time import sleep
from activitiesAlarmSetup import *

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# indicator of when the next activity is selected
next_activity = 0
# select_button = False
activity_added = 0
# constants to initialise the LCD


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
def run_screen():
    global next_activity
    next_activity = 0
    lcd.close(clear=True)
    lcd.write_string('Select activities!!')
    lcd.crlf()
    lcd.write_string('')
    lcd.crlf()

    lcd.write_string('Get 5 hours of sun')
#     switch2()
    detectNextActivityPress()
    detectActivitySelect()
    
#     detectActivitySelect()
#     lcd.backlight_enabled = False
#     # Clear the LCD screen
#     lcd.close(clear=True)
def changeActivity():
    GPIO.remove_event_detect(13)
    if next_activity == 1:
        lcd.close(clear=True)
        lcd.write_string('Next one!')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Journal for 3 hours')
        
        detectNextActivityPress()
        detectActivitySelect()
        
#         detectActivitySelect()
        
        
#         sleep(5)
#     # Switch off backlight
#         lcd.backlight_enabled = False
#     # Clear the LCD screen
#         lcd.close(clear=True)
    if next_activity == 2:
        lcd.close(clear=True)
        lcd.write_string('Next one!')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('1000 pushups')
#         GPIO.remove_event_detect(13)
        detectNextActivityPress()
        detectActivitySelect()
        
#         detectActivitySelect()
        
    if next_activity == 3:
        lcd.close(clear=True)
        lcd.write_string('Next one!')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Take a shit')
#         GPIO.remove_event_detect(13)
        detectNextActivityPress()
        detectActivitySelect()
        
        
    if next_activity == 4 and activity_added == 0:
        lcd.close(clear=True)
        lcd.write_string('Select ATLEAST one!')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('')
        sleep(4)
        run_screen()
        
#         GPIO.remove_event_detect(13)
#         detectActivitySelect()
        
        
    # Switch off backlight
#         lcd.backlight_enabled = False
#     # Clear the LCD screen
#         lcd.close(clear=True)

def addActivity():
    if activity_added == 1 and next_activity == 0:
        store = 'Get 5 minutes of sun'
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('SELECTED')
        lcd.crlf()
        lcd.write_string('')
    if activity_added == 2 and next_activity == 1:
        store = 'Journal for 5 minutes'
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('SELECTED')
        lcd.crlf()
        lcd.write_string('')
    if activity_added == 3 and next_activity == 2:
        store = '10 pushups'
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('SELECTED')
        lcd.crlf()
        lcd.write_string('')
    if activity_added == 3 and next_activity == 2:
        store = 'Drink glass of water'
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('SELECTED')
        lcd.crlf()
        lcd.write_string('')
def switch2(ev=None):
    next_button = False
#     global next_button, count2
    global next_activity
    next_button = not next_button
    next_activity += 1
    print(next_activity)
    
    if next_button == True:
        changeActivity()
        sleep(2)
#             lcd.write_string('Next one!')
#             lcd.crlf()
#             lcd.write_string('')
#             lcd.crlf()
#             lcd.write_string('Journal for 5 minutes')
#         else:
#             print("Turning Off\tcount: " + str(count))
#             GPIO.output(26, GPIO.LOW)




def switch3(ev=None):
    select_button = False
#     global select_button, activity
    global activity_added
    select_button = not select_button
    activity_added += 1
    print("activity added!!")
    
    if select_button == True:
        addActivity()
        sleep(2)
        
        
def detectNextActivityPress():
    GPIO.remove_event_detect(13)
    GPIO.add_event_detect(13, GPIO.FALLING, callback=switch2, bouncetime=300)
    

def detectActivitySelect():
    GPIO.remove_event_detect(6)
    GPIO.add_event_detect(6, GPIO.FALLING, callback=switch3, bouncetime=300)
#     lcd.write_string('Phppot')
#     sleep(5)
    # Switch off backlight
#     lcd.backlight_enabled = False
    # Clear the LCD screen
#     lcd.close(clear=True)
def waitForEvents():
        while True:
            sleep(1)