# AP Functions Notes
name = input("Wat ur name ") 
#             v parameter
def birthday(name, age=35): # Parameters ONLY exist in the function, they are LOCAL
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {name}")
    print("Happy Birthday to you")
    print(f"U R now {age} years old")

#          v argument
birthday("Bob", 35)
print()
birthday("Bobby", 35)
print()
birthday("Bobbette", 35)
birthday(name)

# 4 main purposes
# 1: Readability
#   Good function means easy read
# 2: Modularity
#   big problem makes easy
# 3: Reusability
#   Prefered to be used a million times
# 4: Abstraction
#   Use a function without knowing how the insides work