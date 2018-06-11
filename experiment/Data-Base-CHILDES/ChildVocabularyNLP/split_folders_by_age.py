import nltk
import csv

from nltk.corpus.reader import CHILDESCorpusReader

corpus_root = nltk.data.find('corpora/CHILDES/data-xml/Eng-UK-MOR/')
reader = CHILDESCorpusReader(corpus_root, '.*.xml')

# TODO: arquivos duplicados

file_age = []

def save_folder_by_age(path, age):
    size = 6
    base = int(age/size)
    with open('Corpus/FolderByAge/' + 'age_' + str(base*size) + '_' + str(((base+1)*size)-1) + '.csv', 'a') as csvfile:
        fieldnames = ['pathInput', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
        writer.writerow({'pathInput': path, 'age': age})

def get_age_in_months(arquivo):
    age = reader.age(arquivo)[0]
    year = 0
    month = 0
    if age != None:
        if age.find('Y'):
            year = int(age[1:age.find('Y')])
        if age.find('M') != -1:
            month = int(age[age.find('Y')+1:age.find('M')])
        return month + (year * 12)
    else:
        return -1



# def save_by_age(path, age):
#
#     # size = 6
#     # base = int(age/size)
#     #
#     # lim_inf = base*size
#     # lim_sup = ((base+1)*size)-1
#     #
#     # cat = str(lim_inf) + '_' + str(lim_sup)
#
#     file_age.append((path, age))



for file in reader.fileids():

    # print(file)
    age = reader.age(file,speaker='CHI', month=True)
    # print(age)

    # tuple_path = file.split('/')
    # print(tuple_path)


    # age = get_age_in_months(file)

    print(age)
    # if age != -1:
    #     save_folder_by_age(file, age)

