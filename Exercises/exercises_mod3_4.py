print ("\n\n### Task 1 ###\n\n")
# [ ] split the string(rhyme) into a list of words (rhyme_words)
# [ ] print each word on it's own line
rhyme = 'Jack and Jill went up the hill To fetch a pail of water' 
words = rhyme.split()

print("Words in rhyme phrase: ")
for word in words:
    print(word)

# [ ] split code_tip into a list and print the first and every other word
print("\n\n")
code_tip = "Python uses spaces for indentation"
code_tip = code_tip.split()

print("Code tips words: ")
for word in code_tip:
    print(word)


print ("\n\n### Task 2 ###\n\n")
# [ ] split poem into a list of phrases by splitting on "*" a
# [ ] print each phrase on a new line in title case
poem = "Write code frequently*Save code frequently*Comment code frequently*Study code frequently*"
poem = poem.split('*')
for line in poem:
    print(line.title())


print ("\n\n### Task 3 ###\n\n")
# [ ] .join() letters list objects with an Asterisk: "*"
letters = ["A", "s", "t", "e", "r", "i", "s", "k"]
print("Joined Letters: ","*".join(letters))


print ("\n\n### Task 4 ###\n\n")
# Program: Choose the separator¶
#       get user input on what to use to join words (" ", *, -, etc...) - store in variable: separator
#       join pharse_words with the separator and print


# [ ] complete Choose the separator
phrase_words = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill', 'To', 'fetch', 'a', 'pail', 'of', 'water']
separator = input("Which Separator: ")

print("Phrase Joined: ",separator.join(phrase_words))


print ("\n\n### Task 5 ###\n\n")
# [ ] use 3 print() statements to output text to one line 
# [ ] separate the lines by using "- " (dash space)
string= list("This is a new text")
for word in string:
    print(word,end="- ")
print("\n")

for word in string:
    print(word,end="")
print("\n")

for word in string:
    print(word,end="|")
print("\n")


print ("\n\n### Task 6 ###\n\n")
# cast: str to list
# Msg_characters = list("Always test your code")
Msg_characters = list("Always test your code... Is important!")
for chars in Msg_characters:
    if chars == " ":
        print(end="\n")
    else:
        print(chars)


print ("\n\n### Task 7 ###\n\n")
# Program: add the digits
#   - create a 20 digit string, and cast to a list
#   - then add all the digits as integers
#   - print the equation and answer
# Hint: use cast to sum the digits, and .join() to create the equation (1+2+3+...)
digits_string="10234321278233129584"
print("Number of digits: ",len(digits_string))
digits_list=list(digits_string)
result = 0
equation = ""
plus = " + "
for digit in digits_list:
    result += int(digit)

equation = " + ".join(digits_list)

print("Equation:\n\n",equation," = ",result)

