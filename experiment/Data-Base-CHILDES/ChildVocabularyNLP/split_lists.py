import csv

from posTag import POSTagger
from replacers import RegexpReplacer
from scores import Score

replacer = RegexpReplacer()
tagger = POSTagger()
some_score = Score()

original_words = []
splited_words = []
splited_words_pos = []
canonical_words_pos = []

with open('input/palavras_por_lista_artigos.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        original_words.append((row['list'], row['word'].strip()))


splited_words = replacer.replace_all_list(original_words)
canonical_words_pos = tagger.canonicalTag(splited_words)

classeAberta = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']

list = []
words = []
index = canonical_words_pos[0][0]
# print(index)

for i in canonical_words_pos:
    # print(i)
    if i[0] == index:
        # print(i[0])
        if (i[1],i[2]) not in words:
            # print(i[1])
            words.append(i[1])
            if i[2] in classeAberta:
                list.append((i[1], i[0], i[2], 'OpenClass'))
            else:
                list.append((i[1], i[0], i[2], 'ClosedClass'))
    else:
        # print(list)
        with open('input/Lists/word_list_' + index + '.csv', 'w') as csvfile:
            fieldnames = ['word','list','POS','type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
            writer.writeheader()
            for iA in list:
                # print(iA)
                writer.writerow({'word': iA[0], 'list': iA[1], 'POS': iA[2], 'type': iA[3]})

        words = []
        list = []

        if i[2] in classeAberta:
            list = [(i[1], i[0], i[2], 'OpenClass')]
        else:
            list = [(i[1], i[0], i[2], 'ClosedClass')]
        # list = [(i[1], i[0])]
        index = i[0]

with open('input/Lists/word_list_' + index + '.csv', 'w') as csvfile:
    fieldnames = ['word','list','POS','type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
    writer.writeheader()
    for iA in list:
        writer.writerow({'word': iA[0], 'list': iA[1], 'POS': iA[2], 'type': iA[3]})

words = []
list = []

print('OK')

core_word_list = some_score.commonality(canonical_words_pos, 'A')

with open('input/word_list_J_commonality.csv', 'w') as csvfile:
    fieldnames = ['word', 'list', 'POS', 'type', 'commonality']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
    writer.writeheader()
    for i in core_word_list:
        writer.writerow({'word': i[0], 'list': i[1], 'POS': i[2][0][1], 'type': i[3], 'commonality': i[4]})