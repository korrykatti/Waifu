import os
import random
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
        print(f"User said {said}\n")
    except Exception as e:
        print(e) 
        print("Error")
        return "None"
    return said


greetings = ['I just woke up how are you today ?', 'I had a pretty nice sleep hope you also had same', 'What a lovely day ', 'My bed is very comfortable but i will get up for u ']

speak(random.choice(greetings))


words = get_audio()

if "hello" or "hi" in words:
    hielloreply = ['Hello how are you today', 'Hello There Its Fun To Be With you again' , 'Hi', 'Hello']
    speak(random.choice(hielloreply))


