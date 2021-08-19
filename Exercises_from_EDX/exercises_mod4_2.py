# Examples: Importing files in Jupyter Notebooks

print ("\n\n### Task 1 ###\n\n")
# .readlines()
#   1. Import a list of cities using curl
#       a.git the list from https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities
#       b. name the list cities.txt
#   2. Open cities.txt in read mode using a variable: cities_file
#   3. Read cities_file as a list variable: cities_lines using .readlines()
#   4. Print each line of cities_lines by iterating the list

# [ ] import cities
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
cities_file = open('cities.txt','r')

cities_lines = cities_file.readlines()
for city in cities_lines:
    print(city)


print ("\n\n### Task 2 ###\n\n")
# remove newline characters from cities lists created using .readlines()¶
#   - This task assumes that cites.txt has been imported in Task 1 above
#   - In task 1, the cities were printed with a blank line between each city - this task removes the blank lines
# [ ] re-open file and read file as a list of strings 

# [ ] open cities.txt as cities_file and read the file as a list: cities_lines
cities_file = open('cities.txt','r')
cities_lines = cities_file.readlines()

# [ ] remove the last character, "\n", of each cities_lines list item 
count = 0

for line in cities_lines:
    cities_lines[count] = line[:-1]
    count += 1

# [ ] print each list item in cities_lines
for line in cities_lines:
    print(line)


print ("\n\n### Task 3 ###\n\n")
# File .close()
# write each item in it's own cell
#   - open cities.txt as cities_file
#   - read the lines as cities_lines
#   - print the cities that start with the letter "D" or greater
#   - close cities_file
#   - test that file is closed

# [ ] open cities.txt as cities_file
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
cities_file = open('cities.txt', 'r')

# [ ] read the lines as cities_lines
cities_lines = cities_file.readlines()

# [ ] print the cities that start with the letter "D" or greater
alphabetic = "abcdefghijklmnopqrstuvwxyz"
for l in cities_lines:
    #print(l)
    for letters in alphabetic[3:27]:
        #print(l[0])
        if l[0].lower() == letters:
            print("City Name: ",l)

# [ ] test that file is closed
print(cities_file)

# [ ] close cities_file
cities_file.close()


print ("\n\n### Task 4 ###\n\n")
#   readlines() poem2
#   write each item in its own cell
#   - import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt as poem2.txt
#   - open poem2.txt as poem2_file in read mode
#   - create a list of strings, called poem2_lines, from each line of poem2_text (use .readlines())
#   - remove the newline character for each list item in poem2_lines
#   - print the poem2 lines in reverse order

# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt as poem2.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt -o poem2.txt

# [ ] open poem2.txt as poem2_text in read mode
poem2_text = open('poem2.txt','r')

# [ ] create a list of strings, called poem2_lines, from each line of poem2_text
poem2_lines = poem2_text.readlines()

# [ ] remove the newline character for each list item in poem2_lines
count = 0

for line in poem2_lines:
    poem2_lines[count] = line[:-1]
    count += 1
print(poem2_lines)

# [ ] print the poem2 lines in reverse order
poem2_lines.reverse()
print(poem2_lines)


