import nltk
from nltk.corpus.reader import CHILDESCorpusReader

corpus_root = nltk.data.find('corpora/childes/data-xml/Eng-UK-MOR/')

belfast = CHILDESCorpusReader(corpus_root, 'Belfast/.*.xml')
cruttenden = CHILDESCorpusReader(corpus_root, 'Cruttenden/.*.xml')
manchester = CHILDESCorpusReader(corpus_root, 'Manchester/.*.xml')
tommerdahl = CHILDESCorpusReader(corpus_root, 'Tommerdahl/.*.xml')


print(len(belfast.fileids()))
print(len(cruttenden.fileids()))
print(len(manchester.fileids()))
print(len(tommerdahl.fileids()))