#Andrew Petersen Idiot Proof

first_name = input("What is your first name: ").strip().title()
last_name = input("What is your last name: ").strip().title()
while True:
    try:
        phone_number = int(input("What is your phone number (no spaces or dashes please): "))
    except:
        print("Thats not a valid phone number, try again")
    else:
        break

while True:
    try:
        gpa = float(input("What is your GPA: "))
    except:
        print("Thats not a valid GPA, try again")
    else:
        break

first_separated = first_name.split()
first_fixed = "".join(first_separated)
last_separated = last_name.split() 
last_fixed = "".join(last_separated)

full_name = first_fixed.title() + " " + last_fixed.title()

string_phone = str(phone_number)


print(f"Your name is {full_name}")
print(f"Your phone number is {string_phone[0: 3]} {string_phone[3: 6]} {string_phone[6: 10]}")
print(f"Your GPA is {round(gpa, 1)}")