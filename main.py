import pyttsx3
import os
import speech_recognition as sr
import time
engine = pyttsx3.init('sapi5')

def say(string):
        engine.say(string)
        engine.runAndWait()

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        say("Say something!")
        audio = r.listen(source)
        data = r.recognize_google(audio)
        print(data)
    if "time" in data:
        say(time.strftime('%c'))
