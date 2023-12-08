def get_count(sentence):
    vocales = ["a","e","i","o","u"]
    contador = 0
    for character in sentence:
        character=character.lower()
        if character in vocales:
            contador += 1
    return contador
        