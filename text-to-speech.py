import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to speech")
root.geometry("900x450+100+100")
root.resizable(False, False)
root.configure(bg="#1662b4")

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

Label(root, text="Voice", font="arial 20 bold",
      bg="#1662b4", fg="white").place(x=580, y=160)
Label(root, text="Speed", font="arial 20 bold",
      bg="#1662b4", fg="white").place(x=760, y=160)

gender_combo = Combobox(
    root, values=["Male", "Female"], font="arial 14", state='r', width=10)
gender_combo.place(x=550, y=200)
gender_combo.set("Male")

speed_combo = Combobox(
    root, values=["Fast", "Normal", "Slow"], font="arial 14", state='r', width=10)
speed_combo.place(x=730, y=200)
speed_combo.set("Normal")

btn = Button(root, text="Speak", width=10,
             font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

save = Button(root, text="Save", width=10,
              font="arial 14 bold", command=download)
save.place(x=730, y=280)

root.mainloop()
