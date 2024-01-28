from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
from tkinter import filedialog
import os
from pytube import YouTube
import time
program = Tk()
program.title("DVY")
program.geometry("300x300")
lblE = Label(program,text="enter the link of the video : ")
lblE.pack(pady=10)
ent = ttk.Entry(program)
ent.pack(pady=10)
lblQ = Label(program,text="enter the qualite of the video : ")
lblQ.pack(pady=10)
entQ = ttk.Entry(program)
entQ.pack(pady=10)
btn = ttk.Button(program,text="download")
btn.pack(pady=10)
lblT = Label(program,text="___")
lblT.pack(pady=20)
def choose():
	choose_folder = filedialog.askdirectory(title="select the folder")
	return choose_folder
def dvy():
    loc = fR'{choose()}'
    link = str(ent.get())
    qa = int(entQ.get())
    time.sleep(0.1)
    lblT.config(text="wait...")
    time.sleep(0.1)
    YouTube(link).streams[qa].download(loc)
    lblT.config(text="it's completed")
    tkinter.messagebox.showwarning(message="it's completed")
    os.startfile(R"C:\Users\Lenovo X240\Videos")
btn.config(command=dvy)
program.mainloop()
