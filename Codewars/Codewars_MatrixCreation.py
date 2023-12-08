def get_matrix(n):
    finalArray = [[0 for x in range(n)] for x in range(n)]
    for x in range(n):
        finalArray[x][x] = 1
    return finalArray
        