def stock_list(library,letters):

    shortedBooks = dict(zip(letters,[0 for x in range(len(letters))]))
    finalString = ""
    
    if library == [] or letters == []:
        return finalString

    for char in letters:
        for book in library:
            for searchNumber in book:
                if searchNumber in "0123456789":
                    firstNumber = book.find(searchNumber)
                    break
            if book[0] == char:
                shortedBooks[char] += int(book[firstNumber:])
    
    for position in shortedBooks:
        finalString += "(" + position + " : " + str(shortedBooks[position]) + ") - "

    return finalString[:-3]