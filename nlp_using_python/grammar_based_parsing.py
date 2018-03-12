#!/usr/bin/python
from nltk import CFG,DependencyGrammar
groucho_grammar = CFG.fromstring(""" 
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I' 
VP -> V NP | VP PP 
Det -> 'an' | 'my' 
N -> 'elephant' | 'pajamas' 
V -> 'shot' 
P -> 'in' 
""")

sent = ['I','shot','an','elephant','in','my','pajamas']
parser = nltk.ChartParser(groucho_grammar)
trees = parser.parse(sent)
for tree in trees:
	print tree

groucho_dep_grammar = DependencyGrammar.fromstring("""
'shot' -> 'I' | 'elephant' | 'in'
'elephant' -> 'an' | 'in'
'in' -> 'pajamas'
'pajamas' -> 'my'
""")

print groucho_dep_grammar
pdp = nltk.ProjectiveDependencyParser(groucho_dep_grammar)
sent = 'I shot an elephant in my pajamas'.split()
trees = pdp.parse(sent)
for tree in trees:
	print tree
