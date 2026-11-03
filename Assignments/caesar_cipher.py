# AP Ceaser Cypher

message = input("Type the message message you would like to encode: ").lower()

letters = "0abcdefghijklmnopqrstuvwxyz"

def forward(name="hello world", shift=1):
    for char in name:
        number = letters.find(char)
        if number == -1:
            print(" ", end=" ")
        else:
            number += shift
            print(number, end=" ")


forward(message, 0)