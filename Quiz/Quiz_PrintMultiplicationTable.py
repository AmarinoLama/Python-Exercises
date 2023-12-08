def print_multiplication_table(a):
    contador = [0,0]
    while True:
        contador[1] = 0
        contador[0] = contador[0] + 1
        while True:
            contador[1] = contador[1] + 1
            resultado = contador[0] * contador[1]
            print('{} * {} = {}'.format(contador[0],contador[1],resultado))
            if a <= contador[1]:
                break
        if a <= contador[0]:
            break

print(print_multiplication_table(3))