#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Software: Examples
 Description: 
 Version: 0.0.1
 Date: 30/03/2018
 Email: <franciscosouzaacer@gmail.com> | <fasr@cin.ufpe.br>
 Website: <http://rodriguesfas.com.br> | <http://clubedosgeeks.com.br>
 Github: <https://github.com/rodriguesfas>
'''

__author__ = 'Rodriguesfas'

import nltk

text = 'Mr. Green killed Colonel Mustard in the study vith the candlestick. Mr. Green killed Colonel Mustard in the study vith the candlestick.'
#print(text.split('.'))
#print(text.split(' '))

# Identifica quando uma Frase temina, fazendo distinção de abreviações.
phrase = nltk.tokenize.sent_tokenize(text)
print(phrase)

# Tokens - Separa cada palavra do texto.
tokens = nltk.word_tokenize(text)
print(tokens)

# Identifica a classe gramatical de cada palavra.
classes = nltk.pos_tag(tokens)

# Identificação de entidades
entities = nltk.chunk.ne_chunk(classes)
print(entities)
