def alphabet_position(text):
    import string
    alphabet = string.ascii_lowercase
    lower_text = text.lower()
    only_text = ""
    final_string = ""
    for char in lower_text:
        if char in alphabet:
            only_text += char
        else:
            continue
    for char in only_text:
        position = alphabet.find(char) + 1
        final_string += str(position) + " "
    return final_string[:-1]