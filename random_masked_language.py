import random
from perceiver import bytes_tokenizer as bt

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
            if str[i+1] == ' ' and i == 0:
                maskedwordsIndexesInStr.append(i)
            if str[i+1] == ' ':
                maskedwordsIndexesInStr.append(i+1)
            elif i == 0:
                maskedwordsIndexesInStr.append(i)
        if wordIndex in maskedwordsIndexesInData and i + 1 == len(str):
            maskedwordsIndexesInStr.append(i+1)
    #retourne les indices de début et de fin de chaque mot masqué
    return maskedwordsIndexesInStr


def inputWithMaskedWords(str, maskedwordsIndexesInStr):
    #définit la chaîne avec mots masqués
    tokenizer = bt.BytesTokenizer()
    input_tokens = tokenizer.to_int(str)
    even_len_maskedwordsIndexesInStr = len(maskedwordsIndexesInStr) - len(maskedwordsIndexesInStr) % 2 #"corrige" l'ANOMALIE de analysis.ipynb
    for masked_word_index in range(0, even_len_maskedwordsIndexesInStr, 2):
        input_tokens[maskedwordsIndexesInStr[masked_word_index]:maskedwordsIndexesInStr[masked_word_index+1]] = tokenizer.mask_token
    #retourne la chaîne en masquant les mots choisis
    return input_tokens


def stringWithMaskedWords(str, maskedwordsIndexesInStr):
    return bt.BytesTokenizer().to_string(inputWithMaskedWords(str, maskedwordsIndexesInStr))


def extractWordsByIndexes(str, words_indexes_in_str):
    extracted_words = []
    even_len_words_indexes_in_str = len(words_indexes_in_str) - len(words_indexes_in_str) % 2 #"corrige" l'ANOMALIE de analysis.ipynb
    for index_even_iterator in range(0, even_len_words_indexes_in_str, 2):
        extracted_words.append(
            str[words_indexes_in_str[index_even_iterator]:words_indexes_in_str[index_even_iterator + 1]]
        )
    return extracted_words


def stringWithNewWords(real_str, found_str, words_indexes_in_str):
    #fournit la chaine avec les mots trouvés
    #les Strings sont immuables, donc on utilise une version de found_str sous forme de liste pour la modifier
    predicted_str = list(found_str[:len(real_str)])     #apres len(real_str), il n'y a que des 0
    range_for_overwriting = [i for i in range(0,len(predicted_str))]    #les indices des caracteres a ecraser

    even_len_words_indexes_in_str = len(words_indexes_in_str) - len(words_indexes_in_str) % 2 #"corrige" l'ANOMALIE de analysis.ipynb
    for index_even_iterator in range(0, even_len_words_indexes_in_str, 2):
        #on elimine tous les indexes des caracteres qui ne constituent pas les mots devines
        for index_to_delete in range(words_indexes_in_str[index_even_iterator], words_indexes_in_str[index_even_iterator + 1]):
            range_for_overwriting.remove(index_to_delete)

    #on ecrase tous les caracteres qui ne constituent pas les mots devines par ceux de la String originale
    for iterator_for_overwriting in range_for_overwriting:
        predicted_str[iterator_for_overwriting] = real_str[iterator_for_overwriting]

    #on reconstitue une String a partir de la liste de caracteres
    predicted_str = "".join(predicted_str)
    return predicted_str


def computeEfficiency(real_str, found_str, words_indexes_in_str):
    efficiency = 0.0

    even_len_words_indexes_in_str = len(words_indexes_in_str) - len(words_indexes_in_str) % 2 #"corrige" l'ANOMALIE de analysis.ipynb
    for index_even_iterator in range(0, even_len_words_indexes_in_str, 2):
        if real_str[words_indexes_in_str[index_even_iterator]:words_indexes_in_str[index_even_iterator + 1]] \
                == found_str[words_indexes_in_str[index_even_iterator]:words_indexes_in_str[index_even_iterator + 1]]:
            efficiency += 1

    number_of_words = len(words_indexes_in_str) / 2
    if number_of_words:
        efficiency /= number_of_words
    else:
        efficiency = None
    return efficiency


"""
def main(str, maskPercentage):
    print("chaine saisie :",str)
    print("pourcentage saisi : ", maskPercentage)
    maskedWords, maskedwordsIndexesInData = chooseMaskedWords(str, maskPercentage)
    print("mots a masquer : ", maskedWords)
    maskedwordsIndexesInStr = findIndexes(str, maskedwordsIndexesInData)
    maskedString = stringWithMaskedWords(str, maskedwordsIndexesInStr)
    print("chaine avec mots masques : ",maskedString)
    print(maskedwordsIndexesInStr)

# Données qui pourront à l'avenir être saisies par l'utilisateur
maskPercentage = 100  # doit être positif et inferieur a 100
str = "I wanted to share it with you."

main(str, maskPercentage)
"""
