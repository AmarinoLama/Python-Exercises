def esAntisimetrica(matriz):
    numeroFilas = len(matriz)
    for fila in matriz:
        if len(fila) != numeroFilas:
            return False
    LadoDerecho = []
    LadoIzquierdo = []
    if matriz != []:
        for number,position in enumerate(matriz):
            if position[number] != 0:
                return False
            for x in position:
                if x > 0:
                    LadoDerecho.append(x)
                elif x < 0:
                    LadoIzquierdo.append(x)
    else:
        return False
    for x in range(len(LadoIzquierdo)):
        if LadoIzquierdo[x] + LadoDerecho[x] != 0:
            return False
    return True

# True
print(esAntisimetrica([[0, 1, 2,], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])) 
# True
print(esAntisimetrica([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
# False
print(esAntisimetrica([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]]))
# False
print(esAntisimetrica([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
# False
print(esAntisimetrica([[1,0,0,0],
                    [0,1,1,0],
                    [0,0,0,1]]))
# False
print(esAntisimetrica([[1,0,0,0,0,0,0,0,0]]))

#False
print(esAntisimetrica([]))

# Ns pq falla con matrices 4*4
#* Si le doy la vuelta cuando busque los números de la izquierda funcionará
print(esAntisimetrica([[0,1,2,3],
                      [-1,0,4,5],
                      [-2,-4,0,6],
                      [-3,-5,-6,0]]))

#! PROGRAMA QUE FUNCIONA CON MATRICES 4*4, menores y mayores (hecho por chatgtp)

def esAntisimetrica2(matriz):
    numeroFilas = len(matriz)
    
    # Verifica si la matriz es cuadrada (tiene el mismo número de filas y columnas)
    for fila in matriz:
        if len(fila) != numeroFilas:
            return False

    # Verifica si la matriz es antisimétrica
    for i in range(numeroFilas):
        for j in range(numeroFilas):
            if matriz[i][j] != -matriz[j][i]:
                return False

    return True