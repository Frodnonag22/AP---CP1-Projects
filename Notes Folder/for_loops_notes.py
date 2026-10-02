# AP For Loops Notes
import time

# Iteration going through a collection of items one at a time. 
siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]
     #v iterator variable (i, x, or singular of list name)
for sibling in siblings: # Name of list
    print(f"Good Morning {sibling}")


grades = [100,87, 53, 45, 78, 72, 88, 3, 94]
average = 0

for grade in grades:
    average += grade 
    print(f"{grade} was added.")

average = average/len(grades)
print(f"the average grade is {average:.2f}")

for i in range(2, 21, 2):
    print(i)
    time.sleep(0.5)

for i in range(20, 0, -1):
    print(i)
    time.sleep(0.5)
    if i == 12:
        print("Wait it is lunch time")
        break
