#  List Less Than Ten
# list numbers elements if conditional
# Exercise 3 (and Solution)

# Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# 1. Instead of printing the elements one by one, make a new list that has all the elements 
# less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the 
# original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 99, 101, 104]
leng_a = len(a)
b = []
c = []

#print(str(leng_a))
for value in range(leng_a):
    if (a[value] < 5):
        print(a[value])

print("\n\n")

for value in range(leng_a):
    if (a[value] < 5):
        #print(a[value])
        b.append(a[value])

print("The array with values less than 5 is: ")
print(b)

try:
    number = int(input("Enter a number: "))
    for value in range(leng_a):
        if (a[value] < number):
            #print(a[value])
            c.append(a[value])
    print("The array with values less than "+str(number) +" is: ")
    print(c)
except ValueError:
    print("The value enter is not a integer number...")
