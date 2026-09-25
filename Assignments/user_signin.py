# Andrew Petersen User Signin

red = "\033[31m"
reset = "\033[0m"

users = ["John123", "User4","oops","Why.com"]
passes = ["pass1234", "password", "hjladsafh5323", "insertpasswordhere"]

signup = input("Would you like to sign up? ").lower().strip()

if signup == "yes":
    username = input("What is your username? ").strip()
    users.append(username)
    password = input("What is your password? ").strip()
    passes.append(password)
    login = "yes"
else:
    login = input("Would you like to log in now? ").lower().strip()

if login == "yes" and signup =="yes":
    userattempt = input("Re-type your password: ")
    passattempt = input("Re-type your username: ")
elif login == "yes":
    userattempt = input("What is your username? ")
    passattempt = input("What is your password? ")
else:
    print("Why are you here?")
    userattempt = "no"
    passattempt = "no"

if userattempt in users and passattempt in passes:
    print(f"Welcome {userattempt}")
elif passattempt == "no" and userattempt == "no":
    print("Go away")
elif userattempt in users:
    print("Incorrect password")
elif passattempt in passes:
    print("Invalid username")
else:
    print(f"{red}Account Error, type the username and password correctly next time{reset}")