from welcome import *
from displayStreak import *
from activitiesAlarmSetup import *
from lcdScreen import *




if __name__ == '__main__':
    
#      GPIO.setup(19, GPIO.OUT)
#      GPIO.output(19, GPIO.HIGH)
     
#      time.sleep(3)
#      GPIO.output(19, GPIO.LOW)
#      GPIO.cleanup()

    
    

    
    setupGPIO()
    detectPhoneInBox()  
    waitForEvents()
    
    
    
    

#     superhero_name, name = deviceSetUp()
    
#     print(superhero_name)
#     print(name)
# 
#     
#     storeName(superhero_name, name)