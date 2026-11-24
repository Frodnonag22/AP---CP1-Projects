# AP Flexible Calculator

import sys as s
import time as t 

def type_print(text: str = "", delay: float = 0.05, end = "\n"):
    """Types out text slowly"""
    for char in text:
        s.stdout.write(f"{char}")
        s.stdout.flush()
        t.sleep(delay)
    s.stdout.write(end)
    s.stdout.flush()

def type_input(prompt: str, delay: float = 0.05):
  """Types out inputs slowly"""
  for character in prompt:
    s.stdout.write(f"{character}")
    s.stdout.flush()
    t.sleep(delay)
  return input()

def clear_terminal():
    """clears the terminal"""
    print("\033[H\033[J", end="")

def sum(*args):
    """Calculates the Sum"""
    total = 0
    for arg in args:
        total += arg
    return total

def average(*args):
    """Calculates the avarage"""
    total = 0
    for arg in args:
        total += arg
    amount = 0
    for arg in args:
        amount += 1
    average = total/amount
    return round(average, 2)

def max(*args):
    """Calculates the Max"""
    for arg in args:
        largest = arg
    for arg in args:
        if largest < arg:
            largest = arg
    return largest

def min(*args):
    """Calculates the Min"""
    for arg in args:
        smallest = arg
    for arg in args:
        if smallest > arg:
            smallest = arg
    return smallest

def product(*args):
    """Calculates the Product"""
    product = 1
    for arg in args:
        product *= arg
    return product

clear_terminal()

type_print("Welcome to the Flexible Calculator!\n\nAvailable operations: sum, average, max, min, product\n")

keep_going = True
while keep_going:
    operations = ["sum", "average", "max", "min", "product"]
    while True:
        operation = type_input("Which operation would you like to perform? ")
        if operation in operations:
            break
        else:
            type_print(f"{operation} is not a valid operation\nTry again")

    type_print("\nEnter numbers - negatives will not be accepted -  (type \"done\" when finished):")
    number_list = []
    while True:
        try:
            user_number = type_input("Number: ")
            if "done" in user_number:
                break
            if "-" in user_number:
                type_print("Negative numbers are not allowed")
                user_number = "dfs"
                user_number = int(user_number)
            elif user_number.isnumeric():
                user_number = int(user_number)
                number_list.append(user_number)
            else:
                user_number = int(user_number)
        except:
            type_print("Invalid input\nTry again\n")

    type_print(f"Calculating {operation} of: ", end="")
    print(*number_list)

    if operation == "sum":
        type_print(f"Result: {sum(*number_list)}")
    elif operation == "average":
        type_print(f"Result: {average(*number_list)}")
    elif operation == "max":
        type_print(f"Result: {max(*number_list)}")
    elif operation == "min":
        type_print(f"Result: {min(*number_list)}")
    elif operation == "product":
        type_print(f"Result: {product(*number_list)}")
    else:
        type_print("Congradulations, you have officially broken me")

    while True:
        check = type_input("Would you like to run another operation? (yes/no)")
        if "yes" in check:
            clear_terminal()
            break
        elif "no" in check:
            keep_going = False
            break
        else: 
            type_print("Think you're funny huh?")
            type_print("Good luck >:)")
            x = 1
            speed = 0.5
            while x < 100:
                type_print("The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly but gets faster each minute after you hear this signal bodeboop. A sing lap should be completed every time you hear this sound. ding Remember to run in a straight line and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark. Get ready!… Start.", speed)
                x += 0.5
                speed -= speed/2