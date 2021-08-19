print ("\n\n### Task 1 ###")
# [ ] slice long_word to print "act" and to print "tic"
long_word = "characteristics"
print("First Slice: " + long_word[4:7])
print("Second Slice: " + long_word[11:14])

print ("\n\n")
# [ ] slice long_word to print "sequence"
long_word = "Consequences"
print("Word: " + long_word[3:11])   


print ("\n\n### Task 2 ###")
# [ ] print the first half of the long_word
long_word = "Consequences"
print("Half word: " + long_word[:6])


print ("\n\n### Task 3 ###")
# [ ] print the second half of the long_word
long_word = "Consequences"
print("Second Half: " + long_word[6:])

print ("\n\n### Task 4 ###")
# [ ] print the 1st and every 3rd letter of long_word
long_word = "Acknowledgement"
print(long_word[1::3])

print ("\n\n")
# [ ] print every other character of long_word starting at the 3rd character
long_word = "Acknowledgement"
print(long_word[2::2])
print(long_word[3::])


print ("\n\n### Task 5 ###")
# [ ] reverse long_word
long_word = "stressed"
print(long_word[::-1])

print ("\n\n")
# [ ] print the first 5 letters of long_word in reverse
long_word = "characteristics"
print(long_word[4::-1])


print ("\n\n### Task 6 ###")
# [ ] print the first 4 letters of long_word
# [ ] print the first 4 letters of long_word in reverse
# [ ] print the last 4 letters of long_word in reverse
# [ ] print the letters spanning indexes 3 to 6 of long_word in Reverse
long_word = "timeline"
print(long_word[:4])
print(long_word[3::-1])
print(long_word[:3:-1])
print((long_word[2:6])[::-1])

