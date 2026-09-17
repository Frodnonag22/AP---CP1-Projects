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
numbers_for_password = random.randint(0, 1000)
numbers = str(numbers_for_password)

letter_1 = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
random_letter_1 = letter_1[letter_one: letter_one + 1]
letter_2 = " abcdefghijklmnopqrstuvwxyz"
random_letter_2 = letter_2[letter_two: letter_two + 1]
letter_3 = " abcdefghijklmnopqrstuvwxyz"
random_letter_3 = letter_3[letter_three: letter_three + 1]
letter_4 = " abcdefghijklmnopqrstuvwxyz"
random_letter_4 = letter_4[letter_four: letter_four + 1]
letter_5 = " abcdefghijklmnopqrstuvwxyz"
random_letter_5 = letter_5[letter_five: letter_five + 1]
letter_6 = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
random_letter_6 = letter_6[letter_six: letter_six + 1]
letter_7 = " abcdefghijklmnopqrstuvwxyz"
random_letter_7 = letter_7[letter_seven: letter_seven + 1]
letter_8 = " abcdefghijklmnopqrstuvwxyz"
random_letter_8 = letter_8[letter_eight: letter_eight + 1]
letter_9 = " abcdefghijklmnopqrstuvwxyz"
random_letter_9 = letter_9[letter_nine: letter_nine + 1]
letter_10 = " abcdefghijklmnopqrstuvwxyz"
random_letter_10 = letter_10[letter_ten: letter_ten + 1]
letter_11 = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
random_letter_11 = letter_11[letter_eleven: letter_eleven + 1]

generated_password = f"{random_letter_1}{random_letter_2}{random_letter_3}{random_letter_4}{random_letter_5}{random_letter_6}{random_letter_7}{random_letter_8}{random_letter_9}{random_letter_10}{random_letter_11}{numbers}"

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
    if lol < 2:
        play_game = False
    elif lol == 2:
        print("OOH SOO CLOSE")
    else:
        play_game = True