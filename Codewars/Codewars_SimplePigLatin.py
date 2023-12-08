def pig_it(text):
    string = ""
    first_letter_word = ""
    text_long = len(text)
    for num in range(text_long):
        if num == 0 or text[num - 1] == " ":
            first_letter_word = text[num]
        elif text[num] == " " or num == text_long: # no sé cómo hacerlo para la última palabra
            string += first_letter_word + "ay "
        else:
            string += text[num]
    final_string = string + first_letter_word + "ay" # en consecuencia de lo anterior le añadí la primera letra y el "ay"
    if text[-1] == "!" or text[-1] == "?": # para cuando acabe en ! o ?
        return final_string[:-2]
    else:
        return final_string