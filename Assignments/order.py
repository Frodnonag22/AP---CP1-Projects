# AP order up!

menu = {
    "Main Courses": {
        "Dave's Sandwich": 8.39,
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
        "Pepsi": 1.09,
        "Mountain Dew": 1.95,
        "Mug": 2.99
    }
}

for category, items in menu():
    print(f"\n--- {category.upper()} ---")
    for item, price in items.items():
        print(f"  {item:<38} ${price}")

user_course = input("What main course do you want: ").strip().title()