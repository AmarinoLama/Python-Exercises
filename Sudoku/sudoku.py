from src.checkSudoku import checkSudoku
import casosTest.casosTestSudoku as casosTest

print("RAIZ")
print(checkSudoku(casosTest.correct))
print(checkSudoku(casosTest.incorrect1))
print(checkSudoku(casosTest.incorrect2))
print(checkSudoku(casosTest.incorrect3))
print(checkSudoku(casosTest.incorrect4))
print(checkSudoku(casosTest.incorrect5))