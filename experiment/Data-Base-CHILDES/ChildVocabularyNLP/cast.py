
class CastClass(object):
	def __init__(self):
		pass

	def word_to_index1(self, vetor):
		lista_palavras = []
		lista_frases = []
		
		for i in vetor:
			for j in i:
				lista_palavras.append(('A', j[0], j[1]))		# o A é sem importância =)
			lista_frases.append((lista_palavras))
		
		return lista_frases