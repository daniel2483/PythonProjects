print ("\n\n### Task 1 ###")
# [ ] use len() to find the midpoint of the string 
# [ ] print the halves on separate lines
random_tip = "wear a hat when it rains"
len_word = len(random_tip)
half = int(len_word/2)
print (random_tip[:half])
print (random_tip[half:])

print ("\n\n### Task 2 ###")
# for letters: "e" and "a" in random_tip
# [ ] print letter counts 
# [ ] BONUS: print which letter is most frequent
random_tip = "wear a hat when it rains"
print ("Letter e: ", random_tip.count("e"))
print ("Letter a: ", random_tip.count("a"))
if (int(random_tip.count("e"))>int(random_tip.count("a"))):
    print ("Letter e is higher")
elif (int(random_tip.count("e"))<int(random_tip.count("a"))):
    print ("Letter a is higher")
else:
    print ("Both equals")


print ("\n\n### Task 3 ###")
# [ ] print long_word from the location of the first and second "t"
long_word = "juxtaposition"
index1 = long_word.find("t")
#print (index)
print ("First Index: ",index1);


index2 = long_word.find("t", index1 + 1)
print ("Second Index: ", index2)

print(long_word[index1:index2+1])

print ("\n\n### Task 4 ###")
# [ ] Print each word in the quote on a new line  
quote = "they stumble who run fast"
index = quote.find(" ")

print (quote[0:index])

while index >0:
    #print("Blank space at index =", index)
    previous = index;
    index = quote.find(" ", index + 1)
    print (quote[previous+1:index])
#print("no more blank spaces")
