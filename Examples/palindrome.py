# String Lists
# strings lists index
# Exercise 6 (and Solution)

# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

string = input("Enter a string to see if is a palindrome:\n")

string2 = string[::-1]

print("Original Phrase: "+string)
print("Manipulated Phrase: "+string2)

if string == string2:
    print("This is a palindrome!!!")
else:
    print("This is not a palindrome!")
#for character in string:
#    print(character)