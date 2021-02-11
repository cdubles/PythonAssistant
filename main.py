import pyttsx3 as tts
import os
import speech_recognition as sr
import time
import json
import  coreModules.timeModule as timeMod

engine = tts.init('sapi5')
r = sr.Recognizer()

wakeWord = "test"
voice = "female"
speechRate = 300
volume = .5
with open('config.json') as config_file:
    data = json.load(config_file)
    print(data)
    wakeWord = data["wakeWord"]
    voice = data["voice"]
    speechRate = data["speechRate"]
    volume = data["volume"]

engine.setProperty('voice', voice)
engine.setProperty('rate', speechRate)
engine.setProperty('volume', volume)
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