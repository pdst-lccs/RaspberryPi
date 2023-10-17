# see: https://pyttsx3.readthedocs.io/en/latest/engine.html
import sys

tts = pyttsx3.init()  # Initialize the TTS engine.

tts.say("Warning! Warning! Intruder alert.")
tts.runAndWait()  # Make the TTS engine say it

