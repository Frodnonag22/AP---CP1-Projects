#Andrew Petersen average grade

print("If any questions are not apliccable then put 100. DO NOT PUT THE PERCENTAGE SIGN OR TYPE OUT THE NUMBER")

while True:
    try:
        grade_1 = int(input("What is your grade in your first class? "))
    except:
        print("Thats not a valid number!")
    else:
        break

while True:
    try:
        grade_2 = int(input("What is your grade in your second class? "))
    except:
        print("Thats not a valid number!")
    else:
        break

while True:
    try:
        grade_3 = int(input("What is your grade in your third class? "))
    except:
        print("Thats not a valid number!")
    else:
        break

while True:
    try:
        grade_4 = int(input("What is your grade in your fourth class? "))
    except:
        print("Thats not a valid number!")
    else:
        break

while True:
    try:
        grade_5 = int(input("What is your grade in your fifth class? "))
    except:
        print("Thats not a valid number!")
    else:
        break

while True:
    try:
        grade_6 = int(input("What is your grade in your sixth class? "))
    except:
        print("Thats not a valid number!")
    else:
        break

while True:
    try:
        grade_7 = int(input("What is your grade in your seventh class? "))
    except:
        print("Thats not a valid number!")
    else:
        break

total_grade = grade_1 + grade_2 + grade_3 + grade_4 + grade_5 + grade_6 + grade_7
average_grade = total_grade/7

print("your average grade is:", round(average_grade, 2))