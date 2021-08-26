#  Divisors
# Exercise 4 (and Solution)

# Create a program that asks the user for a number and then prints out a list of all the 
# divisors of that number. (If you don’t know what a divisor is, it is a number that divides 
# evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no 
# remainder.)

ask_again = 0
l = []

try:
    num = int(input("Please enter an integer number: "))
    ask_again = 1
    for n in range(1,num+1):
        divisor = num%n
        if divisor == 0:
            l.append(n)
    print("The list of divisors is: ")
    print(l)
except ValueError:
    print("The number is not an integer")
    ask_again = 0

#while ask_again == 1:
    