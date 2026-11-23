# AP Flexible Calculator

import sys as s
import time as t 

def cool_print(text: str = "", delay: float = 0.05, end = "\n"):
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

print("Welcome to the Flexible Calculator!\n\nAvailable operations: sum, average, max, min, product\n")
type_input("Which operation would you like to perform?").strip().lower
print("\nEnter numbers (type \"done\" when finished):")
number_list = []
while True:
    try:
        user_number = type_input("Number: ")
        if "done" in user_number:
            break
        if "-" in user_number:
            cool_print("Negative numbers are not allowed")
            user_number = "dfs"
            user_number = int(user_number)
        elif user_number.isnumeric():
            user_number = int(user_number)
            number_list.append(user_number)
        else:
            user_number = int(user_number)
    except:
        print("Invalid input\nTry again\n")

print(min(*number_list))