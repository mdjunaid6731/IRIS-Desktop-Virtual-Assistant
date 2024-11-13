from speak import speak
from takecommand import takeCommand
import webbrowser

if __name__ == "__main__":
    speak()
    while True:
        query = takeCommand().lower()    

        if "open google" in query:
            webbrowser.open("https://www.google.com/")

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com/")

        elif "open maps" in query:
            webbrowser.open("https://www.google.com/maps")
        
        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/")
        
        elif "open chat gpt" in query:
            webbrowser.open("https://chatgpt.com/")

        elif "open stack overflow" in query:
            webbrowser.open("https://stackoverflow.com/")

        elif "open github" in query:
            webbrowser.open("https://github.com/")

        elif "open data analysis course" in query:
            webbrowser.open("https://www.coursera.org/learn/data-analysis-with-python/home/module/1")