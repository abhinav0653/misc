#!/usr/bin/python
cfd=nltk.ConditionalFreqDist((fileid,word) for fileid in ptb.fileids()  for word in ptb.words(fileids="hate1.txt"))
cfd.plot()
