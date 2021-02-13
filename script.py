from PIL import Image
import pytesseract
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
#top = tk.Tk()
import cv2
from nltk import tokenize
from operator import itemgetter
import math 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from PyDictionary import PyDictionary
dictionary=PyDictionary()
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import csv

root = tk.Tk()
root.withdraw()
#root.deiconify()
root.lift()
root.focus_force()

#import import_lib
#import nlp
#import ocr

class main_class:
    path = filedialog.askopenfilename(parent=root)
    word_list = []

    #print("Welcome to smart note taker.\nThis application helps you to take notes in a smarter way.")
    #print('Your file path selected is:',path)

class ocr:
    ob = main_class()
    img = cv2.imread(ob.path)
    str = None
    path = None

    def __init__(self):
        self.preprocess()
        self.convert()
        self.store_to_text()

    def preprocess(self):
        gray_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        self.img = threshold_img
        #cv2.imshow('preprocessed', self.img)
        #cv2.waitKey(0)
        #fig = plt.figure()
        #plt.suptitle('Image')
        #ax = fig.add_subplot(1, 2, 1)
        #plt.imshow(self.img, cmap = plt.cm.gray)
        #plt.axis("off")

    def convert(self):
        self.str = pytesseract.image_to_string(self.img)
    
    def store_to_text(self):
        txtfile=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
        self.path=txtfile
        #txtfile = open('data.txt','w')
        txtfile.write(self.str)
        txtfile.close()
        
class execute:
    ob = ocr()