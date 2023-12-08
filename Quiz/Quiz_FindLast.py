def find_last(a,b):
    posicion = 0
    while True:
        penultimo = a.find(b,posicion) #* Al acabar con el bucle while el valor de esta variable no se actualiza, dando así la última posición de dicho string
        posicion = a.find(b,posicion + 1)
        if posicion == -1:
            break
    return a.find(b,penultimo)

x = 'hola me llamo Aman, como estás Aman, yo bien y tu Aman,aaaaaaaaaaaaaaaa,Aman'
y = 'pene'
z = 'Aman'

print(find_last(x,y))
print(find_last(x,z))