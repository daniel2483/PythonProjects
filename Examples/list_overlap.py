#  List Overlap
# Exercise 5 (and Solution)

# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common 
# between the lists (without duplicates). Make sure your program works on two lists of 
# different sizes.

# Extras:

# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python (don’t worry if you can’t figure this out at this 
# point - we’ll get to it soon)

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



new_list =[]

for num in a:
    if num in b:
        new_list.append(num)

print("This is the new list which has the same values in a and b fixed list")
print("\nList in a: "+str(a))
print("\nList in b: "+str(b))
print("\nNew List c: "+str(list(set(new_list))))
print("\n\n")
print("This is the new list which has the same values in a and b random list")

limit_random =100

len_random = random.randint(0,limit_random)
#print(str(len_random))
d =[]
e =[]
new_list2 =[]
for i in range(0,len_random):
    d.append(random.randint(0,limit_random))

len_random = random.randint(0,limit_random)
for i in range(0,len_random):
    e.append(random.randint(0,limit_random))

for num in d:
    if num in e:
        new_list2.append(num)

print("\nList in d: "+str(d))
print("\nList in e: "+str(e))
print("\nNew List f: "+str(list(set(new_list2))))