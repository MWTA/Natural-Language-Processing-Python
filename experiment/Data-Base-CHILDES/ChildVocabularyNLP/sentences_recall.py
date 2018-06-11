#coding=utf-8

import csv
import os


# import nltk

# nltk.download()

from scores import Score

some_score = Score()

'''
1 - To run RECALL BY CORPUS BY COMMONALITY:
corpora = 'ByCorpus'
folder = 'ByCommonality'

2 - To run RECALL BY CORPUS BY LIST:
corpora = 'ByCorpus'
folder = 'ByList'

3 - To run RECALL BY AGE BY COMMONALITY:
corpora = 'ByAge'
folder = 'ByCommonality'

4 - To run RECALL BY AGE BY LIST:
corpora = 'ByAge'
folder = 'ByList'
'''

corpora = 'ByCorpus'
# corpora = 'ByAge'

folder = 'ByCommonality'
# folder = 'ByList'

path_sentences = 'Corpus/Sentences/' + corpora + '/Canonical/'
path_word_frequency = 'Recall/Recall' + corpora + '/' + folder + '/NotRecalled/'
path_lists = 'input/Lists'



def word_phrase_coverage_by_commonality(file):
    commonality_words = []
    canonical_sentences = []

    with open('input/word_list_J_commonality.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            commonality_words.append((row['word'].strip().replace("’", "'"), row['commonality']))

    for line in open(path_sentences + file, 'r'):
        word = ''
        sentence = []
        for i in line:
            if i != ' ':
                word = word + i
            else:
                sentence.append(word)
                word = ''
        canonical_sentences.append(sentence)

    unique_words_frequency = some_score.frequency_word(canonical_sentences)

    # print(unique_words_frequency)

    coverage_spreadsheet = some_score.word_sentence_recall_by_commonality(commonality_words,
                                                                          unique_words_frequency[1],
                                                                          unique_words_frequency[0])

    with open('Recall/Recall' + corpora + '/' + folder + '/Recalled/word_sentence_recall_' + file.split('.')[
        0] + '_by_commonality.csv', 'w') as csvfile:
        fieldnames = ['word', 'commonality', 'cobertura', 'word_order']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
        writer.writeheader()
        for i in coverage_spreadsheet:
            writer.writerow({'word': i[0], 'commonality': i[1], 'cobertura': i[2], 'word_order': i[3]})

    not_recalled_words = some_score.not_recalled_words(commonality_words, unique_words_frequency)

    core_word_not_used = []
    corpus_words_upper = []

    for i in unique_words_frequency[1]:
        corpus_words_upper.append(i[0].upper())

    for w in commonality_words:
        if w[0].upper() not in corpus_words_upper:
            core_word_not_used.append(w)

    with open('Recall/Recall' + corpora + '/' + folder + '/NotUsedCore/not_used_core_' + file.split('.')[
        0] + '_by_commonality.csv', 'w') as csvfile:
        fieldnames = ['word', 'commonality']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
        writer.writeheader()
        for i in core_word_not_used:
            writer.writerow({'word': i[0], 'commonality': i[1]})

    with open('Recall/Recall' + corpora + '/' + folder + '/Frequency/word_frequency_' + file.split('.')[
        0] + '_by_commonality.csv', 'w') as csvfile:
        fieldnames = ['word', 'quantity', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
        writer.writeheader()
        for i in unique_words_frequency[1]:
            writer.writerow({'word': i[0], 'quantity': i[1], 'frequency': i[2]})

    with open('Recall/Recall' + corpora + '/' + folder + '/NotRecalled/not_recalled_words_' + file.split('.')[
        0] + '_by_commonality.csv', 'w') as csvfile:
        fieldnames = ['word', 'quantity', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
        writer.writeheader()
        for i in not_recalled_words:
            writer.writerow({'word': i[0], 'quantity': i[1], 'frequency': i[2]})


def word_phrase_recall_by_list(file):

    canonical_sentences = []

    for i2 in os.listdir(path_lists):
        print(i2)
        core_word_list = []
    # i2 = 'word_list_A.csv'

        with open('input/Lists/' + i2) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                core_word_list.append((row['word'].strip().replace("’", "'"), row['list']))

        for line in open(path_sentences + file, 'r'):
            word = ''
            sentence = []
            for i in line:
                if i != ' ':
                    word = word + i
                else:
                    sentence.append(word)
                    word = ''
            canonical_sentences.append(sentence)

        unique_words_frequency = some_score.frequency_word(canonical_sentences)

        coverage_spreadsheet = some_score.word_sentence_recall_by_list(core_word_list, unique_words_frequency[1],
                                                                       unique_words_frequency[0])

        with open('Recall/Recall' + corpora + '/' + folder + '/Recalled/word_sentence_recall_' + file.split('.')[0] + '_' + i2.split('.')[0] + '.csv', 'w') as csvfile:
            fieldnames = ['word', 'frequency', 'cobertura', 'word_order']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
            writer.writeheader()
            for i in coverage_spreadsheet:
                writer.writerow({'word': i[0], 'frequency': i[1], 'cobertura': i[2], 'word_order': i[3]})

        not_covered_words = some_score.not_recalled_words(core_word_list, unique_words_frequency)

        core_word_not_used = []
        corpus_words_upper = []

        for i in unique_words_frequency[1]:
            corpus_words_upper.append(i[0].upper())

        for w in core_word_list:
            if w[0].upper() not in corpus_words_upper:
                core_word_not_used.append(w)

        with open('Recall/Recall' + corpora + '/' + folder + '/NotUsedCore/not_used_core_' + file.split('.')[0] + '_' +
                          i2.split('.')[0] + '.csv', 'w') as csvfile:
            fieldnames = ['word']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
            writer.writeheader()
            for i in core_word_not_used:
                writer.writerow({'word': i[0]})

        with open('Recall/Recall' + corpora +'/' + folder + '/Frequency/word_frequency_' + file.split('.')[0] + '_' +
                          i2.split('.')[0] + '.csv', 'w') as csvfile:
            fieldnames = ['word', 'quantity', 'frequency']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
            writer.writeheader()
            for i in unique_words_frequency[1]:
                writer.writerow({'word': i[0], 'quantity': i[1], 'frequency': i[2]})

        with open('Recall/Recall' + corpora + '/' + folder + '/NotRecalled/not_recalled_words_' + file.split('.')[0] + '_' +
                          i2.split('.')[0] + '.csv', 'w') as csvfile:
            fieldnames = ['word', 'quantity', 'frequency']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
            writer.writeheader()
            for i in not_covered_words:
                writer.writerow({'word': i[0], 'quantity': i[1], 'frequency': i[2]})


def not_recalled_relative_frequency(relative_frequency, folder):
    total_relative_frequency = []
    unique_words_upper = []
    unique_words = []

    for i in relative_frequency:
        if i[0].upper() not in unique_words_upper:
            unique_words_upper.append(i[0].upper())
            unique_words.append(i[0])

    for i in unique_words:
        sum_freq = 0
        count = 0
        for j in relative_frequency:
            if i.upper() == j[0].upper():
                sum_freq += float(j[1])
                count += 1

        total_relative_frequency.append((i, "{0:.4f}".format(float(sum_freq)/count), count))

    with open('Recall/Recall' + corpora + '/' + folder + '/NotRecalledTotal/not_recalled_words_total_' + 'byCorpus_' + folder + '.csv','w') as csvfile:
        fieldnames = ['word', 'relative_frequency', 'corpus_commonality']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
        writer.writeheader()
        for i in total_relative_frequency:
            writer.writerow({'word': i[0], 'relative_frequency': i[1], 'corpus_commonality': i[2]})



for i1 in os.listdir(path_sentences):
    print('entrei')
    print(i1)

    if folder == 'ByList':
        word_phrase_recall_by_list(i1)
    if folder == 'ByCommonality':
        word_phrase_coverage_by_commonality(i1)


relative_frequency = []

'''
Run this part after the previous one
'''
# for i2 in os.listdir(path_word_frequency):
#
#     with open('Recall/Recall' + corpora + '/' + folder + '/NotRecalled/' + i2) as csvfile:
#         reader = csv.DictReader(csvfile, delimiter=';')
#         for row in reader:
#             relative_frequency.append((row['word'], row['quantity'], row['frequency']))
#
# not_recalled_relative_frequency(relative_frequency, folder)

print('OK')