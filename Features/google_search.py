from speak import speak
from takecommand import takeCommand
import pywhatkit as kt

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()    

        if "search" in query:
            query = query.replace("search","")
            speak("searching in google...")
            kt.search(query) 