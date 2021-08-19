print ("\n\n### Task 1 ###")
# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] reprint list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
print("Foot bones list: ",ft_bones)
del ft_bones[2]
print("Foot bones list after deletion: ",ft_bones)

print("\n\n")
print ("\n\n### Task 2 ###")
# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] delete "navicular" from list
# [ ] reprint list
# [ ] check for deletion of "cuboid" and "navicular"
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
print("Foot bones list: ",ft_bones)
del ft_bones[2]
del ft_bones[2]
print("Foot bones list after deletion: ",ft_bones)

print ("\n\n### Task 3 ###")
# pop()
# [ ] pop() and print the first and last items from the ft_bones list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
print("First Item: ",ft_bones.pop(0))
print("Last Item: ",ft_bones.pop())
# [ ] print the remaining list
print("Remaining list: ",ft_bones)

print ("\n\n### Task 4 pt 1 ###")
# Cash Register Input
#   - create a empty list purchase_amounts
#   - populate the list with user input for the price of items
#   - continue adding to list with while until "done" is entered
#       - can use while True: with break
#   - print purchase_amounts
#   - continue to pt 2

#[ ] complete the Register Input task above
purchase_amounts = []
prices = ""
while prices.lower() != "done":
    prices = input("Enter a price (to exit write 'Done'): $")
    if prices.isnumeric():
        purchase_amounts.append(prices)

print("Prices List: ",purchase_amounts)

print ("\n\n### Task 4 pt 2 ###")
# Cash Register Total¶
#   - create a subtotal variable = 0 create a while loop that runs while purchase_amount (is not empty)
#   - inside the loop
#       - pop() the last list value cast as a float type
#       - add the float value to a subtotal variable
#   - after exiting the loop print subtotal

# be sure to populate purchase_amounts by running pt 1 above

# [ ] complete the Register Total task above
subtotal = 0
length = len(purchase_amounts)
count = 0
while count < length:
    #print(purchase_amounts)
    as_float = float(purchase_amounts.pop())
    print(as_float)
    subtotal += as_float
    count += 1

print("Subtotal: ",subtotal)
    

print ("\n\n### Task 5 ###")
# .remove()
# [ ] remove one "Poodle" from the list: dogs , or print "no Poodle found"
# [ ] print list before and after
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]
print("List before: ", dogs)

try:
    dogs.remove("Poodle")
    print("List after: ", dogs)
except ValueError:
    print("no Poodle found")

try:
    dogs.remove("Poodle")
    print("List after: ", dogs)
except ValueError:
    print("no Poodle found")

try:
    dogs.remove("Poodle")
    print("List after: ", dogs)
except ValueError:
    print("no Poodle found")
    
try:
    dogs.remove("Poodle")
    print("List after: ", dogs)
except ValueError:
    print("no Poodle found")

try:
    dogs.remove("Poodle")
    print("List after: ", dogs)
except ValueError:
    print("no Poodle found")


