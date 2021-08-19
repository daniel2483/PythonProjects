print ("\n\n### Last Exercises Module 3 ###\n\n")
print ("\n\n### Task 1 ###\n\n")
# Order the Rainbow
# Open the rainbow file then put in a list and print in alphabetical order

# Download and open the file.

#   - Download list of rainbow colors, as rainbow.txt, using curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow
#   - Open rainbow.txt in read mode using a variable: rainbow_file

# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow as rainbow.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt

#   - Read rainbow_file as a list variable: rainbow_colors using .readlines()

# [ ]  Open rainbow.txt in read mode & read as list with .readlines()
rainbow_text = open('rainbow.txt','r')
rainbow_lines = rainbow_text.readlines()
print(rainbow_lines)

#   1. Sort the rainbow_lines list alphabetically.
#   2. Print each line of rainbow_lines by iterating the sorted list.
#   3. Close rainbow_file.

# [ ] sort rainbow_colors list, iterate the list to print each color
rainbow_lines.sort()
print(rainbow_lines,"\n")

for line in rainbow_lines:
    print(line[:-1])

rainbow_text.close()


print ("\n\n### Task 2 ###\n\n")
# The Weather
# Create a program that reads from a file to display city name and average temperature in Celsius. 
#   - use !curl to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv as mean_temp.txt

# [ ] The Weather: import world_mean_team.csv as mean_temp.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt

#   1. Open the file in 'r' mode.
#   2. Read the first line of text into a variable called: headings and print().
#   3. Convert headings to a list using .split(',') which splits on each comma, print() the list.

# [ ] The Weather: open file, read/print first line, convert line to list (splitting on comma)
weather_file = open('mean_temp.txt','r')
headings = weather_file.readline()
print(headings,"\n")
headings = headings.split(",")
print(headings)

# use a while loop to read the remaining lines from the file

#   1. Assign remaining lines to a city_temp variable.
#   2. Convert the city_temp to a list using .split(',') for each .readline() in the loop.
#   3. Print each city & the highest monthly average temperature.
#   4. Close mean_temps.

#       Tips & Hints:

#           - Use the print output of headings to determine the city_temp indexes to use.
#           - "month ave: highest high" for Beijing is 30.9 Celsius.
#           - Convert city_temp to lists with .split(',').

# [ ] The Weather: use while loop to print city and highest monthly average temp in celsius
while headings:
    city_temp = weather_file.readline()
    #print(city_temp[:-1])
    city_temp = city_temp.split(',')
    try:
        print("City: ",city_temp[0]," Highest Monthly Average Temperature: ", city_temp[2])
    except IndexError:
        break



print ("\n\n### Task 3 ###\n\n")
# Random pi guessing¶
# Create random appearing numbers by reading digits of pi Note: only "appears" random
#   - Download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi as pi.txt

# [ ] use curl to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi as pi.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o pi.txt

# Set up the project files and intitial values

#   1. Open pi.txt in read mode, the file has a single line of text "3.14....".
#   2. Get user name as input and say "hi".
#   3. Use the length of name for variable called seed.
#   4. Use .seek() with the value of seed to set the initial pointer location reading the file.
#   5. Create a variable digit and assign it the value of reading one character from the file.
#   6. Get guess variable value from users input - "enter a single digit guess or "q" to quit".
#   7. Initialize correct and wrong counter variables to 0 (zero).

# [ ] Set up the project files and initial values
pi = open('pi.txt','r')
username = input("Hi! ")
seed = len(username)
pi.seek(seed - 1,0)
correct = 0
wrong = 0
#print(pi.read())
for digit in pi.read():
    #print(digit)
    guess = input("Enter a single digit guess or 'q' to quit: ")
    if guess == "q":
        break
    elif digit == guess:
        correct += 1
    else:
        wrong += 1

#print("Wrong answers: ",wrong)
#print("Correct answers: ",correct)

# Create a while loop that tests that guess is a digit string

# then in the loop:

#   1. if digit ( read from pi file) is "." read the next character for digit
#   2. else if digit is "\n" increment seed and use seed to set the pointer uing .seek()
#   3. else see if guess is equal to digit
#       a. if guess equals digit: print "correct" and increment the varible named correct
#       b. if guess not equal digit: print "incorrect" and increment the variable named wrong

# end the while loop when user enters any non-digit(s) for guess, like "q".

#   - Print correct and wrong values within a message to the user.
#   - Close the pi file.

correct = 0
wrong = 0
#print(pi.read())
for digit in pi.read():
    #print(digit)
    if digit == ".":
        next
    elif digit == "\n":
        pi.seek(1,0)
        
    guess = input("Enter a single digit guess or 'q' to quit: ")
    if guess == "q":
        break
    elif digit == guess:
        print("correct!")
        correct += 1
    else:
        print("wrong!")
        wrong += 1

print("Wrong answers: ",wrong)
print("Correct answers: ",correct)

pi.close()



