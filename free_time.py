#Andrew Petersen Free time

import random

letter_one = random.randint(1, 26)
letter_two = random.randint(1, 26)
letter_three = random.randint(1, 26)
letter_four = random.randint(1, 26)
letter_five = random.randint(1, 26)
letter_six = random.randint(1, 26)
letter_seven = random.randint(1, 26)
letter_eight = random.randint(1, 26)
letter_nine = random.randint(1, 26)
letter_ten = random.randint(1, 26)
letter_eleven = random.randint(1, 26)
numbers_for_password = random.randint(0, 2000)

upper_alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_alpha = " abcdefghijklmnopqrstuvwxyz"

letter_1 = upper_alpha[letter_one: letter_one + 1]
letter_2 = lower_alpha[letter_two: letter_two + 1]
letter_3 = lower_alpha[letter_three: letter_three + 1]
letter_4 = lower_alpha[letter_four: letter_four + 1]
letter_5 = lower_alpha[letter_five: letter_five + 1]
letter_6 = upper_alpha[letter_six: letter_six + 1]
letter_7 = lower_alpha[letter_seven: letter_seven + 1]
letter_8 = lower_alpha[letter_eight: letter_eight + 1]
letter_9 = lower_alpha[letter_nine: letter_nine + 1]
letter_10 = lower_alpha[letter_ten: letter_ten + 1]
letter_11 = upper_alpha[letter_eleven: letter_eleven + 1]
numbers = str(numbers_for_password)

generated_password = f"{letter_1}{letter_2}{letter_3}{letter_4}{letter_5}{letter_6}{letter_7}{letter_8}{letter_9}{letter_10}{letter_11}{numbers}"

print(generated_password)

inputted_password = input(f"What is the password: ")

if inputted_password == generated_password:
    print(f"Correct password, now you have access to the rest of the program!")
    play_game = True
else:
    play_game = False

while play_game == True:
    print(f"sdfasdf")
    lol = random.randint(1, 100)
    if lol == 1:
        play_game = False
    elif lol == 2:
        print("OOH SOO CLOSE")
    else:
        play_game = True