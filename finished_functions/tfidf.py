



#compute term frequency in an article: 
def computeTF(wordDict, articleStr):
    tfDict = {}
    wordCount = len(articleStr)
    for word, count in wordDict.items():
        tfDict[word] = count / float(wordCount)
    return tfDict


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


def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf