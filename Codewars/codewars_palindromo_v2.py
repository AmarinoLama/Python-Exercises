def permute_a_palindrome(input):
    contador_de_impares = 0
    caracter_en_el_que_estamos = 0
    impares = ""
    while caracter_en_el_que_estamos != len(input): 
        if input.count(input[caracter_en_el_que_estamos]) % 2 == 1 and input[caracter_en_el_que_estamos] not in impares:
            contador_de_impares += 1
            impares += input[caracter_en_el_que_estamos]
        caracter_en_el_que_estamos += 1
    return contador_de_impares < 2