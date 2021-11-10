import random
import bytes_tokenizer

# Objectif : masquer un pourcentage de mots spécifique aléatoirement.


def chooseMaskedWords(str, maskPercentage):
    # Choisit les mots a masquer selon le pourcentage definit
    data = str.split()
    maskedwords = []
    maskedwordsIndexesInData = []
    for word in range(len(data)):
        generatedNumber = random.randint(0, 100)
        if generatedNumber <= maskPercentage:
            maskedwords.append(data[word])
            maskedwordsIndexesInData.append(word)
    return maskedwords, maskedwordsIndexesInData


def findIndexes(str, maskedwordsIndexesInData):
    # Trouve les index des mots à cacher dans la chaîne
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
    return maskedwordsIndexesInStr


def stringWithMaskedWords(str, maskedwordsIndexesInStr):
    #définit la chaîne avec mots masqués
    tokenizer = bytes_tokenizer.BytesTokenizer()
    input_tokens = tokenizer.to_int(str)
    for i in range(2, len(maskedwordsIndexesInStr)):
        if i % 2 == 0:
            input_tokens[maskedwordsIndexesInStr[i]:maskedwordsIndexesInStr[i+1]] = tokenizer.mask_token
    return input_tokens

'''
def main(str, maskPercentage):
    print("chaine saisie :",str)
    print("pourcentage saisi : ", maskPercentage)
    maskedWords, maskedwordsIndexesInData = chooseMaskedWords(str, maskPercentage)
    print("mots a masquer : ", maskedWords)
    maskedwordsIndexesInStr = findIndexes(str, maskedwordsIndexesInData)
    maskedString = stringWithMaskedWords(str, maskedwordsIndexesInStr)
    print("chaine avec mots masques : ",maskedString)


# Données qui pourront à l'avenir être saisies par l'utilisateur
maskPercentage = 20  # doit être positif et inferieur a 100
str = "This is the best thing that happened to me. I wanted to share it with you."

main(str, maskPercentage)
'''