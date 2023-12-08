def median(a,b,c):
    if a >= b and a <= c or a >= c and a <= c:
        return a
    if b >= a and b <= c or b <= a and b >= c:
        return b
    if c >= a and c <= b or c <= a and c >= b:
        return c
    
print(median(1,2,3))
print(median(1,3,2))
print(median(7,1,7))         