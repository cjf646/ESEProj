# Import LCD library
from RPLCD import i2c

# Import sleep library
from time import sleep
from welcome import *
from activitiesAlarmSetup import *
from lcdScreen import *
from doActivities import *
from sleep import *

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# indicator of when the next activity is selected
next_activity = 0
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

activity1 = 'Get 5 hours of sun'
activity2 = 'Journal for 5 mins'
activity3 = '10 pushups'
activity4 = 'Drink glass of water'

# Selecting activities
def run_screen(ev=None):
    global next_activity
    next_activity = 0
    lcd.close(clear=True)
    lcd.write_string('Select activities!!')
    lcd.crlf()
    lcd.write_string('')
    lcd.crlf()

    lcd.write_string(activity1)

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
        lcd.write_string(activity2)

        detectNextActivityPress()
        detectActivitySelect()

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
        lcd.write_string(activity3)

        detectNextActivityPress()
        detectActivitySelect()

    if next_activity == 3:
        lcd.close(clear=True)
        lcd.write_string('Next one!')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string(activity4)

        detectNextActivityPress()
        detectActivitySelect()

# if no activities are selected then return to selecting activites again.
    if next_activity == 4 and activity_added == 0:
        lcd.close(clear=True)
        lcd.write_string('Select ATLEAST one!')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('')
        sleep(3)
        run_screen()


# Display the activities list selected if all activities are viewed or if the activities added are equal to 3
    if next_activity >=4 or activity_added == 3:
        completeActivities(activities_list, activity_added, next_activity)


def addActivity():
    global activities_list
    if activity_added == 1 and next_activity == 0:
        lcd.close(clear=True)
        store_activity = activity1
        activities_list.append(store_activity)
        lcd.write_string(activity1)
        lcd.crlf()
        lcd.write_string('ADDED')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Press red button')
#         detectNextActivityPress()
#         detectActivitySelect()

    if activity_added == 1 and next_activity == 1:
        lcd.close(clear=True)
        store_activity = activity2
        activities_list.append(store_activity)
        lcd.write_string(activity2)
        lcd.crlf()
        lcd.write_string('ADDED')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Press red button ')
#         detectNextActivityPress()
#         detectActivitySelect()

    if activity_added == 1 and next_activity == 2:
        lcd.close(clear=True)
        store_activity = activity3
        activities_list.append(store_activity)
        lcd.write_string(activity3)
        lcd.crlf()
        lcd.write_string('ADDED')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Press red button ')
        detectNextActivityPress()
        detectActivitySelect()

    if activity_added == 1 and next_activity == 3:
        lcd.close(clear=True)
        store_activity = activity4
        activities_list.append(store_activity)
        lcd.write_string(activity4)
        lcd.crlf()
        lcd.write_string('ADDED')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Press red button ')
        detectNextActivityPress()
        detectActivitySelect()

    if activity_added == 2 and next_activity == 1:
        lcd.close(clear=True)
        store_activity = activity2
        activities_list.append(store_activity)
        lcd.write_string(activity2)
        lcd.crlf()
        lcd.write_string('ADDED')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Press red button ')
        detectNextActivityPress()
        detectActivitySelect()
        print("hello", activities_list)

    if activity_added == 2 and next_activity == 2:
        lcd.close(clear=True)
        store_activity = activity3
        activities_list.append(store_activity)
        lcd.write_string(activity3)
        lcd.crlf()
        lcd.write_string('ADDED')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Press red button ')
        detectNextActivityPress()
        detectActivitySelect()
        print("hello", activities_list)

    if activity_added == 2 and next_activity == 3:
        lcd.close(clear=True)
        store_activity = activity4
        activities_list.append(store_activity)
        lcd.write_string(activity4)
        lcd.crlf()
        lcd.write_string('ADDED')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Press red button ')
        detectNextActivityPress()
        detectActivitySelect()
        print("hello", activities_list)

    if activity_added == 3 and next_activity == 2:
        lcd.close(clear=True)
        store_activity = activity3
        activities_list.append(store_activity)
        lcd.write_string(activity3)
        lcd.crlf()
        lcd.write_string('ADDED')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Press red button ')
        detectNextActivityPress()
        detectActivitySelect()
        print("hello", activities_list)

    if activity_added == 3 and next_activity == 3:
        lcd.close(clear=True)
        store_activity = activity4
        activities_list.append(store_activity)
        lcd.write_string(activity4)
        lcd.crlf()
        lcd.write_string('ADDED')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Press red button ')
        detectNextActivityPress()
        detectActivitySelect()
        print("hello", activities_list)


    if activity_added == 4 and next_activity == 3:
        lcd.close(clear=True)
        store_activity = activity4
        activities_list.append(store_activity)
        lcd.write_string(activity4)
        lcd.crlf()
        lcd.write_string('ADDED')
        lcd.crlf()
        lcd.write_string('')
        lcd.crlf()
        lcd.write_string('Press red button ')
        detectNextActivityPress()
        detectActivitySelect()
        print("hello", activities_list)


def switch2(ev=None):
    next_button = False
#     global next_button, count2
    global next_activity
    next_button = not next_button
    next_activity += 1
    print(next_activity)

    if next_button == True:
        changeActivity()
        sleep(1)
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


    if select_button == True:
        activity_added += 1
        print("activities added =", activity_added)
        addActivity()
        sleep(1)


def detectNextActivityPress():
    GPIO.remove_event_detect(13)
    GPIO.add_event_detect(13, GPIO.FALLING, callback=switch2, bouncetime=300)


def detectActivitySelect():
    GPIO.remove_event_detect(6)
    GPIO.add_event_detect(6, GPIO.FALLING, callback=switch3, bouncetime=1500)
#     lcd.write_string('Phppot')
#     sleep(5)
    # Switch off backlight
#     lcd.backlight_enabled = False
    # Clear the LCD screen
#     lcd.close(clear=True)
def waitForEvents():
        while True:
            sleep(1)
