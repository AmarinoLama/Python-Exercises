# sube de carpeta
import sys
sys.path.append('..')

from src.checkColumnas import checkColumn
from src.checkCuadrado import isSquare
from src.checkFilas import checkRow
from src.checkNumValido import isValid



def checkSudoku(sudoku): 
    return isSquare(sudoku) and isValid(sudoku) and checkRow(sudoku) and checkColumn(sudoku)

if __name__ == "__main__":

    import sys
    sys.path.append('..')

    import casosTest.casosTestSudoku as casosTest

    print("SUDOKU?---------------")

    print('correct is', checkSudoku(casosTest.correct))
    print('incorrect is',checkSudoku(casosTest.incorrect))
    print('incorrect1 is',checkSudoku(casosTest.incorrect1))
    print('incorrect2 is',checkSudoku(casosTest.incorrect2))
    print('incorrect3 is',checkSudoku(casosTest.incorrect3))
    print('irregular is',checkSudoku(casosTest.irregular))