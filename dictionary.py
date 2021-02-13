from PyDictionary import PyDictionary
dictionary=PyDictionary()
import tkinter
from tkinter import *
top = tkinter.Tk()

canvas1 = tkinter.Canvas(top, width = 300, height = 300)
canvas1.pack()

top.geometry('500x400')
top.title('Dictionary')
top.wm_iconbitmap('logo.ico')


e = Entry(top)
e.pack()
e.focus_set()

def printtext():
    global e
    string = e.get()
    return string


def w_meaning():
    strg = printtext()
    w = tkinter.Label(canvas1, text=dictionary.meaning(strg))
    w.pack(side=BOTTOM)

def w_synonym():
    strg = printtext()
    w = tkinter.Label(canvas1, text=dictionary.synonym(strg))
    w.pack()
        
def w_antonym():
    strg = printtext()
    w = tkinter.Label(canvas1, text=dictionary.antonym(strg))
    w.pack()

                    
b = tkinter.Button(canvas1,text='Meaning',command = w_meaning,padx=10,pady=20,width=10)
b.pack()
c = tkinter.Button(canvas1,text='Synonym',command = w_synonym,padx=10,pady=20,width=10)
c.pack()
d = tkinter.Button(canvas1,text='Antonym',command = w_antonym,padx=10,pady=20,width=10)
d.pack()


top.mainloop()