print ("\n\n### Task 1 ###\n\n")
# [ ] extend the list common_birds with list birds_seen which you must create
common_birds = ["chicken", "blue jay", "crow", "pigeon"]

common_birds.extend(["duck","cysne","eagle"])

print("List of common birds",common_birds)
# [ ] Create 2 lists zero_nine and ten_onehundred that contain 1-9, and 10 - 100 by 10's.
# [ ] use list addition to concatenate the lists into all_num and print

zero_nine = []
ten_onehundred=[]

for count in range(0,10):
    #print(count)
    zero_nine.append(count)

print ("Zero to Nine list: ",zero_nine)

for count in range(10,101,10):
    #print(count)
    ten_onehundred.append(count)

print ("Ten to One hundred list: ",ten_onehundred)

all_numbers = zero_nine + ten_onehundred

print("All numbers: ",all_numbers)


print ("\n\n### Task 2 ###\n\n")
# [ ] create and  print a list of multiples of 5 from 5 to 100
# { ] reverse the list and print

five_multiple = []
for count in range(5,101,5):
    #print(count)
    five_multiple.append(count)

print("Five multiples: ",five_multiple)
five_multiple.reverse()
print("Reverse List:",five_multiple)


# [ ] Create two lists: fours & more_fours containing multiples of four from 4 to 44
# [ ] combine and print so that the output is mirrored [44, 40,...8, 4, 4, 8, ...40, 44]
four_multiple = []
copy_four_multiple =[]
for count in range(4,45,4):
    #print(count)
    four_multiple.append(count)
    copy_four_multiple.append(count)

print("Four multiples: ",four_multiple)

#copy_four_multiple = four_multiple
print("Four multiples copy: ",copy_four_multiple)
four_multiple.reverse()
print("Reverse Four multiples: ",four_multiple)
#copy_four_multiple.reverse()
new_output = four_multiple + copy_four_multiple
print("New output list: ",new_output)



print ("\n\n### Task 3 ###\n\n")
# [ ] print cites from visited_cities list in alphbetical order using .sort()
# [ ] only print cities that names start "Q" or earlier
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
print("Cities not sorted: ",visited_cities)
visited_cities.sort()
print("Cities sorted: ",visited_cities)


# [ ] make a sorted copy (sorted_cities) of visited_cities list
# [ ] remove city names 5 characters or less from sorted_cities 
# [ ] print visitied cites and sorted citiesn
print("\n\n")
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
print("Complete Not Sorted List: ",visited_cities)
sorted_cities = sorted(visited_cities)
print("Complete Sorted List: ",sorted_cities)

for city in sorted_cities:
    #print (len(city))
    if len(city) <= 5:
        sorted_cities.remove(city)

print("\n\nComplete Not Sorted List: ",visited_cities)
print("Complete Sorted List: ",sorted_cities)


print ("\n\n### Task 4 ###\n\n")
# Program: Merge & Sort Animals
# Create a program that:

#       takes user to build a list: add_animals
#       merges add_anmials with exisiting list: anmimals
#       provides a sorted list to view in alpa or reverse alpha order
animals=["lion","zebra"]
add_animals = []
print("Animals in list: ",animals)
new_animal = "init"
while new_animal != "":
    new_animal= input ("Add new animal: ")
    if new_animal != "":
        add_animals.append(new_animal)

animals.extend(add_animals)
print("New Animals list: ",animals)
animals.sort()
print("New Animals list sorted: ",animals)
animals.reverse()
print("New Animals list sorted reverse: ",animals)

