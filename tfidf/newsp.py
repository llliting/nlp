from newspaper import Article
import nltk
import string
import re
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords 
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
import pandas as pd
import math

#from wsjsample.py import sentimentScore


#preprocess the text; remove the stopwords, punctuations;
#return a text string 
def preprocess(txt):
    wnl = nltk.WordNetLemmatizer()
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english')) 
    dt = TreebankWordDetokenizer()
    remove = string.punctuation
    remove = remove.replace("-", "") # don't remove hyphens
    pattern = r"[{}]".format(remove) # create the pattern
    txt = re.sub(pattern, "", txt)  
    words = []
    for word in word_tokenize(txt):
            if not word in stop_words:
                word = wnl.lemmatize(word)
                word = ps.stem(word)
                words += [word]
    dt.detokenize(words)
    return words


def removePunc(txt):
    remove = string.punctuation
    remove = remove.replace("-", "") # don't remove hyphens
    pattern = r"[{}]".format(remove) # create the pattern
    txt = re.sub(pattern, "", txt)    
    return txt


def freqDic(text):
    wnl = nltk.WordNetLemmatizer()
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english')) 
    text = removePunc(text)
    freqDic = FreqDist()
    for word in word_tokenize(text):
        if not word in stop_words:
            word = wnl.lemmatize(word)
            word = ps.stem(word)
            freqDic[word.lower()] += 1
    return freqDic  


#compute term frequency in an article: 
def computeTF(wordDict, articleStr):
    tfDict = {}
    wordCount = len(articleStr)
    for word, count in wordDict.items():
        tfDict[word] = count / float(wordCount)
    return tfDict


#The log of the number of documents divided by 
#the number of documents that contain the word w. 
#take in a list of dicts and return a idf dictionary 
def computeIDF(documents):
    N = len(documents)
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                if word not in idfDict:
                    idfDict[word] = 1
                else:
                    idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

#multiply TF and IDF 
def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

def main():
    fileName = "articles.txt"
    f = open(fileName,"r",encoding="utf-8" )
    urlList = f.readlines()
    articleList = []
    #extract articles from url
    num = 0
    for url in urlList:
        try:
            article = Article(url)
            article.download()
            article.parse()
            #print(article.authors)
            #text = preprocess(article.text)
            articleList += [article.text]
        except Exception:
            continue
        num += 1
    #compute TFIDF
    tf = []
    for article in articleList:
        if(type(article) is str):
            text = removePunc(article)
            tf += [computeTF(freqDic(text), text)]
    idfDict = computeIDF(tf)
    tfidfs = []
    for t in tf:
        tfidfs += [computeTFIDF(t,idfDict)]
    
    df = pd.DataFrame(tfidfs)  
    
    #print(df)
    #df = pd.DataFrame(tfidfs, columns=)
    df = df.transpose()
    #print(df)
    
    df.to_csv(r'tfidf.csv')
        
main()


