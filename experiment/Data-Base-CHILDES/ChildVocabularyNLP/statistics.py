pennTreeBankPOS = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']

class StatisticAnalisys(object):

	def __init__(self):
		pass
	
	def percent_PosList(self, vetor):
		
		indices = []
		tabela = []

		for i in vetor:
			if i[0] not in indices:
				indices.append(i[0])
		
		for i in indices:			#percorre as listas (índices)
			lista = []
			lista.append((i,0,0))		#append no índice da lista
			
			tamLista = 0
			for a in vetor:
				if (a[0] == i):
					tamLista += 1
				
			lista.append((tamLista,0,0))	#append no tamanho da lista (exige que a lista esteja ordenada por indice)
			
			for j in pennTreeBankPOS:	#percorre os possíveis POS
				count = 0
				
				for k in vetor:		#percorre as palavras de cada lista
					
					if (j == k[2]) & (i == k[0]):
						count += 1
				
				#lista.append((j, count, '{0:.2f}'.format((count/tamLista)*100))) #POS, count, %
				lista.append((j, count, '{0:.3f}'.format(count/tamLista))) #POS, count, %
			
			tabela.append(lista)
		
		return tabela