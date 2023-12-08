def checkColumn(sudoku):
    traspuesta = [[sudoku[i][j] for i in range(len(sudoku))] for j in range(len(sudoku[0]))]
    for fila in traspuesta:
        for i, numero in enumerate(fila):
            if numero in fila[i + 1:]:
                return False
    return True

if __name__ == '__main__':
    import sys
    sys.path.append('..')

    import casosTest.casosTestSudoku as casosTest

    print("desde check column")
    print(checkColumn(casosTest.correct))
    print(checkColumn(casosTest.incorrect1))
    print(checkColumn(casosTest.incorrect2))
    print(checkColumn(casosTest.incorrect3))
    print(checkColumn(casosTest.incorrect4))
    print(checkColumn(casosTest.incorrect5))