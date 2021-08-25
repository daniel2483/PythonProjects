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
        center = math.ceil(center)
        #print (str(center))
        return center


height = int(input("Enter the height of rectangule (must be an integer): "))
width = int(input("Enter the width of rectangule (must be an integer): "))

counter_heigh = 0

center = int(check_if_pair(height))
#center = check_if_pair(width)

string_lines = ""
#string_other_line = ""

counter_line = 0

for height_dimension in range(0,height):
    if counter_heigh == center:
        #print("*"+str(center))
        for width_dimention in range(0,width):
            string_lines = string_lines + "*"
            #if width_dimention == (width-1):
        print(string_lines)
    #elif (counter_heigh < (height-1)):
    #    if (counter_line == 0):
    #       for width_dimention in range(0,width):
    #            if width_dimention == 0 or width_dimention == (width-1):
    #                string_other_line = string_other_line + "*"
    #            else:
    #                string_other_line = string_other_line + " "
    #    print(string_other_line)
    #    counter_line = counter_line + 1
    else:
        print("\n")
    counter_heigh = counter_heigh + 1


