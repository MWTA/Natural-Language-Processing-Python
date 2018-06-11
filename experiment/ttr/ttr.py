#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Software: TTR
 Description: Type-token ration of written language.
 Version: 0.0.1
 Date: 03/03/2018
 Autor: RodriguesFAS
 Email: <franciscosouzaacer@gmail.com> | <fasr@cin.ufpe.br>
 Website: <http://rodriguesfas.com.br> | <http://clubedosgeeks.com.br>
 Github: <https://github.com/rodriguesfas>
'''

import nltk
from nltk import FreqDist
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text_src = open(
	'/home/rodriguesfas/Workspace/Natural-Language-Processing-Python/experiment/ttr/corpus.txt').read()
print "\n>> Texto: Linguagem escrita \n", text_src

text_lowercase = text_src.lower()

tokens = nltk.word_tokenize(text_lowercase)

words = [word for word in tokens if word.isalpha()]

num_of_tokens = len(words)
print "\n>> Number of Tokens", num_of_tokens

#print ">> Lista de palavras"
#print words

list_freq = []

for y in xrange(len(words)):
	aux = words[y], words.count(words[y])
	list_freq.append(aux)

#print ">> Lista montada \n", list_freq

rank = list(set(list_freq))

print "\nTabela: Frequência de ocorrência das palavras:"
for y in xrange(len(rank)):
	print y+1, rank[y]

'''
	Calcular o numero de tokens e o numero de types.
'''
num_of_types = len(rank)

print "\n>> Number of Types", num_of_types

'''
	Calcula o valor do Tipo-token Ratio
'''
ttr = float(num_of_types) / float(num_of_tokens) * 100

print "\n>> Type-token ration %.2f" % ttr, "%"
print "\n>> Interpretação: \n Quanto mais types existirem em comparação com token, mais rico é o vocabulário. \n Isto é, uma TTR alta indica um maior variedade lexical."

'''
	Identificação da classe gramatical das palavras.
'''
# Remove as palavras dulicadas antes de classsificar
list_words_norepet = list(set(words))

# classifica as palavras.
classe = nltk.pos_tag(list_words_norepet)
#print "\n>> Classificação das palavras: \n", classe

'''
	Identificação de Entidades
'''
# Identificação de entidades
entities = nltk.chunk.ne_chunk(classe)
print "\nIdentificação de entidades: \n", entities


freq = FreqDist(tokens)

palavras = freq.keys()
y_pos = np.arange(len(palavras))
contagem = freq.values()

plt.bar(y_pos, contagem, align='center', alpha=0.9)
plt.xticks(y_pos, palavras)
plt.ylabel('Frequencia')
plt.title('Frequencia das palavras no texto.')
plt.show()


'''
	Wordcloud
'''
wordcloud = WordCloud(max_font_size=100,width = 1520, height = 535).generate(text_src)
plt.figure(figsize=(16,9))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
