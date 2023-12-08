def show_sequence(n):
    if n > 0:
        array = [i for i in range(n+1)]
        output = ""
        for num in array:
            output += str(num) + "+"
        return output[:-1] + " = " + str(sum(array))
    elif n == 0:
        return "0=0"
    else:
        return str(n) + "<0"