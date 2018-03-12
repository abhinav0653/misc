#!/usr/bin/python

words = ptb.words(fileids=["hate1.txt"])
anagrams = nltk.defaultdict(list)
for word in words:
	key = ''.join(sorted(word))
	anagrams[key].append(word)

print anagrams['aeilnrt']

last_letters = nltk.defaultdict(list)
words = ptb.words(fileids=["hate1.txt"])
for word in words:
	key = word[-2:]
	last_letters[key].append(word)

print last_letters['ad']
