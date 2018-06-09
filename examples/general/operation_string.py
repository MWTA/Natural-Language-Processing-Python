#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Software: Operation String
 Description: 
 Version: 0.0.1
 Date: 03/03/2018
 Autor: RodriguesFAS
 Email: <franciscosouzaacer@gmail.com> | <fasr@cin.ufpe.br>
 Website: <http://rodriguesfas.com.br> | <http://clubedosgeeks.com.br>
 Github: <https://github.com/rodriguesfas>
'''

import nltk

text_src = open('corpus.txt').read()

tokens = nltk.word_tokenize(text_src)
print(tokens)

'''
	Conta quantas palavras contem na frase.
	len()
'''
print "Contem ",len(tokens)," palavras"

'''
	Contar quantas ocorrências tem uma palavra em um texto.

	lower() - coloca todas as palavras para minusculo.
	count() - conta todas as palavras.
'''
cont_word = text_src.lower()
print cont_word.count('all')

'''
	União de String
'''
lista = ['hot','dog']
print ''.join(lista)

