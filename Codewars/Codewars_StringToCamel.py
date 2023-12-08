def to_camel_case(text):
    if len(text) > 1:
        mayusculas = text[1] + text.title()[2:]
        casi_arreglado = text[0] + mayusculas
        return casi_arreglado.replace("-", "").replace("_", "")
    else:
        return ""