#Andrew Petersen, String Method Notes

sentence = "The quick brown fox jumps over the lazy dog"
# Methods DO NOT change the variable
fixed_sentence = sentence.replace("fox", "wolf")

word = input("What word do you want?: ").strip().lower()
new_word = input("What word should be in the sentence?: ").strip().lower()

location = sentence.find(word)
new_sentence = sentence.replace(word, new_word)

print(new_sentence)
print(sentence.find("over"))

first_name = input("wat ur first name: ").strip().title()
last_name = input("wat ur last name: ").strip().title()
first_separated = first_name.split()
first_fixed = "".join(first_separated)  
last_separated = last_name.split() # .split splits into a list and if there is a word in it then it gets rid of that word
last_fixed = "".join(last_separated) # "".join removed the excess spaces that the troller did
full_name = first_fixed.title() + " " + last_fixed.title()
print("Hello", full_name.title())

print(full_name.isalpha()) #checks if it is ALL letters
print(full_name.isnumeric()) #checks if it is ALL numbers
print(full_name.isupper()) #checks if it is ALL uppercase


print(sentence.split("the"))


#function
len(sentence)
#^ action ^ object

#Method
print(sentence.lower()) # all lowercase
print(sentence.upper()) #all uppercase
print(sentence.capitalize()) # capitalized the first letter
print(sentence.title()) # capitalized all first letters
#      ^ object  ^ action