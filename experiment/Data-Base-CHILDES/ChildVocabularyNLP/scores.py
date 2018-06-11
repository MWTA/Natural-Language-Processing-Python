#coding=utf-8
import nltk

unique_list = []
word_commonality = []
matrix = []

classeAberta = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']

class Score(object):
    def __init__(self):
        pass

    def commonality(self, vector, firstIndex):
        '''
        :param vector:
        :param firstIndex:
        :return: a vector like (Word, Commonality)
        '''

        list = []
        matrix = []
        unique_list = []
        word_commonality = []

        j = firstIndex
        for i in vector:

            if i[0] == j:
                list.append((i[0], i[1]))
            else:
                matrix.append(list)
                list = [(i[0], i[1])]  # leitura da primeira coisa que não é A. Já coloca na lista
                j = i[0]

        matrix.append(list)

        for list in matrix:
            for tuple in list:
                if tuple[1] not in unique_list:
                    unique_list.append(tuple[1])

        for word in unique_list:
            commonality = 0

            for list in matrix:
                for tuple in list:
                    if word == tuple[1]:
                        commonality += 1
                        break

            posTag = nltk.tag.pos_tag([word])
            if posTag[0][1] in classeAberta:
                word_commonality.append((word, 'J', posTag, 'OpenClass', int(commonality)))
            else:
                word_commonality.append((word, 'J', posTag, 'ClosedClass', int(commonality)))

        return word_commonality

    def frequency_WordPOS(self, vetor):
        '''
        :param vetor: with phrases
        :return: a vector like (Word, POS, Frequency)
        '''

        frase_token_POS = []
        palavras_POS = []
        unique_list = []
        frequency_WPOS = []

        for i in vetor:
            #i = i.replace('.', ' .').replace(',', ' ,')
            frase_token_POS.append(nltk.tag.pos_tag(i))

        for j in frase_token_POS:
            for k in j:
                if k[1] == '.' or k[1] == ',':
                    pass
                else:
                    palavras_POS.append(k)

        unique_listUpper = []
        for i in palavras_POS:
            iUpper = i[0].upper()

            if (iUpper, i[1]) not in unique_listUpper:
                unique_listUpper.append((iUpper, i[1]))
                unique_list.append(i)
            else:
                pass

        for i in unique_list:
            count_WPOS = 0
            for j in palavras_POS:
                if (i[0].upper() == j[0].upper()) & (i[1] == j[1]):
                    count_WPOS += 1
            frequency_WPOS.append((i[0], i[1], count_WPOS))

        return [len(palavras_POS), frequency_WPOS]

    def frequency_word(self, vetor):
        '''
        :param vetor: with phrases
        :return: a vector like (Word, POS, Frequency)
        '''

        phrase_token_pos = []
        all_words = []
        frequency_w = []

        for i in vetor:
            #i = i.replace('.', ' .').replace(',', ' ,')
            phrase_token_pos.append(nltk.tag.pos_tag(i))

        for j in phrase_token_pos:
            for k in j:
                if k[1] == '.' or k[1] == ',':
                    pass
                else:
                    all_words.append(k)
                    # set = {}
                    # map(set.__setitem__, all_words, [])
                    # all_words = set.keys()

        unique_list = []
        unique_list_upper = []

        for i in all_words:
            if i[0].upper() not in unique_list_upper:
                unique_list_upper.append(i[0].upper())
                unique_list.append(i)
            else:
                pass

        for i in unique_list:
            count_w = 0
            for j in all_words:
                if (i[0].upper() == j[0].upper()):
                    count_w += 1
            freq = float(count_w) / len(all_words)
            frequency_w.append((i[0].replace('"', '').replace('[', ''), count_w, float("{0:.4f}".format(freq))))

        return [len(all_words), frequency_w]

    def word_sentence_coverage_by_commonality_pos(self, vetor_commonality, vetor_palavra, len_vetor_palavra):
        '''
        :param vetor_commonality:
        :param vetor_palavra:
        :param len_vetor_palavra:
        :return: a vector like (Word, POS, Commonality, CoverageValue, WordOrder)
        '''

        unique_index = []
        vetor_cobertura_palavra_frase = []

        for i in vetor_commonality:
            if i[1] not in unique_index:
                unique_index.append(i[1])

        unique_index = [int(i) for i in unique_index]
        unique_index.sort(reverse=True)

        word_order = 1
        acumulado = 0
        for i in unique_index:
            for j in vetor_commonality:
                for k in vetor_palavra:
                    if (i == int(j[1])) & (j[0].upper() == k[0].upper()) & (j[2] == k[1]):
                        acumulado += float(k[2])
                        cobertura = acumulado / len_vetor_palavra
                        vetor_cobertura_palavra_frase.append((k[0], k[1], i, cobertura, word_order))
                        word_order += 1

        return (vetor_cobertura_palavra_frase)

    def word_sentence_recall_by_commonality(self, vetor_commonality, vetor_palavra, len_vetor_palavra):
        '''
        :param vetor_commonality:
        :param vetor_palavra:
        :param len_vetor_palavra:
        :return: a vector like (Word, Commonality, CoverageValue, WordOrder)
        '''

        unique_index = []
        vetor_cobertura_palavra_frase = []

        for i in vetor_commonality:
            if i[1] not in unique_index:
                unique_index.append(i[1])

        unique_index = [int(i) for i in unique_index]
        unique_index.sort(reverse=True)

        word_order = 1
        acumulado = 0
        for i in unique_index:
            for j in vetor_commonality:
                for k in vetor_palavra:
                    if (i == int(j[1])) & (j[0].upper() == k[0].upper()):
                        acumulado += float(k[1])
                        cobertura = float(acumulado) / len_vetor_palavra
                        vetor_cobertura_palavra_frase.append((k[0], i, float("{0:.3f}".format(cobertura)), word_order))
                        word_order += 1

        return (vetor_cobertura_palavra_frase)

    def not_recalled_words(self, vector_core_words, unique_words_frequency):

        len_all_words = unique_words_frequency[0]
        vetor_palavra = unique_words_frequency[1]
        core_word = []   # Palavras que não estão em comonalidade
        not_covered = []


        for i in vector_core_words:
            if i[0] not in core_word:
                core_word.append(i[0].upper())

        # for i in word_frequency:
        #     rel = (int(i[1]) * 1000) / int(total_words)
        #     relative_frequency.append((i[0], rel))


        for i in vetor_palavra:
            rel = 0
            if i[0].upper() not in core_word:
                rel = float(i[1]) / len_all_words
                float("{0:.3f}".format(rel))
                not_covered.append((i[0], i[1], float("{0:.3f}".format(rel))))

        return not_covered

    def word_sentence_recall_by_list(self, vetor_core_words, vetor_palavra, len_vetor_palavra):

        # unique_index = []
        vetor_cobertura_palavra_frase = []
        unique_freq = []

        # agrupar vetor_palava - key, quantidade -> frequencia

        vetor_palavra_aux = {}
        for palavra in vetor_palavra:
            key = palavra[0]
            if key not in vetor_palavra_aux:
                vetor_palavra_aux[key] = 0
            vetor_palavra_aux[key] += palavra[1]

        # ordena por frequencia
        for a in vetor_palavra_aux:
            freq = float(vetor_palavra_aux[a])/len_vetor_palavra
            if "{0:.4f}".format(freq) not in unique_freq:
                unique_freq.append("{0:.4f}".format(freq))


        unique_freq.sort(reverse=True)
        # print (unique_freq)

        word_order = 1
        acumulado = 0


        for i in unique_freq:
            for k in vetor_palavra_aux:
                freq_k = "{0:.4f}".format(float(vetor_palavra_aux[k])/len_vetor_palavra)
                if i == freq_k:
                    for j in vetor_core_words:
                        if j[0].upper() == k.upper():
                            acumulado += float(vetor_palavra_aux[k])
                            cobertura = float(acumulado) / len_vetor_palavra
                            frequency = float(vetor_palavra_aux[k])/len_vetor_palavra
                            vetor_cobertura_palavra_frase.append((k, "{0:.4f}".format(frequency), float("{0:.4f}".format(cobertura)), word_order))
                            word_order += 1

        return (vetor_cobertura_palavra_frase)
