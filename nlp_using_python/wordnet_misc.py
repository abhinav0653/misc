#!/usr/bin/python
print wn.synset('tree.n.01').part_meronyms()
print wn.synset('tree.n.01').substance_meronyms()
print wn.synset('tree.n.01').member_holonyms()

for synset in wn.synsets('min',wn.NOUN):
	print synset.name() + ':' , synset.definition()

print wn.synset('walk.v.01').entailments()

#semantic similarity
right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')
print right.lowest_common_hypernyms(orca)
print wn.synset('baleen_whale.n.01').min_depth()
print right.path_similarity(minke)
print right.path_similarity(orca)
