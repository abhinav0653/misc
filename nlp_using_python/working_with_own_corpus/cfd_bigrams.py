#!/usr/bin/python
text=ptb.words(["hate1.txt","hate2.txt"])
bigrams=nltk.bigrams(text)
cfd=nltk.ConditionalFreqDist(bigrams)
print list(cfd["bad"])
