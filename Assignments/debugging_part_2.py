# AP Fixing with the debugger
# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? ")) # Needs to be a integer

total = price * quantity

discounted_total = total - 2 * 0.90 # We want 10 percent off, not 90 percent

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) # incorrect variable name
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(total)) #Prints original price instead of total price before tax
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") # Missing Parenthesis on the last line