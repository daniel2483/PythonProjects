print ("\n\n### Task 1 ###")
# [ ] Get user input for first_name
first_name = "Newstring"
# [ ] iterate through letters in first_name

#    - print each letter on a new line
for stringChar in first_name:
    print (stringChar)


print ("\n\n### Task 2 ###")
# [ ] Create capitalize-io
new_name = ""
for letters in first_name:
    if(letters == "i" or letters == "o"):
        new_name += letters.upper();
    else:
        new_name += letters
print ("Nombre original " + first_name + " Nombre nuevo: " + new_name) 


print ("\n\n### Task 3 ###")
# [ ] create & print a variable, other_word, made of every other letter in long_word
long_word = "juxtaposition"
for other in long_word[3::2]:
    print (other)

print ("\n\n")
# Mirror Color
# [ ] get user input, fav_color
# [ ] print fav_color backwards + fav_color
# example: "Red" prints "deRRed"
fav_color = "Green"
for wordRev in fav_color[::-1]:
    print (wordRev)
for word in fav_color:
    print (word)
