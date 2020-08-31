# Final Task Module 3

def word_mixer(word_list):
    word = ""
    word_list_sorted = sorted(word_list)
    new_words = []

    #print(words_list)
    # initializing the length
    words_list_len = len(word_list_sorted)

    #print(word_list_sorted)
    while words_list_len > 5:

        word = word_list_sorted.pop(-5)
        new_words.append(word)

        word = word_list_sorted.pop(0)
        new_words.append(word)
        
        word = word_list_sorted.pop()
        new_words.append(word)


        words_list_len = len(word_list_sorted)
        
    
    return new_words


print("Mixer words!")
poem = input("Please insert a poem: ")

words_list = poem.split()
words_list_len = len(words_list)

for count in range(0,words_list_len):
    
    if len(words_list[count]) <= 3:
        words_list[count] = words_list[count].lower()
    else:
        words_list[count] = words_list[count].upper()



word_already_mixed = word_mixer(words_list)

mixed_sentence = " ".join(word_already_mixed)
print("New values:\n",mixed_sentence)


