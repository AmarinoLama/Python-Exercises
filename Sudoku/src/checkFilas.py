def checkRow(sudoku):
    for row in sudoku:
        rep_numbers = []
        for number in row:
            if number in rep_numbers:
                return False
            rep_numbers.append(number)
    return True   

if __name__ == "__main__":
    import sys
    sys.path.append('..')

    import casosTest.casosTestSudoku as casosTest

    print("Filas?---------------")

    print('correct is', checkRow(casosTest.correct))
    print('incorrect is',checkRow(casosTest.incorrect))
    print('incorrect1 is',checkRow(casosTest.incorrect1))
    print('incorrect2 is',checkRow(casosTest.incorrect2))
    print('incorrect3 is',checkRow(casosTest.incorrect3))
    print('irregular is',checkRow(casosTest.irregular))