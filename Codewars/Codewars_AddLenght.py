def add_length(str_):
    words = str_.split()
    output = []
    for word in words:
        output.append(word + " " + str(len(word)))
    return output