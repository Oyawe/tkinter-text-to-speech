import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from gtts import gTTS
# from gtts import gTTS
import os

root = Tk()
root.title("Text to speech")
root.geometry("900x450+100+100")
root.resizable(False, False)
root.configure(bg="#1662b4")


def speaknow():
    text = text_area.get(1.0, END)

    if text:
        tts = gTTS(text)
        tts.save("output.mp3")  # Save the text as an MP3 file

        # Use macOS's built-in "afplay" command to play the MP3 file
        os.system("afplay output.mp3")


# icon
image_icon = PhotoImage(file="speak.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="speaker-logo.png")
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)

Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold",
      bg="white", fg="black").place(x=100, y=30)

text_area = Text(root, font="arial 20", bg="white",
                 fg="black", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

btn = Button(root, text="Speak", width=20,
             font="arial 14 bold", command=speaknow)
btn.place(x=600, y=250)

root.mainloop()
