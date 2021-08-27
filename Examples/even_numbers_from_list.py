# List Comprehensions Solutions

# Exercise 7

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even 
# elements of this list in it.

import random

random_list = []
limit_random =25
len_random = random.randint(0,limit_random)

list_numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list_even_numbers = [number for number in list_numbers if number % 2 == 0]

print("List of even numbers in fixed list:\n")
print(list_even_numbers)


for i in range(0,len_random):
    random_list.append(random.randint(0,limit_random))

list_even_numbers2 = [number for number in random_list if number % 2 == 0]
print("\nList of even numbers in random list:\n")
print(list_even_numbers2)

#print("List of even numbers in fixed list:\n" +list_even_numbers2)