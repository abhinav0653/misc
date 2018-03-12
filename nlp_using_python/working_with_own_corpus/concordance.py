#!/usr/bin/python
import nltk
text = nltk.Text(word.lower() for word in ptb.words(fileids=["hate1.txt"]))
print text.similar("bad")
print text.concordance("bad")
