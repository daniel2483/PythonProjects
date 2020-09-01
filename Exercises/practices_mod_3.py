print ("\n\n### Last Exercises Module 3 ###\n\n")
print ("\n\n### Task 1 ###\n\n")
#   list iteration: for in
#   for item in list:

# [ ] print out the "physical states of matter" (matter_states) in 4 sentences using list iteration
# each sentence should be of the format: "Solid - is state of matter #1" 
matter_states = ['solid', 'liquid', 'gas', 'plasma']
count = 1
for matter in matter_states:
    print(matter.title()," - is state of matter #",count)
    count += 1

# [ ] iterate the list (birds) to see any bird names start with "c" and remove that item from the list
# print the birds list before and after removals
birds = ["turkey", "hawk", "chicken", "dove", "crow"]

print ("\n\nList of birds: ",birds)
for bird in birds:
    if bird[0].lower() == "c":
        birds.remove(bird)
print ("New list of birds: ",birds)

# the team makes 1pt, 2pt or 3pt baskets
# [ ] print the occurrence of each type of basket(1pt, 2pt, 3pt) & total points using the list baskets
baskets = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]
total = 0
for points in baskets:
    print(points,"pt")
    total += int(points)
print("Total:",total)

print ("\n\n### Task 2 ###\n\n")
#   iteration with range(start) & range(start,stop)
# [ ] using range() print "hello" 4 times
# [ ] find spell_list length
# [ ] use range() to iterate each half of spell_list  
# [ ] label & print the first and second halves
for count in range(0,4):
    print("Hello")

spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
length = len(spell_list)
half = int(length/2)
first_half = ""
second_half = ""

for list in range(0,half):
    first_half = first_half + " " + spell_list[list]

for list in range(half,length):
    second_half = second_half + " " + spell_list[list]

print("First Half: " + first_half)
print("Second Half: " + second_half)



# [ ] build a list of numbers from 20 to 29: twenties 
# append each number to twenties list using range(start,stop) iteration
# [ ] print twenties
print("\n\n")
twenties = []
for count in range(20,30):
    twenties.append(count)
print("List of numbers: ",twenties)

# [ ] iterate through the numbers populated in the list twenties and add each number to a variable: total
# [ ] print total
print("\n\n")
total = 0
for number in twenties:
    total += number
print("Total: ",total)

# check your answer above using range(start,stop)
# [ ] iterate each number from 20 to 29 using range()
# [ ] add each number to a variable (total) to calculate the sum
# should match earlier task
print("\n\n")
total = 0
for count in range(20,30):
    print("Numbers: ",count)
    total += count
print("Total: ",total)

print ("\n\n### Task 3 ###\n\n")
# iteration with range(start:stop:skip)
# [ ] create a list of odd numbers (odd_nums) from 1 to 25 using range(start,stop,skip)
# [ ] print odd_nums
# hint: odd numbers are 2 digits apart

odd_numbers = []
for numbers in range(1,26,2):
    #print("Odd number: ", numbers)
    odd_numbers.append(numbers)
print("Odd Numbers list: ",odd_numbers)

# [ ] create a Decending list of odd numbers (odd_nums) from 25 to 1 using range(start,stop,skip)
# [ ] print odd_nums,  output should resemble [25, 23, ...]
odd_numbers_reverse = []
for numbers in range(25,0,-2):
    #print("Odd number: ", numbers)
    odd_numbers_reverse.append(numbers)
print("Odd Numbers Reverse list: ",odd_numbers_reverse)

# the list, elements, contains the names of the first 20 elements in atomic number order
# [ ] print the even number elements "2 - Helium, 4 - Beryllium,.." in the list with the atomic number
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']
for number in range(1,20,2):
    print((number+1),"-", elements[number])
    

# [ ] the list, elements_40, contains the names of the first 40 elements in atomic number order
# [ ] print the odd number elements "1 - Hydrogen, 3 - Lithium,.." in the list with the atomic number elements_40
print("\n\n")
elements_40 = ['Hydrogen', \
 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', \
 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', \
 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', \
 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium']
for number in range(0,40,2):
    print((number+1),"-", elements_40[number])


print ("\n\n### Task 4 ###\n\n")
# [ ] print the combined lists (numbers_1 & numbers_2) using "+" operator
numbers_1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# pythonic casting of a range into a list

# numbers_2 = list(range(30,50,2)) -- Not working
numbers_2 = [*range(30,50,2)]


all_numbers = numbers_1 + numbers_2

print("numbers_1:",numbers_1)
print("numbers_2:",numbers_2)
print("Join List:",all_numbers)

# [ ] print the combined element lists (first_row & second_row) using ".extend()" method
print("\n\n")
first_row = ['Hydrogen', 'Helium']
second_row = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
combined = []
print("1st Row:", first_row)
print("2nd Row:", second_row)
combined.extend(first_row)
combined.extend(second_row)
print("Combined List:",combined)

# Project: Combine 3 element rows
# Choose to use "+" or ".extend()" to build output similar to

# The 1st three rows of the Period Table of Elements contain:
# ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']

# The row breakdown is
# Row 1: Hydrogen, Helium
# Row 2: Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine, Neon
# Row 3: Sodium, Magnesium, Aluminum, Silicon, Phosphorus, Sulfur, Chlorine, Argon
# [ ] create the program: combined 3 element rows 
print("\n\n")
elem_1 = ['Hydrogen', 'Helium'] 
elem_2 = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
elem_3 = ['Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']
elements = []
print("Elements 1: ",elem_1)
print("Elements 2: ",elem_2)
print("Elements 3: ",elem_3)
for count in range(1,4):
    if count == 1:
        elements.extend(elem_1)
    if count == 2:
        elements.extend(elem_2)
    if count == 3:
        elements.extend(elem_3)
print("Elements extends: ",elements)


# [ ] .extend() jack_jill with "next_line" string - print the result
print("\n\n")
jack_jill = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']
next_line = ['To', 'fetch', 'a', 'pail', 'of', 'water']
jack_jill.extend(next_line)
print(jack_jill)


print ("\n\n### Task 5 ###\n\n")
#   .reverse() : reverse a list in place
# [ ] use .reverse() to print elements starting with "Calcium", "Chlorine",... in reverse order
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',
 'Potassium', 'Calcium']
elements.reverse()
print("Elements in reverse order: ",elements)

# [ ] reverse order of the list... Then print only words that are 8 characters or longer from the now reversed order
print ("\n\n")
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
spell_list.reverse()
print("Words in reverse order: ",spell_list)
for words in spell_list:
    if len(words) >= 8:
        print("Word more than, or equal than 8 characters: ",words)


print ("\n\n### Task 6 ###\n\n")
#   .sort() and sorted()
# [ ] sort the list element, so names are in alphabetical order and print elements
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']
elements.sort()
print("Sorted Elements: ",elements)

# [ ] print the list, numbers, sorted and then below print the original numbers list
print ("\n\n")
numbers = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]
print("Original List: ",numbers)
sorted_numbers=sorted(numbers)
print("Sorted numbers: ",sorted_numbers)

print("Original List: ",numbers)


print ("\n\n### Task 7 ###\n\n")
# Converting a string to a list with .split()
# [ ] split the string, daily_fact, into a list of word strings: fact_words
# [ ] print each string in fact_words in upper case on it's own line
daily_fact = "Did you know that there are 1.4 billion students in the world?"
print("Original phrase: ",daily_fact)
fact_words = daily_fact.split()
for words in fact_words:
    print(words.upper())

# [ ] convert the string, code_tip, into a list made from splitting on the letter "o"
print ("\n\n")
code_tip ="Read code aloud or explain the code step by step to a peer"
print("Original code tip: ",code_tip)
list_code_tip = code_tip.split('o')
print("List: ",list_code_tip)

# [ ] split poem on "b" to create a list: poem_words
# [ ] print poem_words by iterating the list
print ("\n\n")
poem = "The bright brain, has bran!"
print("Original poem: ",poem)
list_poem= poem.split('b')
print("List: ",list_poem)
for list in list_poem:
    print(list)



print ("\n\n### Task 8 ###\n\n")
# .join()
# build a string from a list
# [ ] print a comma separated string output from the list of Halogen elements using ".join()"
halogens = ['Chlorine', 'Florine', 'Bromine', 'Iodine']
print("Comma Separated: ",",".join(halogens))

# [ ] split the sentence, code_tip, into a words list
# [ ] print the joined words in the list with no spaces in-between
# [ ] Bonus: capitalize each word in the list before .join()
print ("\n\n")
code_tip ="Read code aloud or explain the code step by step to a peer"
list_code_tip = code_tip.split()
print("No spaces between: ","".join(list_code_tip))
new_list_code_tip=[]
for words in list_code_tip:
    new_list_code_tip.append(words.title())
print("No spaces between: ","".join(new_list_code_tip))


print ("\n\n### Task 9 ###\n\n")
# list(string) & print("hello",end=' ')
#   - Cast a string to a list
#   - print to the same line
# [ ] cast the long_word into individual letters list 
# [ ] print each letter on a line
long_word = 'decelerating'
#letter_list = list(long_word) Currently not working
for letter in long_word:
    print(letter)

# [ ] use use end= in print to output each string in questions with a "?" and on new lines
print ("\n\n")
questions = ["What's the closest planet to the Sun", "How deep do Dolphins swim", "What time is it"]
for quest in questions:
    print(quest,end="?\n")


# [ ] print each item in foot bones 
#    - capitalized, both words if two word name
#    - separated by a comma and space
#    - and keeping on a single print line
print ("\n\n")
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
for bone in foot_bones:
    print(bone.title())

comma_separated = ",".join(foot_bones)
print("Comma Separated: ",comma_separated,end=" | ")

space_separated = " ".join(foot_bones)
print("Space Separated: ",space_separated)

