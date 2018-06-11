#coding=utf-8
'''
Substituição de contrações pela forma completa baseado em Expressões Regulares
Recebe lista de palavras brutas e retorna uma lista de palavras separadas em linhas distintas
Não pega o caso onde o 's significa posse (e.g., Thiago's car)
'''

# Todo: case insensitive
# Todo: replace da pontuação. Separar a pontuação da palavra

import re

replacement_patterns = [
    (r'[Ww]on\'t', 'will not'),
    (r'[Cc]an\'t', 'cannot'),
    (r'I\'m', 'I am'),
    (r'[Aa]in\'t', 'is not'),
    (r'[Cc]\'mon', 'come on'),
    (r'[Gg]onna', 'going to'),
    (r'[Ww]anna', 'want a'),
    (r'(\w+)\'ll', '\g<1> will'),
    (r'(\w+)n\'t', '\g<1> not'),
    (r'(\w+)\'ve', '\g<1> have'),
    (r'(\w+)\'s', '\g<1> is'),
    (r'(\w+)\'re', '\g<1> are'),
    (r'(\w+)\'d', '\g<1> would'),
]

canonical_replacement_patterns = [
    (r'[Ww]on\'t', 'go not'),
    (r'[Cc]an\'t', 'cannot'),
    (r'I\'m', 'I be'),
    (r'[Aa]in\'t', 'be not'),
    (r'[Cc]\'mon', 'come on'),
    (r'[Gg]onna', 'go to'),
    (r'[Ww]anna', 'want a'),
    (r'(\w+)\'ll', '\g<1> go'),
    (r'(\w+)n\'t', '\g<1> not'),
    (r'(\w+)\'ve', '\g<1> have'),
    (r'(\w+)\'s', '\g<1> be'),
    (r'(\w+)\'re', '\g<1> be'),
    (r'(\w+)\'d', '\g<1> would'),
]

# replacement_clearString = [ "(?!'.*')\b[\w']+\b" ]

'''
class RegexpReplacerString(object):
	def __init__(self, patterns=replacement_clearString):
		self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

	def clear_string(self, vetor):
		for i in vetor:
			s = i
			for (pattern, repl) in self.patterns:
				(s, count) = re.subn(pattern, repl, s)
		return s
'''


class RegexpReplacer(object):

    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

    def replace(self, text):
        s = text
        # v = []
        for (pattern, repl) in self.patterns:
            (s, count) = re.subn(pattern, repl, s)

        # if ' ' not in s:
        #     v.append(s)
        # else:
        #     s1, s2 = s.split(' ')
        #     v.append(s1)
        #     v.append(s2)

        return s

    def canonical_replace(self, text):
        s = text
        patterns = [(re.compile(regex), repl) for (regex, repl) in canonical_replacement_patterns]
        for (patt, repl) in patterns:
            (s, count) = re.subn(patt, repl, s)

        return s

    def replace_all_list(self, vetor):
        lista = []

        for i in vetor:
            s = i[1]

            for (pattern, repl) in self.patterns:
                (s, count) = re.subn(pattern, repl, s)

                if count == 1:
                    break

            if count == 1:
                if ' ' not in s:
                    lista.append((i[0], s))
                else:
                    s1, s2 = s.split(' ')
                    lista.append((i[0], s1))
                    lista.append((i[0], s2))
            else:
                lista.append(i)

        return lista


    def replace_all_sentence(self, vetor):
        lista = []

        for i in vetor:
            s = i[1]

            for (pattern, repl) in self.patterns:
                (s, count) = re.subn(pattern, repl, s)

                if count == 1:
                    break

            if count == 1:
                if ' ' not in s:
                    lista.append((i[0], s))
                else:
                    s1, s2 = s.split(' ')
                    lista.append((i[0], s1))
                    lista.append((i[0], s2))
            else:
                lista.append(i)

        return lista