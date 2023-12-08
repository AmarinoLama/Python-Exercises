def duplicate_encode(string):
    string = string.lower()
    dictionary = {x: string.count(x) for x in string}
    finalString = ""
    for char in string:
        if dictionary[char] != 1:
            finalString += ")"
        else:
            finalString += "("
    return finalString