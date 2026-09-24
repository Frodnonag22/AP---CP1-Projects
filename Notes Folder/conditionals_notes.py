# Andrew Petersen Conditionals

grade = 67

if grade >= 90:
    print("You have an A, good job")
elif grade >= 80: # Every conditional begins with if
#  ^^^^^^^^^^^^ < boolean statement
    print(f"You have a B, step it up buttercup")
#^^^ always indent after an if, white space is really important.
elif grade >= 70:
    print("you have a C, you've got to be get better")
else:
    print("LOCK IN BUDDY")


raining = False

if raining:
    print("Bring an umbrella")
else:
    print("Wear sunscreen")