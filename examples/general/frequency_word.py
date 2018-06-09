#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Software: Frequency Word
 Description: Exibe gráfico com frequência de palavras
 Version: 0.0.1
 Date: 30/03/2018
 Autor: RodriguesFAS
 Email: <franciscosouzaacer@gmail.com> | <fasr@cin.ufpe.br>
 Website: <http://rodriguesfas.com.br> | <http://clubedosgeeks.com.br>
 Github: <https://github.com/rodriguesfas>
'''

from nltk import FreqDist
import numpy as np
import matplotlib.pyplot as plt

frequencia = FreqDist(['six','six','six','Iron Maiden','the','Best','Iron Maiden','forever'])
palavras = frequencia.keys()
y_pos = np.arange(len(palavras))
contagem = frequencia.values()

plt.bar(y_pos, contagem, align='center', alpha=0.5)
plt.xticks(y_pos, palavras)
plt.ylabel('Frequencia')
plt.title('Frequencia das palavras na frase')
plt.show()