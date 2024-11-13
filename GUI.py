from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from PIL import Image,ImageTk
import pyttsx3 # voice module for  speaking
import speech_recognition as sr 
import datetime 
import os 
import pywhatkit as kt #for google Searches
import webbrowser
import wikipedia 
import pygame
import Links_list
import requests
import random
import sys

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

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        usertext.delete(0,ttk.END)
        usertext.insert(0, str(query))
    except Exception as e:
        print(e)
        query = usertext.get()
        
    
    query = str(query).lower()
    
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
    
    bodyText.insert(0,sys.stdout)
    bodyText.insert(ttk.END,sys.stderr)
    


root = ttk.Window(themename="morph")
root.geometry("1450x820")
root.title("IRIS DESKTOP VIRTUAL ASSISTANT")

frame1 = ttk.Frame(master=root,bootstyle=PRIMARY)
frame1.pack(padx=40,pady=40)

ttk.Separator(bootstyle=INFO).pack(fill='x',padx=50)

frame2 = ttk.Frame(master=root,bootstyle="primary")
frame2.pack(padx=40,pady=40)

ttk.Separator(bootstyle=INFO).pack(fill='x',padx=50)

userLabel = ttk.LabelFrame(master=root,text="User Commands",bootstyle=INFO)
userLabel.pack(pady=(40,10))

frame3= ttk.Frame(master=userLabel,bootstyle="primary")
frame3.pack(padx=10,pady=10)


#frame1
img = Image.open("logo.png")

aiImage = ImageTk.PhotoImage(img.resize((150,150)))
aiLabel = ttk.Label(master=frame1,image=aiImage,width=50)
aiLabel.grid(row=0,rowspan=2,column=0,padx=10,pady=(10,10))


aiTextFrame = ttk.LabelFrame(master=frame1,text=" IRIS AI Says : ",bootstyle=INFO)
aiTextFrame.grid(row=0,column=1,rowspan=2,padx=10)

aitext = ttk.Entry(aiTextFrame,bootstyle="success",width=70)
aitext.insert(0,"Hi! How can I help you today?")
aitext.pack(padx=10,pady=10)

#frame2

bodyFrame = ttk.LabelFrame(master=frame2,text="Body Text",bootstyle=INFO)
bodyFrame.pack()
bodyText = ttk.Text(bodyFrame,height=5,width=100,foreground="blue")
bodyText.pack(padx=20,pady=20)


# frame3


usertext = ttk.Entry(master=frame3,bootstyle="success",width=85)
usertext.insert(0,"Your Spoken Commands here!")
usertext.grid(row=0,column=0,padx=10,pady=10)

button = ttk.Button(master=frame3,bootstyle=(DANGER,OUTLINE),text="Take Command",command=takeCommand)
button.grid(row=0,column=1,padx=10,pady=10)


wishMe()
root.mainloop()

   