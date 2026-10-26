# Andrew Petersen password checker pseudocode

# GET password from user

# SET capitals to list ["A" - "Z"]
# CHECK IF letter in capital is in password
    # SET cap_in_pass to 1
# ELSE
    # # SET cap_in_pass to 0

# SET lowercases to list ["a" - "z"]
# CHECK IF letter in lowercase is in password
    # SET low_in_pass to 1
# ELSE
    # # SET low_in_pass to 0

# CHECK IF the length of password is greater than or equal to 8
    # SET len_of_pass to 1
# ELSE
    # SET len_of_pass to 0

# SET numbers to list ["0" - "9"]
# CHECK IF number in password
    # SET num_in_pass to 1
# ELSE
    # SET num_in_pass to 0

# SET symbols to list ["!" - "?"]
# CHECK IF number in password
    # SET sym_in_pass to 1
# ELSE
    # SET sym_in_pass to 0

# CALCULATE pass_strength = cap_in_pass + low_in_pass + len_of_pass + num_in_pass + sym_in_pass

# DISPLAY "password is" (no end so it doesn't go on new line)
# CHECK IF pass_strength is 1 OR 5
    # DISPLAY "very" (no end so it doesn't go on new line)

# CHECK IF pass_strength is 3
    # DISPLAY "medium"
# ELSE IF pass_strength is more than 3
    # DISPLAY "strong"
# ELSE 
    # DISPLAY "weak"
