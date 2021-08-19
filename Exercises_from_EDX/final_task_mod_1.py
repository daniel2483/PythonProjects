# [] create words after "G"
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
#quote = "Wheresoever you go, go with all your heart"
quote = input("Insert a quote: ")
quote = quote + " "


word = ""
alphabetic = 'abcdefghijklmnopqrstuvwxyz'

for letter in quote:
    if letter.isalpha() == True:
        word = word + letter
    else:
        if word != "":
            #print(word)
            for alpha in alphabetic[7:28]:
                #print (alpha)
                if word[0].lower() == alpha:
                    print (word.upper())
                    word = ""
                    break
            word=""
