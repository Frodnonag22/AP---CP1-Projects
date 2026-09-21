# Andrew Petersen Crew Shares

import random
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