# AP Factorial Calculator
import math

def times(number):
    return number
# Max is 1558

while True:
    while True:
        try:
            fac_number = int(input("What number do you want to factorial"))
        except:
            print("Thats not a number!")
        else:
            break
    if fac_number >= 1559:
        print()
    elif fac_number <= 0:
        print()
    else:
        break


numbers = range(fac_number, 0, -1)

multiplied_numbers = map(times, numbers)

print(*list(multiplied_numbers), end="")
print(" all multiplied together is:")

print(math.factorial(fac_number))