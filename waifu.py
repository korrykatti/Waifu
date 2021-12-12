import os
import time
import wave
import pyaudio
import playsound
import speech_recognition as sr
from gtts import gTTS


FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "x.wav"

def speak(text):
    tts = gTTS(text=text, lang="en-in")
    filename = "welcome.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    file = open("microphone-results.wav", "w")
    os.remove('microphone-results.wav')
    
    r = sr.Recognizer()
    with sr.Microphone(sample_rate = 48000) as source:
        print("Now Listening")
        audio = r.record(source, duration = 5)
    with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
            r.pause_threshold = 1
    with sr.AudioFile("microphone-results.wav") as source:
            audio = r.listen(source)

    try:
        said = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")
    except Exception as e:
        print(e) 
        print("Error")
        return "None"
    return query


speak("")
get_audio()


