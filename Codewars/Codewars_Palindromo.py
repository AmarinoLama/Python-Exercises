def permute_a_palindrome(word):
    caracteres = len(word)
    if caracteres % 2 == 0 and caracteres >= 2: # el palindromo es par
        posicion = 1
        contador = 0
        acumulador = 0
        while True:
            localizador = word.find(word[contador],posicion)
            posicion = posicion + 1
            contador = contador + 1
            if localizador != -1:
                acumulador = acumulador + 1
            if caracteres == contador:
                num_carac_no_repes = len(set(word))
                if num_carac_no_repes != caracteres / 2:
                    return False
                else:
                    return True
    else: # el palindromo es impar 
        if caracteres > 2:
            posicion = 1
            contador = 0
            acumulador = 0
            while True:
                localizador = word.find(word[contador],posicion)
                posicion = posicion + 1
                contador = contador + 1
                if localizador != -1:
                    acumulador = acumulador + 1
                if caracteres == contador:
                    num_carac_no_repes = len(set(word))
                    if num_carac_no_repes - 1 != caracteres // 2:
                        return False
                    else:
                        return True
        else:
            return True