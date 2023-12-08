# primero va el nombre del archivo y luego lo que quieres traer de el
from isSquare import isSquare

def isValid(sudoku):
    for row in sudoku:
        if row == []:
            return False
        for number in row:
            if type(number) != int or number > len(sudoku):
                return False
    return True

def checkRow(sudoku):
    for row in sudoku:
        rep_numbers = []
        for number in row:
            if number in rep_numbers:
                return False
            rep_numbers.append(number)
    return True        

def checkColumn (sudoku):
    if isValid(sudoku) == False:  # si el caso test de irregular lelga aqui da error, pero con el checkSudoku no llega entonces no da error ;)
        return False
    transpuesta = [[0]* len(sudoku) for row in sudoku]
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            transpuesta[j][i] = sudoku[i][j]

    for row in transpuesta:
        rep_numbers = []
        for number in row:
            if number in rep_numbers:
                return False
            rep_numbers.append(number)
    return True     
    

def checkSudoku (sudoku): 
    return isSquare(sudoku) and isValid(sudoku) and checkRow(sudoku) and checkColumn(sudoku)


if __name__ == '__main__':
    
    correct = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]
    
    incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 2]]
    
    incorrect1 = [[1, 2, 3],
              [2, 3, 1],
              [2, 3, 1]]
    
    incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 2],
              [4, 1, 2, 3],
              [2, 3, 1, 4]]
    
    incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]
    
    incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

    incorrect5 = [[1, 1.5],
              [1.5, 1]]

    irregular = [[1, 2, 3],
             [2, 3, 1]]

    irregular2 = [[1, 2, 3],
              [2, 3, 1],
              [3, 1]]
    nuevo = [[]]

    print("CUADRADO?---------------")

    # test si son cuadrado
    print('correct is', isSquare(correct))
    print('incorrect is',isSquare(incorrect))
    print('incorrect1 is',isSquare(incorrect1))
    print('incorrect2 is',isSquare(incorrect2))
    print('incorrect3 is',isSquare(incorrect3))
    print('irregular is',isSquare(irregular))

    print("VALIDO?---------------")

    # test si son validos
    print('correct is', isValid(correct))
    print('incorrect is',isValid(incorrect))
    print('incorrect1 is',isValid(incorrect1))
    print('incorrect2 is',isValid(incorrect2))
    print('incorrect3 is',isValid(incorrect3))
    print('irregular is',isValid(irregular))

    print("FILAS?---------------")

    # test que chequea las filas
    print('correct is', checkRow(correct))
    print('incorrect is',checkRow(incorrect))
    print('incorrect1 is',checkRow(incorrect1))
    print('incorrect2 is',checkRow(incorrect2))
    print('incorrect3 is',checkRow(incorrect3))
    print('irregular is',checkRow(irregular))

    print("COLUMNAS?---------------")

    # test que chequea las columnas
    print('correct is', checkColumn(correct))
    print('incorrect is',checkColumn(incorrect))
    print('incorrect1 is',checkColumn(incorrect1))
    print('incorrect2 is',checkColumn(incorrect2))
    print('incorrect3 is',checkColumn(incorrect3))
    print('irregular is',checkColumn(irregular))

    print("SUDOKU?---------------")

    # test que chequea todo
    print('correct is', checkSudoku(correct))
    print('incorrect is',checkSudoku(incorrect))
    print('incorrect1 is',checkSudoku(incorrect1))
    print('incorrect2 is',checkSudoku(incorrect2))
    print('incorrect3 is',checkSudoku(incorrect3))
    print('irregular is',checkSudoku(irregular))