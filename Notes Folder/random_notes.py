# Andrew Petersen random notes

import random # imports a module or library that already exists

ducks = random.randint(1, 100) # first number is lowest number second is the highest number. Separate with a comma
# rand.int is a function
print(f"There are {ducks} ducks")

fruits = ["Pineapple","Mango","Apple","Cherry"]
print(f"I like {random.choice(fruits)}") #pick a random item from a list of items

pens = random.randrange(2,10,2) #First is starting point, second is ending point (NOT INCLUDED) third is what it is counting by
print(f"I have {pens} pens")

percent = random.random() #gets a float that is between 1 and 0
print(f"You have a {percent:.2} grade.")