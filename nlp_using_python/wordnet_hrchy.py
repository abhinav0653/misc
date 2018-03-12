#!/usr/bin/python
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
print types_of_motorcar[26]
x=[lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()]
print sorted(x)
