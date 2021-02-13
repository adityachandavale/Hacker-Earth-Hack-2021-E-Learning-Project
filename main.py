import sys
import os
import tkinter
from tkinter import messagebox as mb
from tkinter import *
top = tkinter.Tk()
top.geometry('500x400')
top.title('Smart Note Taker')
top.wm_iconbitmap('logo.ico')

canvas = tkinter.Canvas(top, width = 300, height = 300)
canvas.pack()
bottomcan = Canvas(top)
bottomcan.pack(side=BOTTOM)


def ocr():
    if os.system('python script.py') == True:
        mb.showinfo(top,'Image failed to process. Please try again.',parent=top)
    else:
        mb.showinfo(top,'The Keywords are stored in data.txt\nThank you for using this software')
    
def text():
    #if os.system('python nlp.py') == True:
    if os.system('python nlp.py') == True:
        mb.showinfo(top,'File failed to process. Please try again.')
    else:
        mb.showinfo(top,'The summary is stored in summary.txt\nThank you for using this software')
        
def diction():
    if os.system('python dictionary.py') == True:
        mb.showinfo(top,'Please try again.')
    else:
        mb.showinfo(top,'Hope you found what you were looking for.\nThank you for using this software')
    
def web_text():
    if os.system('python web_extract.py') == True:
        mb.showinfo(top,'File failed to process. Please try again.')
    else:
        mb.showinfo(top,'The summary is stored in web_summary.txt if you downloaded.\nThank you for using this software')
        
def audio():
    if os.system('python audio.py') == True:
        mb.showinfo(top,'File failed to process. Please try again.')
    else:
        mb.showinfo(top,'Thank you for using this software')
    
def close_window(): 
    top.destroy()
    
def on_closing():
    if mb.askokcancel("Quit", "Do you want to quit?"):
        top.destroy()

top.protocol("WM_DELETE_WINDOW", on_closing)

w = tkinter.Label(canvas, text="Welcome to Smart Note Taker.\nPlease select any one of following Buttons.\n\n\n")
w.pack(side=TOP)
#canvas.create_text(10,150,fill="darkblue",font="Times 10 italic bold",text="Welcome to Smart Note Taker. Please select any one of following Buttons.")
button = tkinter.Button(bottomcan, text = "close", command = close_window)
b = tkinter.Button(canvas,text='Image',command = ocr,padx=10,pady=10,width=20)
c = tkinter.Button(canvas,text='Summary Generator',command = text,padx=10,pady=10,width=20)
d = tkinter.Button(canvas,text='Web Article Summary',command = web_text,padx=10,pady=10,width=20)
e = tkinter.Button(canvas,text='Dictionary',command = diction,padx=10,pady=10,width=20)
f = tkinter.Button(canvas,text='Audio transcribe',command = audio,padx=10,pady=10,width=20)

b.pack(side=TOP)
c.pack(side=TOP)
d.pack(side=TOP)
e.pack(side=TOP)
f.pack(side=TOP)
button.pack(side=TOP)

top.mainloop()