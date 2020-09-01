# Examples: Importing files in Jupyter Notebooks

print ("\n\n### Task 1 ###\n\n")
# use readline to get rainbow colors
#   - import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow as rainbow.txt
#   - open rainbow.txt as rainbow_file as read-only
#   - read the first 3 lines into variables: color1, color2, color3
#   - close rainbow_file
#   - print the first 3 colors


# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow as rainbow.txt
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt

# [ ] open rainbow.txt as rainbow_text
rainbow_text = open('rainbow.txt','r')

# [ ] read the first 3 lines into variables: color1, color2, color3
color1 = rainbow_text.readline()
color2 = rainbow_text.readline()
color3 = rainbow_text.readline()

# [ ] close rainbow.txt
rainbow_text.close()

# [ ] print the first 3 colors
print(color1 + color2 + color3)



print ("\n\n### Task 2 ###\n\n")
# while .readline() rainbow colors¶
# assumes rainbow.txt has been imported in task 1
#   - open rainbow.txt as rainbow_file as read-only
#   - read a color from each line of rainbow_file in a while loop
#       - print each color capitalized
#   - close rainbow_file

# [ ] open rainbow.txt as rainbow_text as read-only
rainbow_text = open('rainbow.txt','r')

# [ ] read the color from lines of rainbow_text in a while loop
# [ ] print each color capitalized as the loop runs
color_line = rainbow_text.readline()

while color_line:
    print(color_line[:-1].title())
    color_line = rainbow_text.readline()

# [ ] close rainbow_text 
rainbow_text.close()


print ("\n\n### Task 3 ###\n\n")
# .readline() with .strip() rainbow colors
# assumes rainbow.tx has been imported in task 1
#   - open rainbow.txt as rainbow_file as read-only
#   - read a color from each line of rainbow_file in a while loop
#       - use .strip to remove the whitespace
#       - print each color upper case
#   - close rainbow_file

# [ ] open rainbow.txt as rainbow_text as read-only  
rainbow = open('rainbow.txt','r')

# [ ] read a color from each line of rainbow_text in a while loop  
# use .strip to remove the whitespace '\n' character 
# print each color upper case 
rainbow_line = rainbow.readline().strip().title()

while rainbow_line:
    print(rainbow_line)
    rainbow_line = rainbow.readline().strip().title()
    
rainbow.close()


print ("\n\n### Task 4 ###\n\n")
# .strip() with arguments
#   - run import of cities_messy.txt below at least once this notebook session
#   - run open cities_messy.txt below before each test of the while loop cell
#   - edit while loop to strip the colon ':' , newline and spaces
#   - close cities_messy

# [ ] import the file
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities_messy -o cities_messy.txt

# [ ] run to read the file into memory
cities_messy = open('cities_messy.txt', 'r')

# [ ] edit the code to remove leading or trailing colon, newline and space characters
line = cities_messy.readline().strip(':\n\s')

while line:
    print(line)
    line = cities_messy.readline().strip(':\n\s')


cities_messy.close()


print ("\n\n### Task 5 ###\n\n")
# .strip() parentheses from poem2_messy¶
#   - import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy as poem2_messy.txt
#   - open poem2_messy.txt as poem2_messy in read mode
#   - edit while loop to strip the leading and trailing parentheses & print the poem without blank lines
#   - close poem2_messy

# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy as poem2_messy.txt  
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy -o poem2_messy.txt

# [ ] open poem2_messy.txt as poem2_messy in read mode
poem2_messy = open('poem2_messy.txt','r')

# [ ] edit while loop to strip the leading and trailing parentheses, and newlines
# [ ] print the poem 
line = poem2_messy.readline().strip(')(\n')

while line:
    print(line)
    line = poem2_messy.readline().strip(')(\n')

poem2_messy.close()


