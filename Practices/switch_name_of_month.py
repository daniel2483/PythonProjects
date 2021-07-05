
print("Finding the name of the month ...")

argument=int(input("Enter a number of a month: "))

def switch_demo(argumento_ini):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print (switcher.get(argumento_ini, "Invalid month"))

switch_demo(argument)
