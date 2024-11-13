import speech_recognition as sr  # for speech recognition
import webbrowser  #for controlling the webbrowsers
import pyttsx3  # voice module for Computer speaking
import datetime
import wikipedia #wikipedia search 
import os
import random
import Links_list # Module to exract links and paths
import requests
import pywhatkit as kt #for google and youtube Searche
import pygame #for music control


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

# Initialize the mixer
pygame.mixer.init()

music_dir = 'C:\\Users\\mdjun\\Music'
songs = os.listdir(music_dir)
random_num = random.randint(0, len(songs)-1)
current_song_index = random_num

# load and play a song
def play_song(index):
    song_path = os.path.join(music_dir, songs[current_song_index])
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    print(f"Playing: {songs[current_song_index]}")


# play the next song
def play_next():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)  # Loop to first song after the last
    play_song(current_song_index)
    


# play the previous song
def play_previous():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)  # Loop to last song if at the first
    play_song(current_song_index)

# pause the song
def pause_song():
    pygame.mixer.music.pause()
    print("Music paused")

# resume the song
def resume_song():
    pygame.mixer.music.unpause()
    print("Music resumed")

if __name__ == "__main__":
    speak("Initializing Desktop Virtual Assistant.....")
    wishMe()
    while True:
        query = takeCommand().lower()    
        
        # Logic for executing tasks based on query
        if 'introduce yourself' in query:
            speak("Hello User")
            intro="I am IRIS, Desktop Virtual Assistant . I can help you in doing your tasks in computer and increse your productivity, like -  I can open programs and applications for you , play music or do any google search"
            print(intro)
            speak(intro)

        elif 'wikipedia'  in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'play music' in query:
            play_song(current_song_index)

        elif 'pause music' in query:
            pause_song()

        elif 'resume music' in query:
            resume_song()
        
        elif 'next' in query:
            play_next()

        elif 'previous' in query:
            play_previous()


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open' in query:
            try:
                list = query.split(" ", 1)[1]  # Split on the first space only
                if list in Links_list.browserApp:
                    link = Links_list.browserApp[list]
                    webbrowser.open(link)
                else:
                    path = Links_list.App[list]
                    os.startfile(path)
            except Exception as e:
                print("Please specify what you want to open.")

        elif 'news' in query:
            newsapi = "e557adbb3a0e4ad7b4e4a5d7049aa9da"
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
                # Parse the JSON response
                data = r.json()

                # Extract the articles
                articles = data.get('articles', [])

                #print the headlines
                for article in articles:
                    print(article['title'])
                    speak(article['title'])

        elif "search" in query:
            query = query.replace("search","")
            speak("searching in google...")
            kt.search(query)

        elif "youtube" in query:
            query = query.replace("youtube","")
            speak("Searching in Youtube...")
            kt.playonyt(query)
        
        elif 'goodbye' in query:
            speak("See you next time, bye bye")
            exit()




           
        
        

        

        




        