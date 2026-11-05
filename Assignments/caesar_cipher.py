# AP Ceaser Cypher

message = input("Type the message message you would like to encode: ")

number_value = ord("A")
print(number_value)

def encode(encoding, shift=1):
    """This encodes the message"""
    for char in encoding:
        if char == " " or char == "." or char == ",":
            print(char, end="")
        else:
            letter = char
            letter = letter[0]
            number_value = ord(letter)
            number_value += shift
            if number_value > 122:
                number_value -= 26
            new_letter = chr(number_value)
            print(new_letter, end="")
    print()

def decode(decoding, shift=1):
    """This decodes the message"""
    for char in decoding:
        if char == " " or char == "." or char == ",":
            print(char, end="")
        else:
            letter = char
            letter = letter[0]
            number_value = ord(letter)
            number_value -= shift
            if number_value < 97:
                number_value += 26
            new_letter = chr(number_value)
            print(new_letter, end="")
    print()

encode(message, 5)