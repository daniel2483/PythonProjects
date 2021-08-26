# Odd Or Even
# input if types int equality comparison numbers mod

# Again, the exercise comes first (with a few extras if you want the extra challenge or 
# want to spend more time), followed by a discussion. Enjoy!

# Exercise 2 (and Solution)

# Ask the user for a number. Depending on whether the number is even or odd, print out an 
# appropriate message to the user. Hint: how does an even / odd number react differently 
# when divided by 2?

# Extras:
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to 
# divide by (check). If check divides evenly into num, tell that to the user. If not, print 
# a different appropriate message.

loop = 0

while loop == 0:
    try:
        number = int(input("Please enter a number to see if is even or odd: "))
        loop = 1
    except ValueError:
        loop = 0
        print("Value is not an integer")

if number%2 == 1:
    print ("This number: "+str(number)+" is an odd")
if number%2 == 0:
    if number%4 == 0:
        print ("This number: "+str(number)+" is an even and can be divided by four.")
    else:
        print ("This number: "+str(number)+" is an even and can't be divided by four.")

loop = 0
while loop == 0:
    try:
        num = int(input("Please enter an integer number: "))
        check = int(input("Please enter an integer number to do a division: "))
        
        loop = 1
    except ValueError:
        loop = 0
        print("Value is not an integer")