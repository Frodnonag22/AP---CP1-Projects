# Andrew Petersen Crew Shares Pseudocode
# 
# IMPORT random from python
# GET random_credit_amount between 500 and 5000
# GET crew_numbers from user
# 
# CALCULATE total_crew = crew_numbers + 2
# CALCULATE yondu_13_percent = random_credit_amount * 0.13 rounded to 2 decimal places
# CALCULATE after_yondu = random_credit_amount - yondu_13_percent rounded to 2 decimal places
# CALCULATE peter_11_percent = after_yondu * 0.11 rounded to 2 decimal places
# CALCULATE after_peter = after_yondu - peter_11_percent rounded to 2 decimal places
# CALCULATE split_price = after_peter / total_crew rounded to 2 decimal places
# CALCULATE yondu_total = yondu_13_percent + split_price rounded to 2 decimal places
# CALCULATE peter_total = peter_11_percent + split_price rounded to 2 decimal places
# 
# DISPLAY original amount of units
# DISPLAY yondu_total
# DISPLAY peter_total
# DISPLAY split_price