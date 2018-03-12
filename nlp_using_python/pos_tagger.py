#!/usr/bin/python
import nltk
text = nltk.word_tokenize("And now for something completely different")
print nltk.pos_tag(text)
text = nltk.word_tokenize("They refuse to permit us to obtain refuse permit")
print nltk.pos_tag(text)


