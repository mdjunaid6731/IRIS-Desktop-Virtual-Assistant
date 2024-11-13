import pyttsx3

engine = pyttsx3.init('sapi5') #takes voice form computer
voices = engine.getProperty("voices")
engine.setProperty('rate',180) #speaking speed(default 200)

# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Initializing Desktop Virtual Assistant.....")
