def isSquare(sudoku):
    for row in sudoku:
        if len(sudoku) != len(row):
            return False
    return True

if __name__ == "__main__":
    import sys
    sys.path.append('..')

    import casosTest.casosTestSudoku as casosTest

    print("COLUMNA?---------------")

    print('correct is', isSquare(casosTest.correct))
    print('incorrect is',isSquare(casosTest.incorrect))
    print('incorrect1 is',isSquare(casosTest.incorrect1))
    print('incorrect2 is',isSquare(casosTest.incorrect2))
    print('incorrect3 is',isSquare(casosTest.incorrect3))
    print('irregular is',isSquare(casosTest.irregular))