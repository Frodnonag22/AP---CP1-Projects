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

keep_going = True
while keep_going:
    while True:
        try:
            grade_percent = int(input(f"{blue}What is your grade percentage? (Enter the whole number before the decimal, e.g., 85: {cyan}"))
        except:
            print(f"{red}Thats not a valid number!{reset}")
        else:
            break
    print(f"{reset}")

    while True:
        try:
            grade_percent2 = int(input(f"{blue}And what are the numbers after the decimal? (e.g., 5 or 00): {cyan}{grade_percent}."))
        except:
            print(f"{red}Thats not a valid number!{reset}")
        else:
            break
    print(f"{reset}")

    if grade_percent >= 93:
        print(f"{green}Your grade is: {grade_percent}.{grade_percent2} AKA an A! Good job, keep up the good work!{reset}")
        print()
    elif grade_percent >= 90:
        print(f"{green}Your grade is: {grade_percent}.{grade_percent2} AKA an A-{reset}")
        print()
    elif grade_percent >= 87:
        print(f"Your grade is: {grade_percent}.{grade_percent2} AKA an B+{reset}")
        print()
    elif grade_percent >= 83:
        print(f"Your grade is: {grade_percent}.{grade_percent2} AKA a B{reset}")
        print()
    elif grade_percent >= 80:
        print(f"Your grade is: {grade_percent}.{grade_percent2} AKA an B-{reset}")
        print()
    elif grade_percent >= 77:
        print(f"{yellow}Your grade is: {grade_percent}.{grade_percent2} AKA an C+{reset}")
        print()
    elif grade_percent >= 73:
        print(f"{yellow}Your grade is: {grade_percent}.{grade_percent2} AKA a C{reset}")
        print()
    elif grade_percent >= 70:
        print(f"{yellow}Your grade is: {grade_percent}.{grade_percent2} AKA an C-{reset}")
        print()
    elif grade_percent >= 67: # lol
        print(f"{magenta}Your grade is: {grade_percent}.{grade_percent2} AKA an D+{reset}")
        print()
    elif grade_percent >= 63:
        print(f"{magenta}Your grade is: {grade_percent}.{grade_percent2} AKA a D{reset}")
        print()
    elif grade_percent >= 60:
        print(f"{magenta}Your grade is: {grade_percent}.{grade_percent2} AKA an D-{reset}")
        print()
    elif grade_percent <= 60:
        print(f"{red}Your grade is: {grade_percent}.{grade_percent2} AKA an F{reset}")
        print()
    else:
        print(f"{black}How is your input invalid?")
        print(f"Congradulations I guess. You broke the code somehow. I guess you've won! Goodbye... for now....{reset}")

    
    end = "no"
    while end != "yes":
        while True:
            try:
                keep_go = int(input(f"{blue}Would you like to input another grade? (1: yes 2: no): {cyan}"))
            except:
                print(f"{red}Thats not a valid number!{reset}")
            else:
                break
        if keep_go > 2:
            print(f"{red}Input must be one or 2{reset}")
        elif keep_go < 0:
            print(f"{red}Input must be one or 2{reset}")
        else:
            end = "yes"
    if keep_go == 1:
        keep_going = True
    else:
        keep_going = False
        print(f"{reset}")