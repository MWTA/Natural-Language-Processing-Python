import csv
import os

import io
import nltk
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus.reader import CHILDESCorpusReader
from nltk.corpus import wordnet as wn

from replacers import RegexpReplacer

corpus_root = nltk.data.find('corpora/childes/data-xml/Eng-UK-MOR/')

replacer = RegexpReplacer()
wordnet_lemmatizer = WordNetLemmatizer()

path = 'Corpus/FolderByAge/'

classeAberta = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']

# TODO tirar as onomatopeias?? POS = on

def canonicalTag(palavra):

    j = nltk.tag.pos_tag([palavra])
    # pal_pos = (j[0][0], j[0][1])

    pal = []
    unique_pal = []

    if j[0][1] in classeAberta:

        if wn.morphy(j[0][0], wn.VERB) != None:
            canonico_pos = wordnet_lemmatizer.lemmatize(j[0][0], pos='v')
            pal.append(canonico_pos)

        elif (wn.morphy(j[0][0], wn.NOUN) != None):
            canonico_pos = wordnet_lemmatizer.lemmatize(j[0][0], pos='n')
            pal.append(canonico_pos)

        elif (wn.morphy(j[0][0], wn.ADJ) != None):
            canonico_pos = wordnet_lemmatizer.lemmatize(j[0][0], pos='a')
            pal.append(canonico_pos)

        elif (wn.morphy(j[0][0], wn.ADV) != None):
            canonico_pos = wordnet_lemmatizer.lemmatize(j[0][0], pos='r')
            pal.append(canonico_pos)

        else:
            pal.append(j[0][0])

    else:
        pal.append(j[0][0])

    for i in pal:
        if i not in unique_pal:
            unique_pal.append(i)

    return unique_pal[0]


def read_files_by_age(file):
    phrase = []
    sentences = []
    canonical_sentences = []
    tuple = []

    unknown = ['xxx', 'www', 'mm']
    ignoredMotPOS = ['chi', 'fam', 'neo']

    with open(path + file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            tuple.append((row['path']))

    for i1 in tuple:
        source = CHILDESCorpusReader(corpus_root, i1)
        sents_chi_pos = source.tagged_sents(speaker='CHI', replace=True)

        for i2 in sents_chi_pos:
            for j1 in i2:
                if (j1[0] not in unknown) & (j1[0] != '') & (j1[1] not in ignoredMotPOS):
                    phrase.append(j1[0])

            if phrase != []:
                t_sentences = []
                treated_sentence = []
                for i3 in phrase:
                    res = re.search(r"(?!'.*')\b[\w']+\b", i3)
                    t_sentences.append(res.group(0))
                treated_sentence.append(t_sentences)
                sentences.append(t_sentences)

                for i4 in treated_sentence:

                    splited_phrase = []
                    for j2 in i4:
                        rep = replacer.replace(j2)
                        if ' ' in rep:
                            a, b = rep.split(' ')
                            splited_phrase.append(canonicalTag(a))
                            splited_phrase.append(canonicalTag(b))
                        else:
                            splited_phrase.append(canonicalTag(rep))
                    canonical_sentences.append(splited_phrase)
                # sentences = []
            phrase = []

    # target = open('Corpus/ByAge/Original/sentence_' + file.split('.')[0] + '.txt', encoding='utf-8')
    # target_canonical =  open('Corpus/ByAge/Canonical/canonical_sentence_' + file.split('.')[0] + '.txt' , mode='w' , encoding='utf-8')

           # shutil.copyfileobj(source, target)

    target = open('Corpus/Sentences/ByAge/Original/sentence_' + file.split('.')[0] + '.txt', 'w')
    target_canonical = open('Corpus/Sentences/ByAge/Canonical/canonical_sentence_' + file.split('.')[0] + '.txt', 'w')

    for i5 in sentences:
        for j4 in i5:
            target.write(j4+ ' ')
        target.write('\n')
    target.close()
    print('terminei (original)')

    for i6 in canonical_sentences:
        for j5 in i6:
            target_canonical.write(j5+ ' ')
        target_canonical.write('\n')
    target_canonical.close()
    print('terminei (canonico)')


for i7 in os.listdir(path):
    print(i7)
    read_files_by_age(i7)

# read_files_by_age('age_18_23.csv')

print('OK!')