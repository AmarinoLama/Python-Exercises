def biggest(a,b,c):
    if a > b and a > c:
        return a
    else: 
        if b > c:
            return b
        else:
            return c
        
print(biggest(1,2,5))
print(biggest(1,7,2))
print(biggest(6,2,1))