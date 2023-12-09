def esMatrizIdentidad(matriz):

    # comprobar que la matriz sea cuadrada

    numeroFilas = len(matriz)
    for fila in matriz:
        if len(fila) != numeroFilas:
            return False
        
    # comprobar que la diagonal principal sea todo unos
    # comprobar que el resto de numeros de la matriz sean 0 o 1

    for number,position in enumerate(matriz):
            if position[number] != 1:
                return False
            for x in position:
                 if x != 0 and x != 1:
                      return False
    
    # comprobar que la suma de total de la matriz no sea superior al numero a la suma de los 1

    sumaMatriz = 0
    for array in matriz:
         sumaMatriz += sum(array)
    if sumaMatriz == len(matriz) > 1:
         return True
    else: 
         return False

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

matrix5 = [[1,0,0,0,0,0,0,0,0]]

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]

matrix8 = []

print(esMatrizIdentidad(matrix1)) # True
print(esMatrizIdentidad(matrix2)) # False
print(esMatrizIdentidad(matrix3)) # False
print(esMatrizIdentidad(matrix4)) # False
print(esMatrizIdentidad(matrix5)) # False
print(esMatrizIdentidad(matrix6)) # False
print(esMatrizIdentidad(matrix7)) # False
print(esMatrizIdentidad(matrix8)) # False