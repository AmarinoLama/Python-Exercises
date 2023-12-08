def factorial(a):
    result = 1
    while a != 0:
        result = result * a
        a = a - 1
    return result

print(factorial(4))