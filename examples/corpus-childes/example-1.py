import os
import nltk
import numpy as np
import pandas as pd

## comment if you don't have the pretty package
#from pretty import pprint
from nltk.corpus.reader import CHILDESCorpusReader


def main():
    nltk_download_dir = '/home/rodriguesfas/nltk_data'

    brown_corpus_root = os.path.join(nltk_download_dir, 'corpora/CHILDES/Eng-NA-MOR/Valian/')
    brown_corpus = CHILDESCorpusReader(root=brown_corpus_root, fileids='.+xml')
    
    print brown_corpus.fileids()[:5]

    fileids = ['02b.xml', '03a.xml']

    print brown_corpus.age(fileids=fileids)
    print brown_corpus.MLU(fileids=fileids)

    print {fid: brown_corpus.age(fileids=fid)[0] for fid in fileids}
    print {fid: brown_corpus.MLU(fileids=fid)[0] for fid in fileids}

    print {fid: brown_corpus.age(fileids=fid, month=True)[0] for fid in fileids}

    metadata = brown_corpus.participants(fileids='03a.xml')[0]

    ## comment this if you don't have the pretty package
    print(metadata)

    ## uncomment this if you don't have the pretty package
    #print metadata

    print 'words:', brown_corpus.words(fileids='03a.xml')[:7]
    print 'sents:', brown_corpus.sents(fileids='03a.xml')[:3]

    print 'tagged words:', brown_corpus.tagged_words(fileids='03a.xml')[:7]
    print 'tagged sents:', brown_corpus.tagged_sents(fileids='03a.xml')[:3]

    print "Adam:", '\t', brown_corpus.sents(fileids='03a.xml', speaker='CHI')[:5]
    print "Mother:", brown_corpus.sents(fileids='03a.xml', speaker='MOT')[:2]

    mother_unstemmed = brown_corpus.sents(
        fileids='03a.xml', speaker='MOT')


    mother_stemmed = brown_corpus.sents(
        fileids='03a.xml', speaker='MOT', stem=True)
    mother_root = [[stemmed_word.split(
        '-')[0] for stemmed_word in stemmed_sent] for stemmed_sent in mother_stemmed]

    print 'Raw:\t\t', mother_unstemmed[:2]
    print 'Stemmed:\t', mother_stemmed[:2]
    print 'Roots only:\t', mother_root[:2]



if __name__ == '__main__':
    main()
