# Examples: Importing files in Jupyter Notebooks
# [ ] review and run example
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt


print ("\n\n### Task 1 ###\n\n")
# Task for Jupyter Notebooks
# [ ] import cities.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
# [ ] open cities.txt as cities_file
# [ ] test cities.txt was opened 
cities = open('cities.txt', 'r')
cities

print("\n\n")


print ("\n\n### Task 2 ###\n\n")
# [ ] after import and open of cities.txt in task 1
# [ ] read cities_file as cities
# [ ] display the string: cities
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt
cities = cities.read()

print("\n\n")
# [ ] print the string: cities
print(cities)


print ("\n\n### Task 3 ###\n\n")
# [ ] digits of pi
# 1. import digits_of_pi.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o digits_of_pi.txt

# [ ] digits of pi
# 2. open as digits_of_pi_text 
# 3. read() 4 char of digits_of_pi_text to pi_digits variable 
# 4. print pi_digits  
digits_of_pi_text = open('digits_of_pi.txt', 'r')
pi_4_digits = digits_of_pi_text.read(4)
print("Pi 4 digits: ",pi_4_digits)

# [ ] digits of pi
# 5. add to pi_digits string with string addition  
#   a. add next 4 characters from digits_of_pi obtained from read()  
#   b. run the cell multiple times to get more digits of *pi*
pi_4_digits = pi_4_digits + digits_of_pi_text.read(4)
print("Pi digits: ",pi_4_digits)

print ("\n\n### Task 4 ###\n\n")
# City Initials
# Read the file cities.text that was imported in task 1
#   1- ensure the code was created and run in task 1 to import cities.txt
#   2- create and run code to re-open cities.txt as cities_file
#   3- read() cities_file into a variable called cities
#   4- iterate through the characters in cities a. test if .isupper(), if True append the character to a string variable: initials c. else if (elif) character is "\n", if True append the "\n" to initials
#   5- print initials
cities_file = open('cities.txt', 'r')
cities_file = cities_file.read()
print(ciites_file)

cities_list = cities_file.split("\n")
print(cities_list)
initials = ""

for city in cities_list:
    if city != "":
        for city_letters in city:
            if city_letters.isupper():
                initials += city_letters + "\n"


print("Initials: ",initials)
                




