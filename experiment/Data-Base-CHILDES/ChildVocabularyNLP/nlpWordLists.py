import csv

from nltk.stem import WordNetLemmatizer

from posTag import POSTagger
from replacers import RegexpReplacer
from scores import Score
from statistics import StatisticAnalisys

wordnet_lemmatizer = WordNetLemmatizer()
replacer = RegexpReplacer()
tagger = POSTagger()
some_score = Score()
statistic = StatisticAnalisys()

original_words = []
splited_words = []
splited_words_pos = []
canonical_words_pos = []
commonality_words = []
canonical_words_statistic = []
splited_words_statistic = []


with open('input/palavras_por_lista_artigos.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        original_words.append((row['list'], row['word'].strip()))


splited_words = replacer.replace_all_list(original_words)
splited_words_pos = tagger.lazyTag(splited_words)
canonical_words_pos = tagger.canonicalTag(splited_words)

# print(canonical_words_pos)

# list = []
# words = []
# index = canonical_words_pos[0][0]
# # print(index)
#
# for i in canonical_words_pos:
#     # print(i)
#     if (i[0] == index):
#         # print(i[0])
#         if i[1] not in words:
#             # print(i[1])
#             words.append(i[1])
#             list.append((i[1], i[0]))
#     else:
#         # print(list)
#         with open('output/Lists/word_list_' + index + '.csv', 'w') as csvfile:
#             fieldnames = ['word','list']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
#             writer.writeheader()
#             for iA in list:
#                 writer.writerow({'word': iA[0], 'list': iA[1]})
#
#         list = [(i[1], i[0])]
#         index = i[0]

# with open('output/Lists/word_list_' + index + '.csv', 'w') as csvfile:
#     fieldnames = ['list', 'word']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
#     writer.writeheader()
#     for iA in list:
#         writer.writerow({'list': iA[0], 'word': iA[1]})







# core_word_list = some_score.commonality(original_words, 'A')
core_word_list = some_score.commonality(canonical_words_pos, 'A')

# canonical_words_statistic = statistic.percent_PosList(canonical_words_pos)
# splited_words_statistic = statistic.percent_PosList(splited_words_pos)
#
#
# with open('output/pos_canonicas.csv', 'w') as csvfile:
#     fieldnames = ['list', 'word', 'pos']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
#     writer.writeheader()
#     for i in canonical_words_pos:
#         writer.writerow({'list': i[0], 'word': i[1], 'pos': i[2]})
#
# with open('output/pos_originais.csv', 'w') as csvfile:
#     fieldnames = ['list', 'word', 'pos']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
#     writer.writeheader()
#     for i in splited_words_pos:
#         writer.writerow({'list': i[0], 'word': i[1], 'pos': i[2]})

#TODO rodar comonalidade!!

with open('output/word_list_commonality.csv', 'w') as csvfile:
    # fieldnames = ['word', 'commonality', 'posTag']
    fieldnames = ['word', 'commonality', 'POS', 'type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
    writer.writeheader()
    for i in core_word_list:
        writer.writerow({'word': i[0], 'commonality': i[1], 'POS': i[2][0][1],'type': i[3]})
        # writer.writerow({'word': i[0], 'commonality': int(i[1]), 'posTag': i[2][0][1]})

# # Estatísticas de POS e porcentagem por lista (PS: no csv gerado, fazer a transposta da matriz com o Excel)
# with open('output/listas_estatistica.csv', 'w') as csvfile:
#     fieldnames = ['list', 'size', 'CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
#     writer.writeheader()
#
#     for i in splited_words_statistic:
#         writer.writerow({'list': i[0][0] + ' Bruta', 'size': i[1][0], 'CC': i[2][1], 'CD': i[3][1], 'DT': i[4][1], 'EX': i[5][1], 'FW': i[6][1], 'IN': i[7][1], 'JJ': i[8][1], 'JJR': i[9][1], 'JJS': i[10][1], 'LS': i[11][1], 'MD': i[12][1], 'NN': i[13][1], 'NNP': i[14][1], 'NNPS': i[15][1], 'NNS': i[16][1], 'PDT': i[17][1], 'POS': i[18][1], 'PRP': i[19][1], 'PRP$': i[20][1], 'RB': i[21][1], 'RBR': i[22][1], 'RBS': i[23][1], 'RP': i[24][1], 'SYM': i[25][1], 'TO': i[26][1], 'UH': i[27][1], 'VB': i[28][1], 'VBD': i[29][1], 'VBG': i[30][1], 'VBN': i[31][1], 'VBP': i[32][1], 'VBZ': i[33][1], 'WDT': i[34][1], 'WP': i[35][1], 'WP$': i[36][1], 'WRB': i[37][1]})
#         writer.writerow({'list': ' ', 'size': ' ', 'CC': i[2][2], 'CD': i[3][2], 'DT': i[4][2], 'EX': i[5][2], 'FW': i[6][2], 'IN': i[7][2], 'JJ': i[8][2], 'JJR': i[9][2], 'JJS': i[20][2], 'LS': i[11][2], 'MD': i[12][2], 'NN': i[13][2], 'NNP': i[14][2], 'NNPS': i[15][2], 'NNS': i[16][2], 'PDT': i[17][2], 'POS': i[18][2], 'PRP': i[19][2], 'PRP$': i[20][2], 'RB': i[21][2], 'RBR': i[22][2], 'RBS': i[23][2], 'RP': i[24][2], 'SYM': i[25][2], 'TO': i[26][2], 'UH': i[27][2], 'VB': i[28][2], 'VBD': i[29][2], 'VBG': i[30][2], 'VBN': i[31][2], 'VBP': i[32][2], 'VBZ': i[33][2], 'WDT': i[34][2], 'WP': i[35][2], 'WP$': i[36][2], 'WRB': i[37][2]})
#
#     for j in canonical_words_statistic:
#         writer.writerow({'list': j[0][0] + ' Canonica', 'size': j[1][0], 'CC': j[2][1], 'CD': j[3][1], 'DT': j[4][1], 'EX': j[5][1], 'FW': j[6][1], 'IN': j[7][1], 'JJ': j[8][1], 'JJR': j[9][1], 'JJS': j[10][1], 'LS': j[11][1], 'MD': j[12][1], 'NN': j[13][1], 'NNP': j[14][1], 'NNPS': j[15][1], 'NNS': j[16][1], 'PDT': j[17][1], 'POS': j[18][1], 'PRP': j[19][1], 'PRP$': j[20][1], 'RB': j[21][1], 'RBR': j[22][1], 'RBS': j[23][1], 'RP': j[24][1], 'SYM': j[25][1], 'TO': j[26][1], 'UH': j[27][1], 'VB': j[28][1], 'VBD': j[29][1], 'VBG': j[30][1], 'VBN': j[31][1], 'VBP': j[32][1], 'VBZ': j[33][1], 'WDT': j[34][1], 'WP': j[35][1], 'WP$': j[36][1], 'WRB': j[37][1]})
#         writer.writerow({'list': ' ', 'size': ' ', 'CC': j[2][2], 'CD': j[3][2], 'DT': j[4][2], 'EX': j[5][2], 'FW': j[6][2], 'IN': j[7][2], 'JJ': j[8][2], 'JJR': j[9][2], 'JJS': j[20][2], 'LS': j[11][2], 'MD': j[12][2], 'NN': j[13][2], 'NNP': j[14][2], 'NNPS': j[15][2], 'NNS': j[16][2], 'PDT': j[17][2], 'POS': j[18][2], 'PRP': j[19][2], 'PRP$': j[20][2], 'RB': j[21][2], 'RBR': j[22][2], 'RBS': j[23][2], 'RP': j[24][2], 'SYM': j[25][2], 'TO': j[26][2], 'UH': j[27][2], 'VB': j[28][2], 'VBD': j[29][2], 'VBG': j[30][2], 'VBN': j[31][2], 'VBP': j[32][2], 'VBZ': j[33][2], 'WDT': j[34][2], 'WP': j[35][2], 'WP$': j[36][2], 'WRB': j[37][2]})

print('OK')