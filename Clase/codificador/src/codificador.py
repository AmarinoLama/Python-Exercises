def codificador(frase):
    stringFinal = ""
    for caracter in frase:
        if frase.count(caracter) > 1:
            stringFinal += "("
        else:
            stringFinal += ")"
    return stringFinal