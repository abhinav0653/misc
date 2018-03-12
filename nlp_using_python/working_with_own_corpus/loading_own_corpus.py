#!/usr/bin/python
from nltk.corpus import PlaintextCorpusReader
corpus_root = './mycorpus'
file_pattern = r".*"
ptb= PlaintextCorpusReader(corpus_root,file_pattern)
print ptb.fileids()
