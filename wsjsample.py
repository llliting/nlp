#Liting Huang

import nltk
import re
import string
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords 

def removePunc(txt):
    remove = string.punctuation
    remove = remove.replace("-", "") # don't remove hyphens
    pattern = r"[{}]".format(remove) # create the pattern
    txt = re.sub(pattern, "", txt)    
    return txt
    #remove += "--"
    #text = re.sub(r'[^\w\s]','',text)

def freqDic(wordList, freqDic):
    for entry in wordList:
        if(type(entry) is str):
            text = entry[entry.find('--')+2:]
            text = removePunc(text)
            for word in word_tokenize(text):
                if not word in stop_words:
                    word = wnl.lemmatize(word)
                    #abst_list += [word]
                    freqDic[word.lower()] += 1
     





stop_words = set(stopwords.words('english')) 
wnl = nltk.WordNetLemmatizer()
allowed_word_types = ["J","R","V","N"]

#read data
data = pd.read_csv("/Users/liting/Desktop/nlp/WSJSample.csv",encoding='ISO-8859-1')
titles = data['Title']
abstract = data['Abstract']
year = data['year']
date = data['entryDate']
startPage = data['startPage']



#analyze the abstracts
print("\n\n\n ==============ABSTRACTS===============")
fdist_abs = FreqDist()
abst_list = []
freqDic(abstract, fdist_abs)
print("most frequent words in the abstracts: \n" , fdist_abs.most_common(100))
print(" \n\n\n\nleast common words in the abstracts: \n", fdist_abs.most_common()[-100:])
print("\n\n\nplot top 30 words: ", FreqDist(dict(fdist_abs.most_common(30))).plot() )           

                
#anaylze the titles
print("\n\n\n ==============TITLES===============")
#analyze the titles
fdist_tit = FreqDist()
title_list = []
freqDic(titles, fdist_tit)
print("most frequent words in the titles: \n" , fdist_tit.most_common(100))
print(" \n\n\n\nleast common words in the titles: \n", fdist_tit.most_common()[-100:])


'''
pos_abs = nltk.pos_tag(abst_list)
trueWords = []
for pos in pos_abs:
    if pos[1][0] in allowed_word_types:
        trueWords.append(pos[0].lower())


print("\n\n\nmost frequent words in the abstracts (j/r/v/n): \n" , FreqDist(trueWords).most_common(100))
print("\n\n\n plot: ", FreqDist(dict(FreqDist(trueWords).most_common(30))).plot())





pr
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

'''
