def stock_list(library,letters):

    shortedBooks = dict.fromkeys(letters,0)
    finalString = ""
    
    if library == [] or letters == []:
        return finalString

    for char in letters:
        for book in library:
            # separa el string en espacios y corta lo último y lo guarda (el número)
            numbers = int(book.split(' ')[-1]) 
            if book[0] == char:
                shortedBooks[char] += numbers
    
    # lo de abajo estaría mejor en otra función en otro fichero

    for position in shortedBooks:
        finalString += "(" + position + " : " + str(shortedBooks[position]) + ") - "

    return finalString[:-3]

if __name__ == "__main__":

    # Test Prueba

    b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B", "C", "D"]
    assert stock_list(b, c) == "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"