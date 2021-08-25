words = ["He","Flower","Banana","Hello","Hala","Rogar", "Rymes","argon","Row","Telon","Test","Rear","Roast","Hi","Hangar"]

letter_dict = {"a" : 0,"b" : 0,"c" : 0,"d" : 0,"e" : 0,"f" : 0,"g" : 0,
  "h" : 0,"i" : 0,"j" : 0,"k" : 0,"l" : 0,"m" : 0,"n" : 0,"o" : 0,"p" : 0,
  "q" : 0,"r" : 0,"s" : 0,"t" : 0,"u" : 0,"v" : 0,"w" : 0,"x" : 0,"y" : 0,
  "z" : 0
}

for word in words:
    first_letter = word[:1].lower()
    number = letter_dict[first_letter]
    letter_dict[first_letter] = number + 1

number_of_times = max(letter_dict["a"],
       letter_dict["b"],
       letter_dict["c"],
       letter_dict["d"],
       letter_dict["e"],
       letter_dict["f"],
       letter_dict["g"],
       letter_dict["h"],
       letter_dict["i"],
       letter_dict["j"],
       letter_dict["k"],
       letter_dict["l"],
       letter_dict["m"],
       letter_dict["n"],
       letter_dict["o"],
       letter_dict["p"],
       letter_dict["q"],
       letter_dict["r"],
       letter_dict["s"],
       letter_dict["t"],
       letter_dict["u"],
       letter_dict["v"],
       letter_dict["w"],
       letter_dict["x"],
       letter_dict["y"],
       letter_dict["z"])

#print ("The letter more frequent: ")
#print (number_of_times)
#print("\n")

for letter in letter_dict:
    if letter_dict[letter] == number_of_times:
        print("Letter '",letter,"' are the most frequent which are present",number_of_times,"time(s)")