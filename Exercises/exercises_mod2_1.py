print ("\n\n### Task 1 ###")
# [ ] create team_names list and populate with 3-5 team name strings
team_names = ["Red Bones","Alphas","The Gladiators"]
# [ ] print the list
print("Teams List: ",team_names)

print ("\n\n")
# [ ] Create a list mix_list with numbers and strings with 4-6 items
mix_list = ["Daniel",37,1.60,"Rodriguez"]
# [ ] print the list
print("Mix List: ",mix_list)


print ("\n\n### Task 2 ###")
# [ ] Create a list, streets, that lists the name of 5 street name strings
address_list=["Laureles","Central Avenue","Concepcion","Varela","Flor"]
# [ ] print a message that there is "No Parking" on index 0 or index 4 streets
print("No Parking ",address_list[0])
print("No Parking ",address_list[4])

print ("\n\n")
# [ ] Create a list, num_2_add, made of 5 different numbers between 0 - 25
num_2_add = [4,15,25,13,7]
sum_numbers = 0
# [ ] print the sum of the numbers
for num in num_2_add:
    sum_numbers += num
print("Sum result: ",sum_numbers)



print ("\n\n### Task 3 ###")
# [ ] Fix the error above by creating and running code in this cell
pay_checks = [23,44,55,45]
print(" Total of checks 3 & 4 = $", pay_checks[2] + pay_checks[3])
