#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Software: My WordCloud
 Description: Exibe gráfico com frequência de palavras
 Version: 0.0.1
 Date: 04/04/2018
 Autor: RodriguesFAS
 Email: <franciscosouzaacer@gmail.com> | <fasr@cin.ufpe.br>
 Website: <http://rodriguesfas.com.br> | <http://clubedosgeeks.com.br>
 Github: <https://github.com/rodriguesfas>
'''
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
text = open('debate.csv','r').read()

wordcloud = WordCloud(max_font_size=100,width = 1520, height = 535).generate(text)

plt.figure(figsize=(16,9))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()