def disemvowel(string_):
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    texto_sin_vocales = ""
    for character in string_:
        if character not in vocales:
            texto_sin_vocales += character
    return texto_sin_vocales