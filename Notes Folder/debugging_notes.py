# Andrew Petersem Debugging notes

# Syntax Error
# fix by doing what python tells you to fix
# ex:
# print("Hello)

    #White space is anywhere that doesn't have code such as spaces, tabs, and blank lines
      
#indentation error
# ed:
# if True:
# print("This is true")

# people = 10
# print(poeple)

# Logic Error
#Didn't write code wrong but did wrong order
# fix by reading code again
#ex
# apples = 100
# people = 20
# print(apples * people)

# Run Time Errors
while True:
    try:
        fav_num = int(input("What is your favorite number"))
    except:
        print("Thats not a number!")
    else:
        break

print(4 + fav_num)
