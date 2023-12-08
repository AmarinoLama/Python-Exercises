def comp(array1, array2):
    return array1 != None and array2 != None and sorted([number**2 for number in array1]) == sorted(array2)