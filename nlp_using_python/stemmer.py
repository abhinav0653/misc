#!/usr/bin/python
import nltk
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
tokens=[ 'ruthless','cars','paints']
print [porter.stem(t) for t in tokens]

