#!/usr/bin/python

#defining features for learning
#the following function returns a dictionary value lastletter:w
def gender_features(word):
	return{'last_letter':word[-1]}

#create training data by shuffling male and female names
from nltk.corpus import names
import random
names = ([(name,'male') for name in names.words('male.txt')]+ [(name,'female') for name in names.words('female.txt')])
random.shuffle(names)

#Training the classifier
featuresets = [(gender_features(n),g) for (n,g) in names]
train_set,test_set = featuresets[500:],featuresets[:500]
classifier= nltk.NaiveBayesClassifier.train(train_set)

#Trying our classifier
print classifier.classify(gender_features('Neo'))
print classifier.classify(gender_features('Trinity'))

#evaluating classifier on tagged test_set
print nltk.classify.accuracy(classifier,test_set)

# Print most informative features. In naive bayes these will be those which have most probability in decreasing order
print classifier.show_most_informative_features(5)

#classifier2
classifier= nltk.DecisionTreeClassifier.train(train_set)
print nltk.classify.accuracy(classifier,test_set)


#checking for errors. To be debugged
"""
errors=[]
for (name,tag) in test_set:
	guess = classifier.classify(gender_features(name))
	if guess != tag:
		errors.append((tag,guess,name))
for (tag,guess,name) in sorted(errors):
	print 'correct-%-8s guess=%-8s name=%-30s' %(tag,guess,name)
"""
