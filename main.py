import pyttsx3 as tts
import os
import speech_recognition as sr
import time
import json
from coreModules import *
engine = tts.init()
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
    print(wakeWord)

def say(string):
    engine.setProperty('voice', voice)
    engine.setProperty('rate', speechRate)
    engine.setProperty('volume', volume)
    print(engine.getProperty('voice'))
    print(engine.getProperty('rate'))
    print(engine.getProperty('volume'))
    engine.say(string)
    engine.runAndWait()

def choose_command(data):
    if "time" in data:
        say(timeMod.what_time())
    if 'year' in data:
        say(timeMod.what_year())
    if 'date' in data:
        say(timeMod.what_date())
    if 'close' in data:
        say("good bye")
        exit()
while True:
    with sr.Microphone() as source:
        audio = r.listen(source,timeout=2)
       #print(audio)
        try:
            data = r.recognize_google(audio).lower()
           #data = str(input('command'))
        except:
            continue
            print('bad audio')
        print(data)
        if wakeWord in data:
            say('listening')
            command_audio = r.listen(source, timeout=0)
            command_data = r.recognize_google(command_audio).lower()
            print("command data: "+command_data)
            choose_command(command_data)
        else:
            print("no wake word")
