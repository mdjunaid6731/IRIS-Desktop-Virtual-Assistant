import pyttsx3
import datetime


engine = pyttsx3.init('sapi5') #takes voice form computer
voices = engine.getProperty("voices")
engine.setProperty('rate',180) #speaking speed(default 200)

# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish according to the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("My name is IRIS, How may i help you")

if __name__ == "__main__":
    wishMe()
