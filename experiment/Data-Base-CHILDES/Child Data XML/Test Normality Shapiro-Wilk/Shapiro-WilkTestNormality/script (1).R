##
## 24/06/2017
##
##
 
## Importar dados
## Antes de importar, verifique se o caminho dos seus arquivo estão corretos.

## Ultilizando read.table()

#belfast <- read.table("~/Estatistica/Shapiro-Wilk Test Normality/csv/word_frequency_canonical_sentence_Belfast_by_commonality.csv", h=T)
#cruttenden <- read.table("~/Estatistica/Shapiro-Wilk Test Normality/csv/word_frequency_canonical_sentence_Cruttenden_by_commonality.csv", h=T)
#manchester <- read.table("~/Estatistica/Shapiro-Wilk Test Normality/csv/word_frequency_canonical_sentence_Manchester_by_commonality.csv", h=T)
#tommerdahl <- read.table("~/Estatistica/Shapiro-Wilk Test Normality/csv/word_frequency_canonical_sentence_Tommerdahl_by_commonality.csv", h=T)

# Ultilizando read.csv()

belfast <- read.csv("~/Estatistica/Shapiro-WilkTestNormality/csv/word_frequency_canonical_sentence_Belfast_by_commonality.csv", sep=";")
cruttenden <- read.csv("~/Estatistica/Shapiro-WilkTestNormality/csv/word_frequency_canonical_sentence_Cruttenden_by_commonality.csv", sep=";")
manchester <- read.csv("~/Estatistica/Shapiro-WilkTestNormality/csv/word_frequency_canonical_sentence_Manchester_by_commonality.csv", sep=";")
tommerdahl <- read.csv("~/Estatistica/Shapiro-WilkTestNormality/csv/word_frequency_canonical_sentence_Tommerdahl_by_commonality.csv", sep=";")

# Visualizar os dados
View(belfast)
View(cruttenden)
View(manchester)
View(tommerdahl)

# Executa o Test Shapiro-Wilk
# Verifica se a amostra pertence a uma população normal.
shapiro.test(belfast$frequency)
shapiro.test(cruttenden$frequency)
shapiro.test(manchester$frequency)
shapiro.test(tommerdahl$frequency)

## Gerar Gráficos
hist(belfast$frequency)
hist(cruttenden$frequency)
hist(manchester$frequency)
hist(tommerdahl$frequency)

plot(belfast$frequency)
plot(cruttenden$frequency)
plot(manchester$frequency)
plot(tommerdahl$frequency)

barplot(belfast$frequency)
barplot(cruttenden$frequency)
barplot(manchester$frequency)
barplot(tommerdahl$frequency)



