import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

from firebase import firebase
import pyttsx3
import time
import pyrebase

#date module
import datetime

from welcome import *
from activitiesAlarmSetup import *
from lcdScreen import *
from doActivities import *
from sleep import *

# def speech(text):
#     print(text)
#     language = "en"
#     output = gTTS(text = text, lang=language, slow=False)
#
#     output.save("/home/cjf646/Desktop/ESE_Final_Project/output.mp3")
#     playsound('/home/cjf646/Desktop/ESE_Final_Project/output.mp3')
#

def listening():

    print("Listening...")
    listening = True
    while listening:
    #keyword = "activate"
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            recognizer.adjust_for_ambient_noise(source)
            recognizer.dynamic_energy_threshold = 2500


            try:

                print("Listening...")
                audio = recognizer.listen(source, timeout=5.0)
                superhero_name = recognizer.recognize_google(audio)
#                 time.sleep(2)
#                 speech("hello how is it going")
                return superhero_name
#                 if len(superhero_name.split()) < 3:
#                     return superhero_name
#
            except sr.UnknownValueError:
                print("Didn't recognize that.")

def gratitudeVoiceDeviceInteraction():
    print("hello")
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[32].id)

    engine.say("Hi, I am your superhero coach")
    engine.runAndWait()
    time.sleep(1)
    engine.say("Please say one thing you are grateful for before you go to sleep! ok go")
    engine.runAndWait()
    gratitude_text = listening()
    substring = "I am grateful"
    if substring in gratitude_text:

        engine.say("Did you say:" + gratitude_text)
        engine.runAndWait()
        yes_or_no = listening()
        yes = "yes"
        if yes in yes_or_no:
            engine.say("Yes you are very grateful for that. Have a great sleep!")
            engine.runAndWait()
#             Going to sleep
#             clock()



#     time.sleep(1)
#     engine.say("Is this what you said?")
#     time.sleep(1)
#     engine.say(gratitude_text)
#     engine.runAndWait()
#


    time.sleep(1)
#     engine.say("What would you like to call me?")
#     engine.runAndWait()
#     set_superhero_name = listening()
#
#     time.sleep(1)
#     engine.say(set_superhero_name + "at your service!!!")
#     engine.runAndWait()
#
#
#     return set_superhero_name, your_name




# welcoming code

# def listening():
#
#     print("Listening...")
#     listening = True
#     while listening:
#     #keyword = "activate"
#         with sr.Microphone() as source:
#             recognizer = sr.Recognizer()
#             recognizer.adjust_for_ambient_noise(source)
#             recognizer.dynamic_energy_threshold = 3000
#
#
#             try:
#
#                 print("Listening...")
#                 audio = recognizer.listen(source, timeout=5.0)
#                 superhero_name = recognizer.recognize_google(audio)
#
#                 if len(superhero_name.split()) < 3:
#                     return superhero_name
#
#             except sr.UnknownValueError:
#                 print("Didn't recognize that.")
#
#
# def deviceSetUp():
#     print("hello")
#     engine = pyttsx3.init()
#     voice = engine.getProperty('voices')
#     engine.setProperty('voice', voice[32].id)
#
#     engine.say("Hi, I am your superhero coach")
#     engine.runAndWait()
#     time.sleep(1)
#     engine.say("What is your name?")
#     engine.runAndWait()
#     your_name = listening()
#
#     time.sleep(1)
#     engine.say("Nice to meet you" + your_name)
#     engine.runAndWait()
#
#
#
#     time.sleep(1)
#     engine.say("What would you like to call me?")
#     engine.runAndWait()
#     set_superhero_name = listening()
#
#     time.sleep(1)
#     engine.say(set_superhero_name + "at your service!!!")
#     engine.runAndWait()
#
#
#     return set_superhero_name, your_name
#
#
#
#
# def storeName(superhero_name, name):
#
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
#     firebase = pyrebase.initialize_app(firebaseConfig)
#     db = firebase.database()
#
#     #date and time
#     date = datetime.date.today()
#     d = date.strftime("%B %d, %Y")
#
#     tim = time.localtime()
#     current_time = time.strftime("%I:%M %p", tim)
#
#
#
#     data = {'Date': d, 'Time': current_time}
# #     FBConn = firebase.FirebaseApplication('https://habits-b5b42-default-rtdb.firebaseio.com', None)
#     db.child("Users").child(name).child(superhero_name).set(data)
#
