# AP Ceaser Cypher

message = input("Type the message message you would like to encode: ").lower()

letters = "0abcdefghijklmnopqrstuvwxyz"

def encode(message="hello world", shift=1):
    """This encodes the message"""
    for char in message:
        number = letters.find(char)
        if number == -1:
            print(" ", end=" ")
        else:
            number += shift
            if number > 26:
                number -= 26
    


encode(message, 5)