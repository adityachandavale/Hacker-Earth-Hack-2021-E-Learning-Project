import tkinter
from tkinter import messagebox as mb
from tkinter import *
top = tkinter.Tk()
import urllib3
import html2text
http = urllib3.PoolManager()
from bs4 import BeautifulSoup
import requests
import io
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
stopword = stopwords.words('english')
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer('english')
from nltk import FreqDist
import heapq

canvas1 = tkinter.Canvas(top, width = 300, height = 300)
canvas1.pack()

top.geometry('500x400')
top.title('Webpage Summary Generator')
top.wm_iconbitmap('logo.ico')

e = Entry(top)
e.pack()
e.focus_set()

def printtext():
    global e
    string = e.get()
    return string

def web():
    s = printtext()
    page = requests.get(s).text
    soup = BeautifulSoup(page,'lxml')
    text = soup.find_all(text=True)
    output = ''
    blacklist = [
        '[document]',

       'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
    ]
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
       

    tokenizer = nltk.RegexpTokenizer(r"\w+")
    new_words = tokenizer.tokenize(output)

    lower_text = output.lower()

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|'''
    no_punct = ""
    for char in lower_text:
        if char not in punctuations:
            no_punct = no_punct + char

    word_tokens = nltk.word_tokenize(no_punct)

    removing_stopwords = [word for word in word_tokens if word not in stopword]

    lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in removing_stopwords]

    freq = FreqDist(lemmatized_word)

    summary_sentences = heapq.nlargest(1, freq, key=freq.get)

    keyword = ' '.join([str(elem) for elem in summary_sentences]) 

    txt = [sentence + '.' for sentence in output.split('.') if keyword in sentence]

    with open('web_summary.txt', 'w', encoding="utf-8") as f:
        for item in txt:
            f.write("%s\n" % item)

b = tkinter.Button(canvas1,text='Download',command = web,padx=10,pady=20,width=10)
b.pack(side=LEFT)

top.mainloop()