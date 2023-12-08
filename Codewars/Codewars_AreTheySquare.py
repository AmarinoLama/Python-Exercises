def is_square(arr):
    import math
    if arr == []:
        return None
    for number in arr:
        if math.sqrt(number) % 1 != 0:
            return False
    return True