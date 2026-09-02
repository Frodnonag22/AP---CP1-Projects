#Andrew Petersen String Notes

name = "Andrew" # <= this is a string

age = "15" # <= this is a string as well

print(age + "2")

print(name + " " + age)

first_name = "Andrew"
last_name = "Petersen"
full_name = first_name + " " + last_name

print(last_name)

print('Single quotes work')
#escape character \
print('can\'t use apostraphies in the string though')

print("backslash n will \nreturn the line backslash t will \ttab the line")

print("-" * 60)

sentence = "The quick brown fox jumps over the lazy dog"
print(sentence)
#index starts at 0
#Spaces count as characters
print(sentence.find("t"))
#add one to make it start at one
print(sentence.find("t") + 1)
print(sentence[10: 15]) #The 10 is the start location the ending index is NOT included
word = "jumps"
start = sentence.find(word)
length = len(word)
print(sentence[start: start+length])