import random
from perceiver import bytes_tokenizer

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
    #retourne la liste des mots masqués et leurs indices dans la liste des mots
    return maskedwords, maskedwordsIndexesInData



def findIndexes(str, maskedwordsIndexesInData):
    # Trouve les index des mots à cacher dans la chaîne
    maskedwordsIndexesInStr = []
    wordIndex = 0
    for i in range(len(str)):
        if str[i] == ' ':
            wordIndex += 1
            if wordIndex in maskedwordsIndexesInData:
                maskedwordsIndexesInStr.append(i)
        if wordIndex in maskedwordsIndexesInData and i + 1 < len(str):
            if str[i+1] == ' ':
                maskedwordsIndexesInStr.append(i+1)
            elif i == 0:
                maskedwordsIndexesInStr.append(i)
        if wordIndex in maskedwordsIndexesInData and i + 1 == len(str):
            maskedwordsIndexesInStr.append(i+1)
    #retourne les indices de début et de fin de chaque mot masqué
    return maskedwordsIndexesInStr


def stringWithMaskedWords(str, maskedwordsIndexesInStr):
    #définit la chaîne avec mots masqués
    tokenizer = bytes_tokenizer.BytesTokenizer()
    input_tokens = tokenizer.to_int(str)
    even_number_of_masked_words_indexes_in_str = len(maskedwordsIndexesInStr) - len(maskedwordsIndexesInStr) % 2
    for masked_word_index in range(0, even_number_of_masked_words_indexes_in_str, 2):
        input_tokens[maskedwordsIndexesInStr[masked_word_index]:maskedwordsIndexesInStr[masked_word_index+1]] = tokenizer.mask_token
    #retourne la chaîne en masquant les mots choisis
    return tokenizer.to_string(input_tokens)

'''
def stringWithNewWords(realStr, foundStr, maskedwordsIndexesInStr):
    #fournit la chaine avec les mots trouvés
    even_number_of_masked_words_indexes_in_str = len(maskedwordsIndexesInStr) - len(maskedwordsIndexesInStr) % 2
    for masked_word_index in range(0, even_number_of_masked_words_indexes_in_str, 2):
    
    
def succed(maskedWordsInRealStr, maskedWordsInFoundStr)

'''
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