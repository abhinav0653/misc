#!/usr/bin/python
print motorcar.hypernyms()
paths = motorcar.hypernym_paths()
print len(paths)
print [synset.name() for synset in paths[0]]
print motorcar.root_hypernyms()
