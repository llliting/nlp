
import nltk
import re
import pandas as pd
import numpy as np
import os
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

#access the data
data = pd.read_csv("/Users/liting/Desktop/nlp/ProQuestDocuments-2019-11-01.csv")

#data = pd.read_csv("/cps/home/lhuang1/Desktop/nlp/ProQuestDocuments-2019-11-01.csv")
titles = data["Title"]
abstract = data["Abstract"]
wnl = nltk.WordNetLemmatizer()

#analyze the abstracts
fdist_abs = FreqDist()
for abst in abstract:
    if(type(abst) is str):
        abst = re.sub(r'[^\w\s]','',abst)
        for word in word_tokenize(abst):
            word = wnl.lemmatize(word)
            fdist_abs[word.lower()] += 1
print("frequent words in the abstracts: \n" , fdist_abs.most_common(100))


#analyze the titles
fdist_tit = FreqDist()
for title in titles:
    if(type(title) is str):
        title = re.sub(r'[^\w\s]','',title)
        for word in word_tokenize(title):
            word = wnl.lemmatize(word)
            fdist_tit[word.lower()] += 1
print("\n\nfrequent words in the titles: \n" , fdist_tit.most_common(100))

