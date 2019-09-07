#!/usr/bin/python3

import speech_recognition as sr

AUDIO_FILE = ("Song.wav")     # The audio file to use

r = sr.Recognizer()           # Create an object for the library

with sr.AudioFile(AUDIO_FILE) as source:       # Open the audio file as source
    audio = r.record(source)                   # Take in and record the audio file
    
try :
    print("The audio file contains the following contents")
    print("\""+r.recognize_google(audio)+"\"")                    # Print the text as in the audio file

except sr.UnknownValueError :           # Exception UnknownValueError i.e file not proper
    print("Audio file is improper")
except sr.RequestError :                # Exception while making request to server
    print("Can't supply request to Google")