def is_friend(a): #Mi solucion
    x = a.find("D")
    if x>0:
        return True
    else:
        return False

print(is_friend('Dylan'))
print(is_friend('Aman'))

def is_friend(a): #Solucion del video
    if a[0] == "D":
        return True
    else:
        return False

print(is_friend('Dylan'))
print(is_friend('Aman'))