from speak import speak
from takecommand import takeCommand
import datetime

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()    

        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

