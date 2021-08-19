print ("\n\n### Task 1 ###\n\n")
# [ ] for x = 6, use range(x) to print the numbers 1 through 6
x = 6
for count in range(100):
    if count <= x:
        print (count)
    else:
        break

# [ ] using range(x) multiply the numbers 1 through 7
# 1x2x3x4x5x6x7 = 5040
result = 1
for count in range(1,8):
    result=result*count
    print(result)
    
print(result)

# [ ] print the second half of a spelling list using a range(stop) loop to iterate the list
spell_list = ["Wednesday", "Tuesday", "February", "November", "Annual", "Calendar", "Solstice"]
length = len(spell_list)
half=int(length/2)
#print(half)

for word in range(half,length):
    print(spell_list[word])

print ("\n\n### Task 2 ###\n\n")
# [ ] using range(start,stop), .append() the numbers 5 to 15 to the list: five_fifteen
# [ ] print list five_fifteen
numbers = []
for count in range(5,16):
    numbers.append(count)
print(numbers)


# [ ] using range(start,stop) - print the 3rd, 4th and 5th words in spell_list
# output should include "February", "November", "Annual"
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
for count in range(2,5):
    print(spell_list[count])

# [ ] using code find the index of "Annual" in spell_list
# [ ] using range, print the spell_list including "Annual" to end of list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
length = len(spell_list)
for count in range(0,length):
    string = ""
    if spell_list[count] == "Annual":
        #print("Found")
        string = "Is found"
    print(spell_list[count]," ",string)


print ("\n\n### Task 3 ###\n\n")
# [ ] print numbers 10 to 20 by 2's using range
for numbers in range(10,21,2):
    print(numbers)

# [ ] print numbers 20 to 10 using range (need to countdown)
# Hint: start at 20
for numbers in range(20,9,-1):
    print(numbers)

# [ ] print first and every third word in spell_list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

for word in range(0,9,3):
    print(spell_list[word])

print ("\n\n### Task 4 ###\n\n")
# [ ] complete List of letters program- test with the word "complexity"
words=input("Enter a string: ")
length = len(words)

for letter in range(0,length):
    print("Letters: ",words[letter])

for letter in range(0,length,2):
    print("Odd letters: ",words[letter])

for letter in range(1,length,2):
    print("Even letters: ",words[letter])

print ("\n\n### Task 5 ###\n\n")
# [ ] fix the error printing odd numbers 1 - 9
for num in range(1,10,2):
    print(num)
