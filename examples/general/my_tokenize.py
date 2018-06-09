#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Software: Tokenize
 Description: Separa as palavras de um Texto, Frase, Sentença.
 Version: 0.0.1
 Date: 30/03/2018
 Autor: RodriguesFAS
 Email: <franciscosouzaacer@gmail.com> | <fasr@cin.ufpe.br>
 Website: <http://rodriguesfas.com.br> | <http://clubedosgeeks.com.br>
 Github: <https://github.com/rodriguesfas>
'''

import nltk
from nltk import FreqDist
import matplotlib.pyplot as plt
#import matplotlib

text_src = open('corpus.txt').read()

'''
	nltk.word_tokenize(text)
'''
print "=====================[word_tokenize]"
tokens = nltk.word_tokenize(text_src)
print tokens

'''
	Retorna a frequência max de uma palavra
	FreqDist()
'''
print "=====================[FreqDist]"
frequency_word = FreqDist('are')
print frequency_word

'''
	Retorna a frequência da palavra mais frequente.
'''
print "=====================[max]"
print frequency_word.max()
