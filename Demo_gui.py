import tkinter as tk
from tkinter import scrolledtext
from tkinter import *
from PIL import Image, ImageTk  # Import Pillow modules
import main

# Initialize the main window
root = tk.Tk()
root.title("IRIS | Desktop Virtual Assistant")
root.geometry("1800x1200")
root.config(bg="#EBD38F")  # Light yellow background

# Header with icon and title
header_frame = tk.Frame(root, bg="#EBD38F", height=200)
header_frame.pack(fill="x", pady=10)

# Load and resize the image using PIL (Pillow)
logo_image = Image.open("logo.png")  # Replace with your image file path
logo_image = logo_image.resize((300, 300))  # Resize the image to the desired width and height

# Convert the resized image to a format Tkinter can use
logo_photo = ImageTk.PhotoImage(logo_image)

# Create a label with the resized image logo
icon_label = tk.Label(header_frame, image=logo_photo, bg="#EBD38F")
icon_label.pack(side="left", padx=50, pady=20)

# Add some text next to the logo (optional)
header_label = tk.Label(header_frame, text="IRIS | Desktop Virtual Assistant", font=("Arial", 34), bg="#EBD38F")
header_label.pack(side="left", padx=10, pady=1)

# Divider line
divider = tk.Frame(root, bg="gray", height=3)
divider.pack(fill="x", pady=5)

# Chat history frame
chat_history_frame = tk.Frame(root, bg="#EBD38F")
chat_history_frame.pack(fill="both",  padx=20, pady=10)

# Chat history text area (scrolledtext)
chat_history = scrolledtext.ScrolledText(chat_history_frame, wrap="word", width=60, height=15, font=("Arial", 12))
chat_history.pack(side="left", fill="both", expand=True, padx=10, pady=5)
chat_history.insert("end", "Hello, this is your Virtual Assistant! \nHow can I assist you today?")  # Initial text
chat_history.config(state="disabled")  # Disable editing

# Map or additional section (right side)
map_placeholder = tk.Label(
    chat_history_frame, 
    text="""IRIS can perform the following tasks:
- Play music
- Search Wikipedia for information
- Provide live news headlines
- Open Programs/Browser
- Open Applications
- Perform Google and YouTube searches
- Respond to voice commands""", 
    bg="#F0F0F0", 
    font=("Arial", 12), 
    width=40, 
    height=15, 
    anchor="w",  # Align text to the left inside the label
    justify="left"  # Left justify the text within the label
)
map_placeholder.pack(side="right", padx=10, pady=5)

# Divider line
divider = tk.Frame(root, bg="gray", height=2)
divider.pack(fill="x", pady=5)

# Chat input frame
input_frame = tk.Frame(root, bg="#EBD38F")
input_frame.pack(fill="x", padx=20, pady=10)


# Load and resize the microphone icon
mic_icon = Image.open("mic.png")  
mic_icon = mic_icon.resize((100, 100))  
mic_photo = ImageTk.PhotoImage(mic_icon)

# Create a button with the resized microphone icon
mic_button = tk.Button(input_frame, image=mic_photo, bg="#FFFFFF", relief="flat")
mic_button.pack(side="top", padx=5, pady=10)


# Input field
input_field = tk.Entry(input_frame, font=("Arial", 14), width=75)
input_field.pack(side="left", padx=10)
input_field.insert(0, "Type your task here....")

# Submit button
submit_button = tk.Button(input_frame, text="Submit", font=("Arial", 14))
submit_button.pack(side="right", padx=5)



# Function to handle sending messages (you can add more functionality here)
def send_message(event=None):
    message = input_field.get()
    if message.strip():
        chat_history.config(state="normal")
        chat_history.insert("end", "You: " + message + "\n")
        chat_history.insert("end", "AI: This is a response from the AI.\n\n")  # Placeholder response
        chat_history.config(state="disabled")
        chat_history.yview("end")  # Scroll to the bottom
        input_field.delete(0, "end")

# Bind Enter key to send message
input_field.bind("<Return>", send_message)


# Run the application
root.mainloop()