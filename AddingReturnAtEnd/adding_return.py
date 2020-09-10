# Reading a input file for indexes and generating new file output

# Open File in r mode
fileIn = open('in/input.txt','r')
fileOut = open('out/output.txt','w')

new_file = "";

# Reading headings
line = fileIn.readline()

fileOut.write(line + "\n")

while line:
    #print(line)
    line = fileIn.readline()
    fileOut.write(line + "\n")


fileOut.close()
fileIn.close()

