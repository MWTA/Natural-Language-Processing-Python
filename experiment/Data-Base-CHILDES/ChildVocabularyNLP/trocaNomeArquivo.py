'''
Já foi feito. Não precisa mais...
'''

import sys, os

pathInput = 'C:/Users/nmf/PycharmProjects/ChildVocabularyNLP-master/Corpus/RecallByCorpus/ByList/NotUsedCore'
pathOutput = 'C:/Users/nmf/Desktop/temp/'

for i2 in os.listdir(pathInput):
    print(i2)

    name = i2.split('.')
    print(name)

    lista = name[0].split('_')[8]
    print(lista)

    print(name[0][:-1])
    # print(type(name[0][:-1]+'H'+'.'+ name[1]))

    if lista == 'A':
        os.rename(pathInput + '/' + i2, pathOutput + name[0][:-1] + 'H' + '.' + name[1])
    if lista == 'B':
        os.rename(pathInput + '/' + i2, pathOutput + name[0][:-1] + 'A' + '.' + name[1])
    if lista == 'C':
        os.rename(pathInput + '/' + i2, pathOutput + name[0][:-1] + 'F' + '.' + name[1])
    if lista == 'D':
        os.rename(pathInput + '/' + i2, pathOutput + name[0][:-1] + 'G' + '.' + name[1])
    if lista == 'E':
        os.rename(pathInput + '/' + i2, pathOutput + name[0][:-1] + 'C' + '.' + name[1])
    if lista == 'F':
        os.rename(pathInput + '/' + i2, pathOutput + name[0][:-1] + 'E' + '.' + name[1])
    if lista == 'G':
        os.rename(pathInput + '/' + i2, pathOutput + name[0][:-1] + 'B' + '.' + name[1])
    if lista == 'H':
        os.rename(pathInput + '/' + i2, pathOutput + name[0][:-1] + 'D' + '.' + name[1])
    if lista == 'I':
        os.rename(pathInput + '/' + i2, pathOutput + name[0][:-1] + 'I' + '.' + name[1])  #tá certo
    # else:
    #     print('Erro')

# os.rename()