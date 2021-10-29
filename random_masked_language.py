import random

# Objectif : masquer un pourcentage de mots spécifique aléatoirement.

# Données qui pourront à l'avenir être saisies par l'utilisateur

maskPercentage = 20 # doit être positif et inferieur a 100
str = "This is the best thing that happened to me. I wanted to share it with you."
data = str.split()
maskedwords = []
maskedwordsIndexesInData = []
print(data)
for word in range(len(data)):
    generatedNumber = random.randint(0, 100)
    if generatedNumber <= maskPercentage:
        maskedwords.append(data[word])
        maskedwordsIndexesInData.append(word)
print(maskedwords)
print(maskedwordsIndexesInData)
# Objectif : trouver les index des masked words (début et fin) et afficher la masked string

maskedwordsIndexesInStr = []
wordIndex = 0
for i in range(len(str)):
    if str[i] == ' ':
        wordIndex+=1
        if wordIndex in maskedwordsIndexesInData:
            maskedwordsIndexesInStr.append(i)
    if wordIndex in maskedwordsIndexesInData and i + 1 < len(str):
        if str[i+1] == ' ':
            maskedwordsIndexesInStr.append(i+1)
        elif i == 0:
            maskedwordsIndexesInStr.append(i)
    if wordIndex in maskedwordsIndexesInData and i + 1 == len(str):
        maskedwordsIndexesInStr.append(i+1)

print(maskedwordsIndexesInStr) # les indices dans str des mots à masquer (début mot1, fin mot2, débutmot2 ...)
