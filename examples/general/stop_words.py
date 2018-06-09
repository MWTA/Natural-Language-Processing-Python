#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
	StopWords
	Description: Remoção de palavras ou artigos usados em um texto, como "a", "de", "o", "da", entre outras.
'''
import nltk 

'''
	Exibe um dicionário do NLTK que contem palavras em português consideradas stopwords.
'''
stopwords = nltk.corpus.stopwords.words('portuguese')
#print stopwords

'''
	Função recebe um texto e remove os stopwords
'''
def RemoviStopWords(instancia):
	instancia = instancia.lower()
	stopwords = set(nltk.corpus.stopwords.words('portuguese'))
	palavras = [i for i in instancia.split() if not i in stopwords]
	return (" ".join(palavras)) 

print RemoviStopWords('Ola mundo, estou trabalhando com textos no artigo do minerando dados')
