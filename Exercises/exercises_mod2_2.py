# [ ] create and populate list called days_of_week then print it

print("\n\n### Task 1 ###\n")

days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

print ("Days Selected: ",days_of_week[1]," - ",days_of_week[3]," - ",days_of_week[5])

# [ ] create and populate list called phone_letters then print it

print("\n\n### Task 2 ###\n")

phone_letters = [" ","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

print ("Phone Letters List: ",phone_letters)


print("\n\n### Task 3 ###\n")

day = days_of_week[1]
print("Day: ",day)


day = days_of_week[5]
print("Day: ",day)


print("\n\n### Task 4 ###\n")

days_of_week.append("Newday")

# If I keep running the command above will add more Newdays at the end of the list
# To return to the initial I can use pop,del or remove to get the initial state

days_of_week.insert(3,"Newday")
print("New List: ", days_of_week)

days_of_week.insert(6,"Newday")
print("New List: ", days_of_week)

# Delete from a list
# `del` & `.pop()` some bad ideas
# exercises below assume days_of_week appended/inserted 3 extra days in previous exercises

# [ ] print days_of_week 
# [ ] modified week is too long - pop() the last index of days_of_week & print .pop() value
# [ ] print days_of_week

print("\n\n### Task 5 ###\n")

print("Current List: ", days_of_week)
days_of_week.pop()
print("New List: ", days_of_week)

# [ ] print days_of_week 
# [ ] delete (del) the new day added to the middle of the week 
# [ ] print days_of_week


print("Current List: ", days_of_week)
del days_of_week[3]
print("New List: ", days_of_week)

# [ ] print days_of_week 
# [ ] programmers choice - pop() any day in days_of week & print .pop() value
# [ ] print days_of_week

choice = input("Select Day of week(from 1 to 7): ")

choice = int(choice) - 1

print("Day selected: ",days_of_week.pop(choice))



print("\n\n### Task 6 ###\n")

phone_letters = [" ","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

def let_to_num(letter):
    key = 0
    while key < 10:
        #print ("Key Number: ",key)
        #print ("Key number: ",key," | String Letter:",phone_letters[key])
        
        if letter in phone_letters[key]:
            return key
        
        key += 1
        #print (key)
    return "Not Found"
    
input_string = input("Enter a string: ")

number_phone = ""
for letters in input_string:
    #print (letters)
    number_phone = let_to_num(letters.upper())
    print (number_phone)

if input_string == "":
    print (1)
    
#print (number_phone)
#if "e" in "open":
#    print("e found")
#else:
#   print("e not found")


## Reverse a string

print("\n\n### Challenge ###\n")

input_string = input("Enter a string: ")
list = []

if input_string != "":
    for letters in input_string:
        list.insert(0,letters)
        print ("This is a list:\n",list)

reverse_string = ""
for letters in list:
    reverse_string += list.pop(0)
    print (reverse_string)

print ("Reverse String: " + reverse_string)







