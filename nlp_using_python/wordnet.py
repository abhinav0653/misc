#!/usr/bin/python
from nltk.corpus import wordnet as wn
print wn.synsets('motorcar')
print wn.synset('car.n.01').lemma_names()
print wn.synset('car.n.01').definition()
print wn.synset('car.n.01').examples()
