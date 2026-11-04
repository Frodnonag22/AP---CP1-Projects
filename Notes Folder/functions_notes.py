# AP Functions Notes
name = input("Wat ur name: ") 
#             v parameter

def increase():
    return attempts + 1

def birthday(name, age=35): # Parameters ONLY exist in the function, they are LOCAL
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {name}")
    print("Happy Birthday to you")
    print(f"U R now {age} years old")

attempts = 0
def stupid_proof(user_answer, correct):
    user_answer = user_answer.strip().title()
    if user_answer in correct:
        return True, user_answer, increase()
    else:
        return False, user_answer, increase()
#          v argument
birthday("Bob", 35)
print()
birthday("Bobby", 35)
print()
birthday("Bobbette", 35)
birthday(name)

while True:
    capital = input("What is the capital of Utah: ")
    correct, capital, attempts = stupid_proof(capital, ["Salt Lake City", "Slc", "Salt Lake"])
    if correct:
        print(f"Good job {capital} is the capital of Utah")
        break
    else:
        print(f"Try Again. {capital} is not the capital of Utah. You have tried {attempts} times")
        
print(f"You took {attempts} attempts")
# 4 main purposes
# 1: Readability
#   Good function means easy read
# 2: Modularity
#   big problem makes easy
# 3: Reusability
#   Prefered to be used a million times
# 4: Abstraction
#   Use a function without knowing how the insides work