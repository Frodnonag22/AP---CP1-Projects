# AP Multiplaction Chart

while True:
    while True:
        try:
            choice = int(input())
        except:
            print("Thats not a number!")
        else:
            break
    if choice >= 32:
        print("try again")
    elif choice <= 0:
        print("try again")
    else: 
        break

for i in range(1, choice+2):
    if i == 1:
        print("┌", end="")
    elif i == choice+1:
        print("────┐")
    else:
        print("────┬", end="")

for i in range(1, choice+1):
    go_until = 1
    print("│", end="")
    for x in range(1 , choice+1):
        print(f"{i * x:4}│", end="")
    print()
    if i != choice:
        print("├", end="")
    else:
        print("└", end="")
    if i != choice:
        for y in range(1 , choice+1):
            if go_until == choice:
                print(f"────", end="")
            else:
                print(f"────┼", end="")
            go_until += 1
        print("┤")
    else:
        for y in range(1 , choice+1):
            if go_until == choice:
                print(f"────", end="")
            else:
                print(f"────┴", end="")
            go_until += 1
        print("┘")