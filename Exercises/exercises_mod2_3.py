print ("\n\n### Task 1 ###")
# replace items in a list
#   - create a list, three_num, containing 3 single digit integers
#   - print three_num
#   - check if index 0 value is < 5
#       - if < 5 , replace index 0 with a string: "small"
#       - else, replace index 0 with a string: "large"
#   - print three_num
three_num = [4,6,7]
print("Three Numbers: ",three_num)
if three_num[0] < 5:
    three_num[0] = "small"
else:
    three_num[0] = "large"
print("Three Numbers: ",three_num)

print("\n\n")
# Function Challenge: create replacement function
#   - Create a function, str_replace, that takes 2 arguments: int_list and index
#       - int_list is a list of single digit integers
#       - index is the index that will be checked - such as with int_list[index]
#   - Function replicates purpose of task "replace items in a list" above and replaces an integer with a string "small" or "large"
#   - return int_list

#   Test the function!


# [ ]  create challenge function
int_list =[23,55,1,55,6,7,9,13,35]
def str_replace(ori_list,index):
    #print("Original List: ",int_list)
    if ori_list[index] < 5:
        ori_list[index] = "small"
    else:
        ori_list[index] = "large"
    #print("Replacement List: ",int_list)
    return ori_list

print("Original List: ",int_list)
new_list = str_replace(int_list,3)
print("New List: ",new_list)
    



print ("\n\n### Task 2 ###")
# modify items in a list
#   - create a list, three_words, containing 3 different capitalized word stings
#   - print three_words
#   - modify the first item in three_words to uppercase
#   - modify the third item to swapcase
#   - print three_words

# [ ] complete coding task described above
three_words = ["Big","sMAll","mediUM"]
print("Word list: ",three_words)
three_words[0] = three_words[0].upper()
three_words[2] = three_words[2].swapcase()
print("Edited Word list: ",three_words)

print ("\n\n### Task 3 ###")
# [ ] insert a name from user input into the party_list in the second position (index 1)
party_list = ["Joana", "Alton", "Tobias"]
print("Party List: ",party_list)
party_list.insert(1,"Daniel")
# [ ] print the updated list
print("New Party List: ",party_list)


print ("\n\n### Task 4 ###")
# [ ] Fix the Error
tree_list = ["oak"]
print("tree_list before =", tree_list)
tree_list.insert(1,"pine")
print("tree_list after  =", tree_list)
