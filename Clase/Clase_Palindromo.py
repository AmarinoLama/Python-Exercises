def permute_a_palindrome(input):

    oddCharacter = ""
    for character in input:
        occurence =input.count(character)
        print(character)
        if not oddCharacter and occurence % 2 != 0:
            oddCharacter = character
        elif oddCharacter == character:
            continue
        elif occurence % 2 != 0:
            return False
        else:
            continue
    return True

print(permute_a_palindrome("aman"))