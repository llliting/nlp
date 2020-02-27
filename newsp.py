from newspaper import Article
import nltk
import string
import re
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords 
#from wsjsample.py import sentimentScore

fileName = "/Users/liting/Desktop/nlp/articles.txt"

f = open(fileName,"r",encoding="utf-8" )

urlList = f.readlines()
articleList = []

def removePunc(txt):
    remove = string.punctuation
    remove = remove.replace("-", "") # don't remove hyphens
    pattern = r"[{}]".format(remove) # create the pattern
    txt = re.sub(pattern, "", txt)    
    return txt


for url in urlList:
    try:
        article = Article(url)
        article.download()
        article.parse()
        #print(article.authors)
        articleList += [article.text]
    except Exception:
        continue
    

dist = FreqDist()
stop_words = set(stopwords.words('english')) 
wnl = nltk.WordNetLemmatizer()
ps = PorterStemmer()


for t in articleList:      
    t = removePunc(t)
    for word in word_tokenize(t):
        if not word in stop_words:
            word = wnl.lemmatize(word)
            word = ps.stem(word)
            dist[word.lower()] += 1
    
    
    
   

