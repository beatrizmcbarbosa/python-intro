import cowsay
import pyttsx3


# Initialise pyttsx3 library
engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
