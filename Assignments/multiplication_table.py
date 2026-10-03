# AP Multiplication Table

reset = "\033[0m"
bold ="\033[1m"
green = "\033[32m"

end = "no"
while end != "yes":
    while True:
        try:
            mult_chart_number = int(input("What number (1 - 31) do you want a multiplication chart to go up to? "))
        except:
            print(f"Thats not a valid number!")
        else:
            break
    if mult_chart_number > 31:
        print(f"Input must be 1 to 31")
    elif mult_chart_number <= 0:
        print(f"Input must be 1 to 31")
    else:
        end = "yes"

print(f"{bold}┌" + f"─────┬"*mult_chart_number + "─────┐")

for i in range(0, mult_chart_number+1):
    if i == 0:
        print("│  x  ", end="")
    elif i == mult_chart_number and i < 10:
                print(f"│  {i}  │")
    elif i == mult_chart_number:
        print(f"│  {i} │")
    elif i >= 10:
        print(f"│  {i} ", end="")
    else:
        print(f"│  {i}  ", end="")

print("├" + f"─────┼"*mult_chart_number + "─────┤")

mult_number = 1

for x in range(0, mult_chart_number):
    product_number = mult_chart_number * mult_number
    for i in range(0, mult_chart_number * mult_number + 1, mult_number):
        if i == 0 and x >= 9:
            print(f"{bold}│  {mult_number} ", end="")
        elif i == 0:
            print(f"{bold}│  {mult_number}  ", end="")
        elif i == product_number and i >= 100:
            print(f"│{reset} {i} │")
        elif i == product_number and i >= 10:
            print(f"│{reset}  {i} │")
        elif i == product_number and i >= 1:
            print(f"│{reset}  {i}  │")
        elif i >= 100:
            print(f"│{reset} {i} ", end="")
        elif i >= 10:
            print(f"│{reset}  {i} ", end="")
        else:
            print(f"│{reset}  {i}  ", end="")
    if x == mult_chart_number-1:
        print("└" + f"─────┴"*mult_chart_number + "─────┘")
    else:
        print("├" + f"─────┼"*mult_chart_number + "─────┤")
    mult_number += 1