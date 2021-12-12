import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en-in")
    filename = "welcome.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get

speak("a quick brown fox jumped over a lazy dog")


