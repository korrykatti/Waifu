import os
import time
import pyaudio
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en-in")
    filename = "welcome.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    vocbrain = sr.Recognizer()
    with sr.Microphone as source:
        audio = vocbrain.listen(source)
        said = ""


        try:
            said = vocbrain.recognize_google(audio)
            print(said)        
        except Exception as e:
            


speak("a quick brown fox jumped over a lazy dog")


