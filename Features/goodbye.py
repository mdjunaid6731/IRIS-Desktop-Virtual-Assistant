from speak import speak
from takecommand import takeCommand


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()    

        if 'goodbye' in query:
            speak("See you next time, bye bye..")
            exit()