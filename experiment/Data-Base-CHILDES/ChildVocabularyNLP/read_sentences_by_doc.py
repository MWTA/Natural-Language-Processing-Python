#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import io
import nltk
from nltk.corpus.reader import CHILDESCorpusReader


def read_sentences_by_doc(corpus_X, x, doc_name, corpus_name):

    # LÊ AS FRASES POR DOCUMENTO

    sents_chi_pos = corpus_X.tagged_sents(x, speaker='CHI', replace=True)

    unknown = ['xxx', 'www', 'mm']
    ignoredMotPOS = ['chi', 'fam', 'neo', 'on']

    phrase = []
    sentences = []
    # canonical_sentences = []

    for i1 in sents_chi_pos:
        for j1 in i1:
            if (j1[0] not in unknown) & (j1[0] != '') & (j1[1] not in ignoredMotPOS):
                phrase.append(j1[0])

        # print(phrase)

        if phrase != []:
            t_sentences = []
            # treated_sentences = []
            # for i2 in phrase:
            #     res = re.search(r"(?!'.*')\b[\w']+\b", i2)
            #     t_sentences.append(res.group(0))
            # treated_sentences.append(t_sentences)
            sentences.append(t_sentences)

            # print(t_sentences)

            # for i4 in treated_sentences:
            #     splited_phrase = []
            #     particle = []
            #     for j2 in i4:
            #         if j2 in cont_list:
            #             for cont in contractions_list:
            #                 if j2 == cont[0]:
            #                     if cont[1]:
            #                         splited_phrase.append(cont[1])
            #                     if cont[2]:
            #                         # aqui conta o verbo
            #                         splited_phrase.append(cont[2])
            #                     if cont[3]:
            #                         # aqui é uma análise separada. O tipo de contração que usa
            #                         particle.append(cont[3])
            #         elif '\'s' in j2:
            #             rep = replacer.replace(j2)
            #             if ' ' in rep:
            #                 a, b = rep.split(' ')
            #                 splited_phrase.append(a)
            #                 particle.append(b)
            #         else:
            #             splited_phrase.append(j2)
            #     for x in particle:
            #         splited_phrase.append(x)
            #     canonical_sentences.append(splited_phrase)

        phrase = []

    target = io.open('ChildVocabularyNLP' +corpus_name + '_' + doc_name + '.txt', 'w', encoding='utf-8')

    for i3 in sentences:
        for j2 in i3:
            target.write(j2)
            target.write(' ')
        target.write('\n')
    target.close()

    return None


nltk_download_dir = '/home/rodriguesfas/nltk_data'
path_corpus_root = os.path.join(
    nltk_download_dir, 'corpora/CHILDES/Eng-UK-MOR/Thomas/')
corpus_name = "T"


# corpus_X = CHILDESCorpusReader(path_corpus_root, corpus_name + '/.*.xml')
corpus_X = CHILDESCorpusReader(path_corpus_root, corpus_name + '/.*.xml')
fileids = corpus_X.fileids()

for x in fileids:
    doc_name = x.split('.')[0].split(
        '/')[-1].replace('(', '').replace(')', '').replace(' ', '')
    doc_mlu = corpus_X.MLU(x, speaker=['CHI'])[0]
    doc_age = corpus_X.age(x, month=True)[0]
    doc_n_words = len(corpus_X.words(x, speaker=['CHI']))
    doc_n_sentences = len(corpus_X.sents(x, speaker=['CHI']))

    read_sentences_by_doc(corpus_X, x, doc_name, corpus_name)
