from nltk.corpus.reader import reviews
import numpy as np
import matplotlib.pyplot as plt
import sys

from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


tokenizer = RegexpTokenizer(r'\w+')
on_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()


def getCleanReview(review):
    
    review = review.lower()
    review = review.replace("<br /><br />"," ")
    
    #Tokenize 
    tokens = tokenizer.tokenize(review)
    new_tokens = [token for token in tokens if token not in on_stopwords]
    stemmed_tokens = [ps.stem(token) for token in new_tokens]
    
    cleaned_review = ' '.join(stemmed_tokens)
    return cleaned_review


def getStemedDocument(inputfile,ouputfile):

    out = open(ouputfile,'w',encoding='utf8')

    with open(inputfile, encoding="utf8") as f:
        reviews = f.readlines()

    for review in reviews:
        cleaned_review = getCleanReview(review)
        print((cleaned_review),file=out)
        
    out.close()


# Read Command line arguments

# inputFile = sys.argv[1]
# outputFile = sys.argv[2]

# getStemedDocument(inputFile,outputFile)