print ("\n\n### Task 1 ###")

# [ ] access and print the second character from planet_name: "u"
planet_name = "Jupiter"
print(planet_name[1])

# [ ] access and print the first character from planet_name: "J"
planet_name = "Jupiter"
print(planet_name[0])

# [ ] access and print the first and last characters from planet_name
planet_name = "Jupiter"
print(planet_name[0],planet_name[-1])

# [ ] using a negative index access and print the first character from planet_name: "J"
planet_name = "Jupiter"
print(planet_name[-7])

print ("\n\n### Task 2 ###")

# [ ] print planet_name sliced into the first 3 characters and remaining characters
planet_name = "Neptune"
print (planet_name[:3])
print (planet_name[3:])

# [ ] print 1st char and then every 3rd char of wise_words
# use string slice with a step
wise_words = 'Play it who opens'
print(wise_words[::3])

# [ ] print planet_name in reverse
print(planet_name[::-1])

print ("\n\n### Task 3 ###")

# [ ] Get user input for 1 fav_food
# [ ] iterate through letters in fav_food 
#    - print each letter on a new line
fav_food = "Shrimps"

for food in fav_food:
    print (food)
    
# [ ] iterate work_tip string concatenate each letter to variable: new_string 
# [ ] concatenate the letter or a "-" instead of a space " "
# tip: concatenate string example: word = word + "a"
work_tip = "Good code is commented code"
new_string = ""

for sentence in work_tip:
    if sentence == " ":
        sentence = "-"
        
    new_string = new_string + sentence
    print (new_string)
    
# [ ] Print the first 4 letters of name on new line
name = "Hiroto"
print(name[:4])

# [ ] Print every other letter from 2nd to last letter of name 
name = "Hiroto"
print (name[1:])

print ("\n\n### Task 4 ###")

# [ ] Create Mystery Name
first_name = "D!ni&l"
new_name = ""

for name in first_name:
    if name == "!":
        name = "a"
    elif name == "&":
        name = "e"
    new_name = new_name + name
    print(new_name)

# [ ] find and display the length of the string: topic
topic = "len() returns the length of a string"
print(len(topic))

# [ ] use len() to find and display the mid_pt (middle) index (+/- 1) of the string: topic
# note: index values are whole numbers
topic = "len() can take a sequence, like a string, as an argument"
mid_pt = int(len(topic)/2)
#print(mid_pt)
print(topic[:mid_pt])
print(topic[mid_pt:])

# [ ] print index where first instance of the word  "code" starts using .find()
work_tip = "Good code is commented code"
test=work_tip.find("code")
print(test)


# [ ] search for "code" in code_tip using .find() 
# [ ] search substring with substring index start= 13,end = last char 
# [ ] save result in variable: code_index
# [ ] display index of where "code" is found, or print "not found" if code_index == -1
work_tip = "Good code is commented code"
sub = work_tip[13:]
code_index=work_tip.find("code")
print(code_index)
code_index=sub.find("code")
print(code_index)

if code_index != -1:
    print("code is found")
else:
    print("code is not found")


print ("\n\n### Task 5 ###")

# [ ] find and report (print) number of w's, o's + use of word "code"
work_tip = "Good code is commented code"
count_ws=0
count_os=0
count_code = 0
words_code = work_tip.split()

for sentence in work_tip:
    if sentence == "w":
        count_ws += 1
    if sentence == "o":
        count_os += 1
        
for words in words_code:
    if(words == "code"):
        count_code += 1

print(count_ws)
print(count_os)
print(count_code)


print ("\n\n### Task 6 ###")
# [ ]  count times letter "i" appears in code_tip string
# [ ] find and display the index of all the letter i's in code_tip
# Remember: if .find("i") has No Match, -1 is returned
code_tip = "code a conditional decision like you would say it"
print ("code_tip:" , code_tip)
count_i = 0

for codetip in code_tip:
    if codetip == "i":
        count_i += 1

print("Number of i's: ",count_i)
        
init = 0
index = 0

for i in range(0,500):
    index_copy = index
    index = code_tip.find("i",i+init)
    if index != -1 and index != index_copy:
        print(index)
    init+=1


# Create a program inputs a phrase (like a famous quotation) and prints all of the words that start with h-z

# Sample input:
# enter a 1 sentence quote, non-alpha separate words

#quote = "Wheresoever you go, go with all your heart "

quote = input("Please enter a quote: ")
quote = quote + " "


print ("\n\n### Task 7 ###")
word = ""
alphabetic = 'abcdefghijklmnopqrstuvwxyz'

for letter in quote:
    if letter.isalpha() == True:
        word = word + letter
    else:
        if word != "":
            #print(word)
            for alpha in alphabetic[7:28]:
                #print (alpha)
                if word[0].lower() == alpha:
                    print (word.upper())
                    word = ""
                    break
            word=""
        

