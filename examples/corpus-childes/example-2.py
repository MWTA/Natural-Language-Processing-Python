#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Software: CHILDES Corpus Readers
 Description: How to use CHILDESCorpusReader
              Read the XML version of the CHILDES corpus.
              http://www.nltk.org/howto/childes.html
 Version: 0.0.1
 Date: 16/04/2018
 Autor: RodriguesFAS
 Email: <franciscosouzaacer@gmail.com> | <fasr@cin.ufpe.br>
 Website: <http://rodriguesfas.com.br> | <http://clubedosgeeks.com.br>
 Github: <https://github.com/rodriguesfas>
'''

import os
import nltk
import numpy as np
import pandas as pd

from nltk.corpus.reader import CHILDESCorpusReader

def main():
    nltk_download_dir = '/home/rodriguesfas/nltk_data'

    brown_corpus_root = os.path.join(
        nltk_download_dir, 'corpora/CHILDES/Eng-NA-MOR/Valian/')

    brown_corpus = CHILDESCorpusReader(root=brown_corpus_root, fileids='.+xml')

    #exibe os arquivos
    print brown_corpus.fileids()

    #conta o numero de arquivos
    print len(brown_corpus.fileids())

    #exibe propriedade dos arquivos
    corpus_data = brown_corpus.corpus(brown_corpus.fileids())
    print(corpus_data[0]['Lang'])

    for key in sorted(corpus_data[0].keys()):
        print(key, ": ", corpus_data[0][key])

    # Imprimindo informações dos participantes do corpus. 
    # Os códigos mais comuns para os participantes são 'CHI' (filho alvo), 'MOT' (mãe) e 'INV' (investigador).
    corpus_participants = brown_corpus.participants(brown_corpus.fileids())
    for this_corpus_participants in corpus_participants[:2]:
        for key in sorted(this_corpus_participants.keys()):
            dct = this_corpus_participants[key]
            print(key, ": ", [(k, dct[k]) for k in sorted(dct.keys())])

    # printing words.
    print brown_corpus.words('01a.xml')

    # printing sentences.
    print brown_corpus.sents('01a.xml')

    #You can specify the participants with the argument speaker.
    print brown_corpus.words('01a.xml', speaker=['INV'])
    print brown_corpus.words('01a.xml', speaker=['MOT'])
    print brown_corpus.words('01a.xml', speaker=['CHI'])

    # tagged_words() and tagged_sents() return the usual (word,pos) tuple lists. 
    # POS tags in the CHILDES are automatically assigned by MOR and POST programs (MacWhinney, 2000).
    print brown_corpus.tagged_words('01a.xml')[:30]

    print brown_corpus.tagged_sents('01a.xml')[:10]

    # When the argument stem is true, the word stems (e.g., 'is' -> 'be-3PS') are used instread of the original words.
    print brown_corpus.words('01a.xml')[:30]
    print brown_corpus.words('01a.xml', stem=True)[:30]

    #When the argument replace is true, the replaced words are used instread of the original words.
    print brown_corpus.words('01a.xml', speaker='CHI')[247]
    print brown_corpus.words('01a.xml', speaker='CHI', replace=True)[247]

    # When the argument relation is true, the relational relationships in the sentence are returned. 
    # See Sagae et al. (2010) for details of the relational structure adopted in the CHILDES.
    print brown_corpus.words('01a.xml', relation=True)[:10]

    # Printing age. When the argument month is true, the age information in the CHILDES format is converted into the number of months.
    print brown_corpus.age()
    print brown_corpus.age('01a.xml')
    print brown_corpus.age('01a.xml', month=True)

    # Printing MLU. The criteria for the MLU computation is broadly based on Brown (1973).
    print brown_corpus.MLU()
    print brown_corpus.MLU('01a.xml')

    # Basic stuff 
    # Count the number of words and sentences of each file.

    for this_file in brown_corpus.fileids()[:6]:
        print(brown_corpus.corpus(this_file)[0]['Corpus'], brown_corpus.corpus(this_file)[0]['Id'])
        print("num of words: %i" % len(brown_corpus.words(this_file)))
        print("num of sents: %i" % len(brown_corpus.sents(this_file)))
    

if __name__ == '__main__':
    main()
