def switcher(arr):
    alphabet = "zyxwvutsrqponmlkjihgfedcba!? "
    output = ""
    for num in arr:
        output += alphabet[int(num)-1]
    return output
        
    