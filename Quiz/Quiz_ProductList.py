def product_list(array):
    result = 1
    for position in array:
        result = position * result
    return result

print(product_list([1,2,3]))
print(product_list([]))