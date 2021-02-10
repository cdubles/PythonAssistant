import pyttsx3
import os
import speech_recognition as sr
import time
import  coreModules.timeModule as timeMod
engine = pyttsx3.init('sapi5')
r = sr.Recognizer()

def say(string):
        engine.say(string)
        engine.runAndWait()

while True:
    with sr.Microphone() as source:
        say("Say something!")
        audio = r.listen(source,timeout=5)
        print(audio)
        try:
            data = r.recognize_google(audio)
        except:
            say('bad audio')
            continue
        print(data)
        if "time" in data:
            say(timeMod.what_time())
        if 'year' in data:
            say(timeMod.what_year())
        if 'date' in data:
            say(timeMod.what_date())
        if 'close' in data:
            say("good bye")
            break