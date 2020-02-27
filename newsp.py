from newspaper import Article
import nltk
import string
import re
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords 
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import math

#from wsjsample.py import sentimentScore

def removePunc(txt):
    remove = string.punctuation
    remove = remove.replace("-", "") # don't remove hyphens
    pattern = r"[{}]".format(remove) # create the pattern
    txt = re.sub(pattern, "", txt)    
    return txt

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

def computeIDF(documents):
    N = len(documents)
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

def main():
    fileName = "/Users/liting/Desktop/nlp/articles.txt"
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
            articleList += [article.text]
        except Exception:
            continue
        num += 1
        
    dist = FreqDist()
    stop_words = set(stopwords.words('english')) 
    wnl = nltk.WordNetLemmatizer()
    ps = PorterStemmer()


    #tfidf
    uniquewords = set(word_tokenize(articleList[0]))
    for t in articleList:      
        t = removePunc(t)
        uniquewords = uniquewords.union(set(word_tokenize(t)))
        
    numWords = []
    tfList = []
    for t in articleList:
        numOfWords = dict.fromkeys(uniquewords, 0)
        for word in word_tokenize(t):
            numOfWords[word] += 1
        numWords += [numOfWords]
        tfList += [computeTF(numOfWords, word_tokenize(t))]
    
    idfs = computeIDF(numWords)
    idfList = []
    for i in range (len(tfList)):
        idfList += [computeTFIDF(tfList[i], idfs)]
    
    print("idfs" + idfs)
    df = pd.DataFrame(idfList)
    print("df\n" + df)
    print(uniquewords)
    print(num)
    
main()
    

                
'''          
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(articleList)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
'''

        
    
'''
    #calculate wordfrequency
    for t in articleList:      
        t = removePunc(t)
        for word in word_tokenize(t):
            if not word in stop_words:
                word = wnl.lemmatize(word)
                word = ps.stem(word)
                dist[word.lower()] += 1
'''
       
    
