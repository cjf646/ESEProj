from welcome import *
from activitiesAlarmSetup import *
from lcdScreen import *
from doActivities import *
from sleep import *
from morning import *

from picamera import PiCamera
from time import sleep
import datetime


from datetime import datetime
from picamera import PiCamera
from time import sleep
import os

import pyrebase


if __name__ == '__main__':

    setupGPIO()
    detectPhoneInBox()
    waitForEvents()
