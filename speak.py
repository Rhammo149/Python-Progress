import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("Whats this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()

