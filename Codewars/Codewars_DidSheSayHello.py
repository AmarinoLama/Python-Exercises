def validate_hello(greetings):
    lower_greetings = greetings.lower()
    valid_greetings = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    for valid_greeting in valid_greetings:
        if valid_greeting in lower_greetings:
            return True
    return False
