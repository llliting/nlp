#Liting Huang

import nltk
import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords 

stop_words = set(stopwords.words('english')) 


data = pd.read_csv("/Users/liting/Desktop/nlp/WSJSample.csv",encoding='ISO-8859-1')
titles = data['Title']
abstract = data['Abstract']
year = data['year']
date = data['entryDate']
startPage = data['startPage']

wnl = nltk.WordNetLemmatizer()
allowed_word_types = ["J","R","V","N"]

#print(titles)
#analyze the abstracts
abst_list = []
print("\n\n\n ==============ABSTRACTS===============")
fdist_abs = FreqDist()
for abst in abstract:
    if(type(abst) is str):
        abst = re.sub(r'[^\w\s]','',abst)
        abst = re.sub(r'Ê', '', abst)
        for word in word_tokenize(abst):
            if not word in stop_words:
                abst_list += [word]
                word = wnl.lemmatize(word)
                fdist_abs[word.lower()] += 1
pos_abs = nltk.pos_tag(abst_list)
trueWords = []
for pos in pos_abs:
    if pos[1][0] in allowed_word_types:
        trueWords.append(pos[0].lower())
print("most frequent words in the abstracts: \n" , fdist_abs.most_common(100))
print(" \n\n\n\nleast common words in the abstracts: \n", fdist_abs.most_common()[-100:])
print("\n\n\nplot top 30 words: ", FreqDist(dict(fdist_abs.most_common(30))).plot() )

print("\n\n\nmost frequent words in the abstracts (j/r/v/n): \n" , FreqDist(trueWords).most_common(100))
print("\n\n\n plot: ", FreqDist(dict(FreqDist(trueWords).most_common(30))).plot())





print("\n\n\n ==============TITLES===============")
#analyze the titles
fdist_tit = FreqDist()
title_list = []
for title in titles:
    if(type(title) is str):
        title = re.sub(r'[^\w\s]','',title) #remove punctuations
        for word in word_tokenize(title):
            if not word in stop_words:
                title_list += [word]
                word = wnl.lemmatize(word)
                fdist_tit[word.lower()] += 1
pos_title = nltk.pos_tag(title_list)

print("\n\nmost frequent words in the titles: \n" , fdist_tit.most_common(100))
print(" \n\n\n\nleast common words in the title: \n", fdist_tit.most_common()[-100:])
print("\n\n\nplot top 30 words: ", FreqDist(dict(fdist_tit.most_common(30))).plot() )


