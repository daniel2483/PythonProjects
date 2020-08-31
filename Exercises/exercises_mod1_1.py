print ("\n\n### Task 1 ###")
# [ ] assign a string 5 or more letters long to the variable: street_name
street_name  = "Laureles"
# [ ] print the 1st, 3rd and 5th characters
print(street_name[0])
print(street_name[2])
print(street_name[4])

print ("\n\n")
# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
team_name = "Pistols"
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else
if (team_name[1].lower() == "i"):
    print ("Team second letter is i")
elif (team_name[1].lower() == "o"):
    print ("Team second letter is o")
elif (team_name[1].lower() == "u"):
    print ("Team second letter is u")
else:
    print ("Team Name don't have i,o or u in second letter!")


print ("\n\n### Task 2 ###")
# [ ] assign a string 5 or more letters long to the variable: street_name
street_name = "Bellavista"
# [ ] print the last 3 characters of street_name
print (street_name[-3]+street_name[-2]+street_name[-1])

print ("\n\n")
# [ ] create and assign string variable: first_name
first_name = "Daniel"
# [ ] print the first and last letters of name
print(first_name[0] + first_name[-1])

print ("\n\n### Task 3 ###")
# [ ] Review, Run, Fix the error using string index
shoe = "tennis"
# print the last letter
print(shoe[-1])
