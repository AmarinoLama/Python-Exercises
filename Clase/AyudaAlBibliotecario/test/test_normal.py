from src.stock_list import stock_list

def test_prueba():
    b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B", "C", "D"]
    assert stock_list(b, c) == "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"

def test_dos():
    b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B"]
    assert stock_list(b, c) == "(A : 200) - (B : 1140)"

def test_vacioUno():
    b = []
    c = ["A", "B"]
    assert stock_list(b, c) == ""

def test_vacioDos():
    b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = []
    assert stock_list(b, c) == ""

def test_MasDeCuatro():
    b = ["BBARA 150", "ACDXE 515", "BCKWR 250", "DTSAQ 890", "ADRTY 600"]
    c = ["A", "B", "C", "D"]
    assert stock_list(b,c) == "(A : 1115) - (B : 400) - (C : 0) - (D : 890)"

# seperar esto en varios archivos