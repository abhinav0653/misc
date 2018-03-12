#!/usr/bin/python
from nltk.corpus import movie_reviews

#gather all documents from all movie categories as list
documents = [(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

#Get words along with their frequencies 
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
#Get 2000 most popular words as features
word_features = all_words.keys()[:2000]

#our feature is whether review contains most popular 2000 words
def document_features(document):
	document_words = set(document)
	features={}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

#training
featuresets = [(document_features(d),c) for (d,c) in documents]
train_set,test_set = featuresets[100:],featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier,test_set)

print classifier.show_most_informative_features(5)

