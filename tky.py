#importing numpy and pandas to store, manipulate and process data
import pandas as pd
import numpy as np
#importing regular expressions librarires for pre- processing 
import re, string, unicodedata
#importing these libraries for pre-processing purposes
#use pip install contractions to install them
import contractions
import inflect
#importing bs4 to identify and remove web-tags
from bs4 import BeautifulSoup
#nltk is used for natural language processing
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
#importing pre-processing libraries from keras
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
#importing keras to access machine learning model
from keras.models import Sequential
#importing keras for defining neutral netwrok
from keras.layers.core import Activation, Dropout, Dense
from keras.layers import Flatten, LSTM
from keras.layers import GlobalMaxPooling1D
from keras.layers.embeddings import Embedding
#importing sklearn 
from sklearn.model_selection import train_test_split
import keras
from scipy.stats import gamma 
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')




from tensorflow import keras
model = keras.models.load_model('D:\School')
a= input("enter the sentence")
stop_words= stopwords.words('english')


def pre_pro(text):
  
  #print(text)
  
  
#HTML tags were found in the text so Bs4 was used to strip them to get better sentiments as HTML tags are <br> doesnt help in sentiment analysis
  def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


#removing the square brackets as it increase inconsistencies in pre-processing
  def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)



  def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    return text


#we have to remove contraction to get clear idea of the text. like 'you'll' will get converted into 'you will'
  def replace_contractions(text):
    """Replace contractions in string of text"""
    return contractions.fix(text)    


  #removing indentified general pattern names starting with @ and #tags. when we scrap a data from the web it may contain symbols like '@' and '%' which do not tell us about the setiments of the sentences .Thus they are removed. 
  text=" ".join (word for word in text.split() if word[0] not in ['@', '#'])
  
  #denoise
  text=denoise_text(text)

  #removing stop words. stop wods are words like 'and' , 'if' etc which do not have any role in setimental analysis hence they are removed.
  text=" ".join (word for word in text.split() if word not in stop_words)

  #removing line skip. replaces the unneeded elements by blankspace
  text=text.replace('[^\w\s]','')
  
  # Remove punctuations and numbers. punctuation like !, ? and numbers are not used in sentimental analysis 
  text = re.sub('[^a-zA-Z]', ' ', text)

  #lowercase. Changing into lower case for uniform datastructure
  text=" ".join (word.lower() for word in text.split())
 
 #contraction.
  text=replace_contractions(text)

  # Single character removal
  text = re.sub(r"\s+[a-zA-Z]\s+", ' ', text)

  # Removing multiple spaces
  text = re.sub(r'\s+', ' ', text)
  

  
  return text
  
a=pre_pro(a)
x=model.predict_classes([a])[0]
from tkinter import *
z=Tk()
####FRAME 1
frame=LabelFrame(z)
frame.pack(side="top",expand=True,fill="both")
frame.configure(bg="lavender")
dest=Button(frame,text="EXIT",font=("impact"),fg="royal blue",bg="lavender",command=z.destroy)
dest.place(relx=0.5,rely=1.0,anchor="s")
frameser=LabelFrame(frame)
search=Entry(frameser,width=20,font=("century gothic",25),fg="grey")
search.insert(0,"Search")
senti=search.get()"
def btsent():
    return
e=Entry(frame,width=20,font=("century gothic",25),fg="grey")
searchb=Button(frameser,text="SEARCH",fg="royal blue",bg="lavender",font="impact")
frameser.pack()
e.pack()
search.grid(row=1,column=2)
searchb.grid(row=1,column=3)
z.mainloop()""""