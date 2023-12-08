def encryptor(key, message):
    import string
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    final_string = ""
    for char in message:
        if char in alphabet_lower:
            location = alphabet_lower.find(char)
            final_position = key + location
            while final_position <= -26:
                final_position += 26
            while final_position >= 26: 
                final_position -= 26
            final_string += alphabet_lower[final_position]
        elif char in alphabet_upper:
            location = alphabet_upper.find(char)
            final_position = key + location
            while final_position <= -26:
                final_position += 26
            while final_position >= 26: 
                final_position -= 26
            final_string += alphabet_upper[final_position]
        else:
            final_string += char
    return final_string
# estoy totalmente seguro de que este inmenso código se podría refactorizar
# cuando tenga tiempo libre lo refactorizaré para que sea más legible