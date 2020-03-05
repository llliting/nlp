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
    if(type(text) is str):
        text = removePunc(text)
        counter = 0
        freqDic = {}
        for word in word_tokenize(text):
            if not word in stop_words:
                word = wnl.lemmatize(word)
                word = ps.stem(word)
                freqDic[word.lower()] += 1
                counter += 1
        for key in freqDic:
            freqDic[key] = freqDic[key]/float(counter)
    return freqDic, counter 


#compute term frequency in an article: 
def computeTF(wordDict, articleStr):
    tfDict = {}
    bagOfWordsCount = len(articleStr)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
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
    #dist = FreqDist()
    
    
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
            text = preprocess(article.text)
            articleList += [text]
        except Exception:
            continue
        num += 1
        
    
    
    tf = []
    for article in articleList:
        text = removePunc(article)
        tf += freqDic(text)
        
    idfDict = computeIDF(tf)
    computeTFIDF(tf,idfDict)
        
main()

    #tfidf



'''
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
'''
    #vectorizer = TfidfVectorizer()
    #ectors = vectorizer.fit_transform(articleList)
    
    
    '''
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(articleList)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
    df = df.transpose()
    print(df)
    '''
   # df.to_csv(r'tfidf.csv')

    
    #print(vectors)
    

                
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
       
    
