import nltk
import re
import string
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer 



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
