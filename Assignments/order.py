# AP order up!
menu = {
    "Main Courses": {
        "Dave'S Sandwich": 8.39,
        "Baconator": 9.39,
        "Son of Baconator": 7.79,
        "Barbecue Cheeseburger": 7.89,
        "S'Awesome Bacon Cheeseburger": 8.39,
        "Peppercorn Mushroom Melt": 8.39,
        "Spicy": 7.39,
        "Homestyle": 7.39,
        "Asiago Ranch Chicken Club": 8.39,
        "Grilled": 7.69,
        "10 Piece Nuggets": 5.99,
        "Chicken Ternders": 8.49
    },
    "Drinks": {
        "Mountain Dew": 0.99,
        "Fountain Drink": 1.98,
        "FiiZ Drinks": 5.67,
        "Bo'Ohw'O'Wo'Er": 9.99,
        "Battery Acid": 1.99,
        "Coke And Mentos": 1.99
    },
    "Sides": {
        "Mac And Cheese": 1.20,
        "Fries": 1.99,
        "Salad": 2.59,
        "Mashed Potatoes": 2.69,
        "Assorted Vegetables": 1.89,
        "Corn": 0.19,
        "Cornbread": 3.89,
        "Entire Watermelon": 0.49
    }
}
for category, items in menu.items():
    print(f"\n--- {category.upper()} ---")
    for item, price in items.items():
        print(f"  {item:<38} ${price}")
print()
while True:
    user_course = input("What main course do you want: ").strip().title()
    if user_course in menu["Main Courses"]:
        print()
        break
    else: 
        print("That's not a main course we offer")
main_price = menu["Main Courses"][user_course]
while True:
    user_drink = input("What drink do you want: ").strip().title()
    if user_drink in menu["Drinks"]:
        print()
        break
    else: 
        print("That's not a drink we offer")
drink_price = menu["Drinks"][user_drink]
while True:
    user_side1 = input("What 2 sides do you want: \n").strip().title()
    user_side2 = input().strip().title()
    if user_side1 in menu["Sides"] and user_side2 in menu["Sides"]:
        print()
        break
    else: 
        print("Those are not sides we offer, try again")
side_price1 = menu["Sides"][user_side1]
side_price2 = menu["Sides"][user_side2]
print(f"Total price: ${round(main_price + drink_price + side_price1 + side_price2, 2)}")