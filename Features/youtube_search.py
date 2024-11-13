from speak import speak
from takecommand import takeCommand
import pywhatkit as kt

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()    

        if "youtube" in query:
            query = query.replace("youtube","")
            speak("Searching in Youtube...")
            kt.playonyt(query)