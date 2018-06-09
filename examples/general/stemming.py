#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
	Stemming
	Description: Redução da palavra até o radical, Isso é possível ao remover seus afixos e 
				 vogais temáticas das palavras.
'''
import nltk 

stemmer = nltk.stem.RSLPStemmer()

print stemmer.stem('frequentemente')
print stemmer.stem('copiar')

'''
	Função que recebe um texto e retorna a raiz de cada palavra.
'''
def Stemming(instancia):
  stemmer = nltk.stem.RSLPStemmer()
  palavras = []
  
  for w in instancia.split():
      palavras.append(stemmer.stem(w))
  return (" ".join(palavras))

print Stemming('Ele trabalhava frequentemente no projeto de criacao de novos produtos')