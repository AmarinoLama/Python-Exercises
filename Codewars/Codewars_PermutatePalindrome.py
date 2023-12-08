def permute_a_palindrome(word):
    contador_de_impares = 0
    caracter_en_el_que_estamos = 0
    impares = ""
    while caracter_en_el_que_estamos != len(word): 
        if word.count(word[caracter_en_el_que_estamos]) % 2 == 1 and word[caracter_en_el_que_estamos] not in impares:
            contador_de_impares += 1
            impares += word[caracter_en_el_que_estamos]
        caracter_en_el_que_estamos += 1
    return contador_de_impares < 2