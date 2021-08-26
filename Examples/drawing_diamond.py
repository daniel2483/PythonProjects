import math

def check_if_pair(number):
    test = number%2
    if test == 0:
        center = test
        center = number/2
        #print (str(center))
        return center
    else:
        center = number/2
        center = math.floor(center)
        #print (str(center))
        return center


height = int(input("Enter the dimension of diamond (must be an integer): "))
#width = int(input("Enter the width of diamond (must be an integer): "))
width = height

width_blank = width//2
counter_heigh = 0

center = int(check_if_pair(height))
#center = check_if_pair(width)

string_lines = ""
#string_other_line = ""

counter_line = 1

for height_dimension in range(0,height):
    if counter_heigh == center:
        #print("*"+str(center))
        string_lines = ""
        for width_dimention in range(0,width):
            string_lines = string_lines + "*"
        print(string_lines)
        width_blank = width_blank+1
    if counter_heigh > center:
        string_lines = ""
        for width_dimention in range(0,width_blank):
            string_lines = string_lines + " "
        for width_dimention in range(0,(counter_line-2)):
            string_lines = string_lines + "*"
        print(string_lines)
        counter_line= counter_line -2
        width_blank = width_blank+1
    if counter_heigh < center:
        string_lines = ""
        for width_dimention in range(0,width_blank):
            string_lines = string_lines + " "
        for width_dimention in range(0,counter_line):
            string_lines = string_lines + "*"
        print(string_lines)
        counter_line= counter_line +2
        width_blank = width_blank-1
    counter_heigh = counter_heigh + 1


