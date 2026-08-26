#Unit 1 Final Andrew Petersen
print("Hello User")
name = input("What is your name, User? ")
print("Hello", name)
sport = input("What sport do you play? ")
print("Wow!", sport, "is really cool!")
record = input("What's your record? ")
print("WHAT? Your record is", record+ "!? That's insane!")
print("I wish I could play sports, but I'm just a porgram, so I can't")
hobby = input("What is your favorite passtime? ")
print("Huh...", hobby, "sounds interesting.")
while True:
    try:
        age = int(input("How old are you? (number not typed out pls) "))
    except:
        print("Thats not a number!")
    else:
        break
if age > 20:
	print("Did you ride a dinosaur to school??")
elif age < 20:
	print("wazzup yungin")
else:
    print("Bros almost unc")

final_check = input("Ok, so let me get this straight, you are", name, "you're", age, "you do", sport, "your record in", sport, "is", record, "and your hobby is", hobby, "Is that correct? ")
if final_check == "yes" or "Yes":
     print("YAY")
else: 
     print("")