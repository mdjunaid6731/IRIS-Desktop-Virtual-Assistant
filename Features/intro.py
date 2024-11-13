import speak
import takecommand

if __name__ == "__main__":
    while True:
        query = takecommand.takeCommand().lower()    
        
        # Logic for executing tasks based on query
        if 'introduce yourself' in query:
            speak.speak("Hello User")
            intro="I am IRIS, Desktop Virtual Assistant . I can help you in doing your tasks in computer and increse your productivity, like -  I can open programs and applications for you , play music or do any google search"
            print(intro)
            speak.speak(intro)
