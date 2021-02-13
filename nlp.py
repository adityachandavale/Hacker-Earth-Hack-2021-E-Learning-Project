import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
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
import re
import io

root = tk.Tk()
root.withdraw()
#root.deiconify()
root.lift()
root.focus_force()

class nlp:
    txtfile = open('data.txt','r')
    p = txtfile.read()
    #ob.word_list = p
    dw ={}

    def __init__(self):
        self.nlp()

    def nlp(self):
        
        path = filedialog.askopenfilename(parent=root)

        with io.open(path,"r", encoding="utf-8") as f:
            text = f.read()
        f.close()

        tokenizer = nltk.RegexpTokenizer(r"\w+")
        new_words = tokenizer.tokenize(text)

        lower_text = text.lower()

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

        #print(keyword)
        txt = [sentence + '.' for sentence in text.split('.') if keyword in sentence]

        with open('summary.txt', 'w', encoding="utf-8") as f:
            for item in txt:
                f.write("%s\n" % item)
                
class exec:
    a = nlp()