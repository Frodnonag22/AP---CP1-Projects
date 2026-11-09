# AP Ceaser Cypher

while True:
    user_choice = input("Would you like to encode or decode a message: ").lower().strip()
    user_message = input("What is the message: ").strip()
    while True:
        try:
            user_shift = int(input("What numerical value does it need to be shifted by: "))
            if user_shift < 1 or user_shift > 26:
                print("Number must be between 1 and 26")
                continue
            break
        except:
            print("Invalid input, try again")

    def encode(encoding, shift=1):
        """This encodes the message"""
        encoded = ""
        for char in encoding:
            if char.isalpha():
                letter = char
                letter = letter[0]
                number_value = ord(letter)
                number_value += shift
                if char.isupper():
                    if number_value > 90:
                        number_value -= 26
                    new_letter = chr(number_value)
                    encoded += new_letter
                else:
                    if number_value > 122:
                        number_value -= 26
                    new_letter = chr(number_value)
                    encoded += new_letter
            else: 
                encoded += char
        return encoded

    def decode(decoding, shift=1):
        """This decodes the message"""
        decoded = ""
        for char in decoding:
            if char.isalpha():
                letter = char
                letter = letter[0]
                number_value = ord(letter)
                number_value -= shift
                if char.isupper():
                    if number_value < 65:
                        number_value += 26
                    new_letter = chr(number_value)
                    decoded += new_letter
                else:
                    if number_value < 97:
                        number_value += 26
                    new_letter = chr(number_value)
                    decoded += new_letter
            else: 
                decoded += char
        return decoded

    if "enc" in user_choice:
        print(f"Encoded message is: {encode(user_message, user_shift)}")
    elif "dec" in user_choice:
        print(f"Decoded message is: {decode(user_message, user_shift)}")
    else:
        print("Why didn't you select to change a message?")
    
    play_again = input("Would you like to change another message?")
    if "ye" in play_again:
        pass
    else:
        break