import wikipedia
from speak import speak
from takecommand import takeCommand


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()    
        if 'wikipedia'  in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)