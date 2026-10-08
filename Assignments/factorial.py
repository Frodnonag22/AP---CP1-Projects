# AP Factorial Calculator
import math
def times(number):
    return number

while True:
    while True:
        try:
            factorial_number = int(input("What number do you want to factorial: "))
        except:
            print("Thats not a number!")
        else:
            break
    if factorial_number >= 1559:
        print("Invalid number")
    elif factorial_number < 0:
        print("Invalid number")
    else:
        break

numbers = range(1, factorial_number+1)

new_numbers = []
for number in numbers:
    new_numbers.append(number)

if factorial_number == 0:
    print("0!")

print(f"{factorial_number}! = ", end="")
print(" x ".join(map(str, new_numbers)), end=" = ")
print(math.factorial(factorial_number))