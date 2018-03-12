#!/usr/bin/python
from nltk.corpus import brown

#Training sentences from a tagged corpora named brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

#separating training and testing data
size = int(len(brown_tagged_sents)*0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

#Training a unigram tagger
unigram_tagger = nltk.UnigramTagger(train_sents)
#evaluating above tagged on same sentence
print unigram_tagger.evaluate(test_sents)
