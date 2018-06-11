from posTag import POSTagger

tagger = POSTagger()

vetor = [('A','fish'), ('A', 'will'), ('A', 'was')]

print(tagger.canonicalTag(vetor))