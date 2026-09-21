# Andrew Petersen Crew Shares


import random
print("Yondu Udonta and his crew arrive at the Iron Lotus after several weeks of plundering various places around the galaxy. The crew has been in space for nearly six months and they are ready for a night of celebration. Yondu doesn't want to divvy up the plunder just yet, so he gives each crew member other than himself and Peter Quill 3 units and sends them off to the Iron Lotus. After the crew has gone, he and Peter count what's left and decide how to split it up among the crew. Yondu takes 13% of the total. He then gives Peter 11% of what's left. The next morning, Yondu divides the remaining amount evenly among all of the crew, including Yondu and Quill. The crew does not know that Yondu and Quill have already taken a cut.")
random_credit_amount = random.randint(500, 5000)
while True:
    try:
        crew_numbers = int(input(f"How many crew members are there? "))
    except:
        print("Thats not a number!")
    else:
        break

total_crew = crew_numbers + 2
yondu_13_percent = yondu_13_percent = random_credit_amount * 0.13
after_yondu = random_credit_amount - yondu_13_percent
peter_11_percent = after_yondu * 0.11
after_peter = after_yondu - peter_11_percent
split_price = after_peter / total_crew
split_price = round(split_price, 2)
yondu_total = round(yondu_13_percent) + round(split_price, 2)
peter_total = round(peter_11_percent, 2) + round(split_price, 2)

print(f"Amount of units collected: {random_credit_amount}")
print(f"Yondu's share: {yondu_total}")
print(f"Peter's share: {peter_total}")
print(f"Crew's share: {split_price}")