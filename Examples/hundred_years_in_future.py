# Character Input

# input strings types int

# Calibrating the exercises to the audience is going to be a challenging task, so I ask you 
# to bear with me if the exercises are too easy or too hard. Every week there will be a poll 
# you can click on to discuss whether the exercise is too easy or too hard and hopefully in 
# a few weeks, I’ll get the level right. Let’s get to it! I will start with the exercise and 
# include a discussion later, in case you want the extra challenge.

# Exercise 1 (and Solution)

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years
# old.

# Extras:
# 1. Add on to the previous program by asking the user for another number and printing out
# that many copies of the previous message. (Hint: order of operations exists in Python)
# 2.Print out that many copies of the previous message on separate lines. (Hint: the string
# "\n is the same as pressing the ENTER button)

import sys
from datetime import datetime

name = input("Please enter your name: ")

try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Error, invalid age should be an integer number...")
    sys.exit()

try:
    copies = int(input("How many copies do you want? "))
except ValueError:
    print("Error, invalid number of copies should be an integer number...")
    sys.exit()

years_to_add = 100 - age
#print("Years to add: " + str(years_to_add))
today = datetime.today()
current_year = today.strftime("%Y")
#print ("Current Year: " + str(current_year))
year_in_future = int(current_year)+years_to_add

times = name + ", you will have a 100 years in: " + str(year_in_future) + "\n"

#for times in range(0,copies):
    #print (name + ", you will have a 100 years in: " + str(year_in_future))

print(copies*times)