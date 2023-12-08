def gimme_the_letters(sp):
    import string
    abecedario_lower = string.ascii_lowercase
    abecedario_upper = string.ascii_uppercase
    if sp[0] in abecedario_lower:
        posicion_inicial = abecedario_lower.find(sp[0])
        posicion_final = abecedario_lower.find(sp[2])
        return abecedario_lower[posicion_inicial:posicion_final + 1]
    else:
        posicion_inicial = abecedario_upper.find(sp[0])
        posicion_final = abecedario_upper.find(sp[2])
        return abecedario_upper[posicion_inicial:posicion_final + 1]