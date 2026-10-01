# AP Shopping List Manager

black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
reset = "\033[0m"
strike = "\033[9m"

shop_list = []

while True:
    # Forcing the user to type a vailid number lol
    while True:
        while True:
            try:
                action = int(input(f"\n{white}Would you like to: \n{cyan}1{white}: Add an item, \n{cyan}2{white}: Remove an item completely, \n{cyan}3{white}: Cross off item from list, \n{cyan}4{white}: Print off list \n{cyan}5{white}: Exit \n{cyan}"))
            except:
                print(f"{red}Thats not a valid number!{reset}")
            else:
                break
        if action > 5:
            print(f"{red}Invalid input{reset}")
        elif action < 1:
            print(f"{red}Invalid input{reset}")
        else:
            break

    if action == 1:
        added_item = input(f"\n{blue}What item would you like to add: \n{cyan}").strip().title()
        shop_list.append(added_item)
    elif action == 2: 
        while True:
            removed_item = input(f"\n{blue}What item do you want to remove (type 'cancel' to cancel): \n{cyan}").strip().title()
            if removed_item in shop_list:
                print(f"{green}Removing item...{reset}")
                shop_list.remove(removed_item)
                break
            elif removed_item == "Cancel":
                print(f"{yellow}Cancelling request{reset}")
                break
            else:
                print(f"{red}Item not in list{reset}")
    elif action == 3:
        while True:
            crossed_off = input(f"{blue}What item do you want to cross off (type 'cancel' to cancel): \n{cyan}").strip().title()
            if crossed_off in shop_list:
                print(f"{green}Crossing off item...{reset}")
                shop_list.remove(crossed_off)
                crossed_off = strike + crossed_off + reset
                shop_list.append(crossed_off)
                break
            elif crossed_off == "Cancel":
                print(f"{yellow}Cancelling request{reset}")
                break
            else:
                print(f"{red}Item not in list{reset}")
    elif action == 4: 
        print()
        for item in shop_list:
            print(f"{magenta}{item}{reset}")
    elif action == 5:
        print("Exiting")
        break
    else:
        print("What?")
        print("How?")
        break