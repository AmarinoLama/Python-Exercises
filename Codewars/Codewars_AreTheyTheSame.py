def comp(array1, array2):
    if (array1 == None or array2 == None) or len(array1) != len(array2):
        return False
    array1 = [abs(x) for x in array1]
    array1.sort()
    array2.sort()
    isTheSame = dict(zip(array1,array2))
    for position in isTheSame:
        if position**2 != isTheSame[position]:
            print(isTheSame)
            return False
    return True