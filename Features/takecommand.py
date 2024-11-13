import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5') #takes voice form computer
voices = engine.getProperty("voices")
engine.setProperty('rate',180) #speaking speed(default 200)

# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# It takes audio from microphone and retunrs string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
            
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
        except Exception as e:
                print("Say that again please....")
                return "None"
    return query

if __name__ == "__main__":
    speak("Hello, this is sample voice from computer")
    takeCommand()