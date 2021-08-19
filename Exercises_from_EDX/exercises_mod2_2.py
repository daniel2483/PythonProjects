print ("\n\n### Task 1 ###")
# Currency Values
# [ ] create a list of 3 or more currency denomination values, cur_values
# cur_values, contains values of coins and paper bills (.01, .05, etc.)
cur_values = [0.5,0.3,0.7,0.8]
# [ ] print the list
print("Currency denomination list: ",cur_values)

# [ ] append an item to the list and print the list
cur_values.append(0.66)
print("New Currency denomination list: ",cur_values)

print ("\n\n")
# Currency Names
# [ ] create a list of 3 or more currency denomination NAMES, cur_names
# cur_names contains the NAMES of coins and paper bills (penny, etc.)
cur_names = ["cent","penny","quarter"]
# [ ] print the list
print("Currency Name List: ",cur_names)

# [ ] append an item to the list and print the list
cur_names.append("dollar")
print("New Currency Name List: ",cur_names)


print ("\n\n### Task 2 ###")
# [ ] append additional values to the Currency Names list using input()
new_currency_name = input("Add new currency: ")
# [ ] print the appended list
cur_names.append(new_currency_name)
print("New Currency Name List: ",cur_names)


print ("\n\n### Task 3 ###")
# while loop .append()
#   - define an empty list: bday_survey
#   - get user input, bday, asking for the day of the month they were born (1-31) or "q" to finish
#   - using a while loop (while user not entering "quit")
#       - append the bday input to the bday_survey list
#       - get user input, bday, asking for the day of the month they were born (1-31) or "q" to finish
#   - print bday_survey list
bday_survey = []
user_input = ""

while user_input != "q":
    user_input = input("The day of their birthdays are [from 1-31]: ")
    if user_input.isnumeric():
        if int(user_input) > 0 and int(user_input) <= 31:
            bday_survey.append(user_input)
        else:
            print("Insert a correct value between [1-31]")
    else:
        print("Please enter a numeric value...")

print("Birthday survey list: ",bday_survey)


print ("\n\n### Task 4 ###")
# [ ] Fix the Error
three_numbers = [1, 1, 2, 5]
print("an item in the list is: ", three_numbers[3])


