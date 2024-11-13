from speak import speak
from takecommand import takeCommand
import pygame
import random
import os

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
    while True:
        query = takeCommand().lower()    
        
        # Logic for executing tasks based on query
        if 'play music' in query:
            play_song(current_song_index)

        elif 'pause music' in query:
            pause_song()

        elif 'resume music' in query:
            resume_song()
        
        elif 'next' in query:
            play_next()

        elif 'previous' in query:
            play_previous()