# AP, What is my grade

reset = "\033[0m"
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"

while True:
    try:
        gp = int(input(f"{blue}What is your grade percentage: {cyan}"))
    except:
        print("Thats not a valid number!")
    else:
        break
print(f"{reset}")

if gp >= 90:
    print(f"{green}Your grade is: {gp} AKA an A! Good job, keep up the good work!")
elif gp >= 80:
    print(f"Your grade is: {gp} AKA a B")