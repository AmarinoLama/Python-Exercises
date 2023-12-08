alphabet =   "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
codificate = "GBCEDFAHKJIUMNPOQYSTLVWXRZgbcedfahkjiumnpoqystlvwxrz"

def encode(message):
    output = ""
    for char in message:
        if char != " ":
            output += codificate[alphabet.find(char)]
        else: 
            output += " "
    return output
    
def decode(message):
    output = ""
    for char in message:
        if char != " ":
            output += alphabet[codificate.find(char)]
        else: 
            output += " "
    return output