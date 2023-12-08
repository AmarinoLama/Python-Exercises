def isValid(sudoku):
    for row in sudoku:
        if row == []:
            return False
        for number in row:
            if type(number) != int or number > len(sudoku):
                return False
    return True

if __name__ == "__main__":
    import sys
    sys.path.append('..')

    import casosTest.casosTestSudoku as casosTest

    print("Valido?---------------")

    print('correct is', isValid(casosTest.correct))
    print('incorrect is',isValid(casosTest.incorrect))
    print('incorrect1 is',isValid(casosTest.incorrect1))
    print('incorrect2 is',isValid(casosTest.incorrect2))
    print('incorrect3 is',isValid(casosTest.incorrect3))
    print('irregular is',isValid(casosTest.irregular))