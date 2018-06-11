import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

classeAberta = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']




class POSWord(object):
	
	def __init__(self):
		self.wordnet_lemmatizer = WordNetLemmatizer()

	def toCanonical(self, vetor):
		
		lista = []
		
		for i in vetor:
			
			j = nltk.tag.pos_tag([i[1]])
			pal_pos = (i[0], j[0][0], j[0][1])

			if j[0][1] in classeAberta:

				hasClasse = False

				if wn.morphy(j[0][0], wn.NOUN) != None:
					hasClasse = True
					canonico_pos = self.wordnet_lemmatizer.lemmatize(j[0][0], pos='n')
					pal_pos = (i[0], canonico_pos, 'NN')
					if pal_pos not in lista:
						lista.append(pal_pos)
				
				if wn.morphy (j[0][0], wn.VERB) != None:
					hasClasse = True
					canonico_pos = self.wordnet_lemmatizer.lemmatize(j[0][0], pos='v')
					pal_pos = (i[0], canonico_pos, 'VB')
					if pal_pos not in lista:
						lista.append(pal_pos)
				
				if wn.morphy (j[0][0], wn.ADJ) != None:
					hasClasse = True
					canonico_pos = self.wordnet_lemmatizer.lemmatize(j[0][0], pos='a')
					pal_pos = (i[0], canonico_pos, 'JJ')
					if pal_pos not in lista:
						lista.append(pal_pos)
				
				if wn.morphy (j[0][0], wn.ADV) != None:
					hasClasse = True
					canonica = self.wordnet_lemmatizer.lemmatize(j[0][0], pos='r')
					pal_pos = (i[0], canonica, 'RB')
					if pal_pos not in lista:
						lista.append(pal_pos)
				
				if not hasClasse:
					if pal_pos not in lista:
						lista.append(pal_pos)
			else:
				if pal_pos not in lista:
					lista.append(pal_pos)
			
		return lista