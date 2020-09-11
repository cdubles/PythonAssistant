import pyttsx3
import os
import speech_recognition as sr
from time import ctime
engine = pyttsx3.init()

def say(string):
    engine.say(string)
    engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    say("Say something!")
    audio = r.listen(source)
    data = r.recognize_google(audio)
    print(data)
if "time" in data:
    say(ctime())
