# Examples: Importing files in Jupyter Notebooks

print ("\n\n### Task 1 ###\n\n")
# create a local file
#   - open in 'w' mode
#   - open inner_planets.txt in write mode 'w' to create a local file
#   - write the first four planets from the sun in earth's solar system (Mercury, Venus, Earth, Mars) on separate lines
#   - close the file and re-open in read mode 'r'
#   - use .read() to read the entire file contents
#   - print the entire file contents

# [ ] open planets.txt in write mode
inner_planets = open('inner_planets.txt','w')

# [ ] write Mercury, Venus, Earth, Mars on separate lines
inner_planets.write("Mercury\nVenus\nEarth\n")

# [ ] close the file and re-open in read mode
inner_planets.close()

# [ ] use .read() to read the entire file contents
inner_planets = open('inner_planets.txt','r')
inner_planets_text = inner_planets.read()

# [ ] print the entire file contents and close the file
print(inner_planets_text)


print ("\n\n### Task 2 ###\n\n")
# using .seek(0) on a local file in write plus read mode 'w+'¶
# open outer_planets.txt in 'w+' mode (write plus read)
#   - open outer_planets.txt in write plus read mode 'w+'
#   - write four outer planets in earth's solar system (Jupiter, Saturn, Uranus, Neptune) on separate lines
#   - use .seek() to move the pointer to the start of the file
#   - use .read() to read the entire file contents
#   - print the entire file contents and close the file

# [ ] open outer_planets.txt in write mode 'w+' 
outer_planets = open('outer_planets.txt','w+')

# [ ] write four outer planets in earth's solar system (Jupiter, Saturn, Uranus, Neptune) on separate lines
outer_planets.write("Jupiter\nSaturn\nUranus\nNeptune\n")

# [ ] use .seek() to move the pointer to the start of the file
# [ ] use .read() to read the entire file contents
outer_planets.seek(0)
outer_planets_text =outer_planets.read()

# [ ] print the entire file contents and close the file
print(outer_planets_text)

outer_planets.close()

print ("\n\n### Task 3 ###\n\n")
#   whence mode	    description
#   0	            points to the beginning of the file
#   1	            points to the current location
#   2	            points to the end of the file & offset is always 0

# seek() with optional whence argument
#   - open a new file days.txt in write plus read mode 'w+'
#   - write week days (Monday - Friday) on separate lines
#   - use .seek() to move the pointer to the start of the file
#   - use .read() to read the entire file contents
#   - print the entire file contents and close the file
#   - use .seek() to move the pointer to the end of the file and write the weekend days (Saturday & Sunday)
#   - use .seek() to move the pointer to the start of the file
#   - use .read() to read the entire file contents
#   - print the entire file contents and close the file

# [ ] open a new file days.txt in write plus read mode 'w+' 
# [ ] write week days (Monday - Friday) on separate lines to the file
new_file = open('days.txt','w+')
new_file.write("Monday\nTuesday\nWednesday\nThursday\nFriday\n")
print(new_file)

# [ ] use .seek() to move the pointer to the start of the file
# [ ] use .read() to read the entire file contents
# [ ] print the entire file contents and close the file
new_file.seek(0)
new_file_text = new_file.read()
print(new_file_text)

#new_file.close()

# [ ] use .seek() to move the pointer to the end of the file
# [ ] write the weekend days (Saturday & Sunday)
#new_file = open('days.txt','w+')
new_file.seek(0,2)
new_file.write("Saturday\nSunday\n")

# [ ] use .seek() to move the pointer to the start of the file
# [ ] use .read() to read the entire file contents
# [ ] print the entire file contents and close the file
new_file.seek(0)
new_file_text = new_file.read()
print(new_file_text)

new_file.close()

print ("\n\n### Task 4 ###\n\n")
#   MODE	Description
#   'r'	        read only mode
#   'w'	        write - overwrites file with same name
#   'w+'	write and read mode - overwrites file with same name
#   'r+'	read and write mode (no overwrite)
#   'a'	        opens for appending to end of file (no overwrite)
#   'a+'	opens for appending to end of file (no overwrite) plus read

# append
#   - Open task4_file.txt in append plus mode ("a+")
#   - create a for item in range(5): loop, for each loop:
#       - write to the file: "append #"+ str(item)+"\n"
#       - use seek() to set the pointer to the beginning of the file
#   - print the file contents using file .read() method after eiting the loop
# in append mode the file should only write to the end of the file regardless of setting seek() location

# [ ] complete the task
# Provided Code creates and populates task4_file.txt
task4_file = open('task4_file.txt', 'w+')
task4_file.write("Line1\nLine2\nLine3\n")
task4_file.close()
# [ ] code here
file = open('task4_file.txt','a+')

for item in range(5):
    file.write("append #"+ str(item)+"\n")

file.seek(0)
file_text = file.read()
print(file_text)


print ("\n\n### Task 5 ###\n\n")
# read plus (r+) mode
# read the provided code and complete the code as follows:
#   - Run the provided code below to create/open, print and close task5_file.txt
#   - Open task5_file.txt in append plus mode ("r+")
#   - create a   for item in range(1,5): loop, then, during each loop:
#       - write to the file: "append#" + str(item)+ "\n"
#       - use .seek(item*18) to set the pointer to 18x's the loop count
#           Note: starting the first loop, item is 1 if using range(1,5), seek will be set to 18, 36, 54, 72
#   - print the file contents using file .read() method after exiting the loop
# "r+" mode will write wherever the pointer is set - such as after a read or from using .seek()

# [ ] complete the task
# Provided Code creates and populates task5_file.txt
task5_file = open('task5_file.txt', 'w+')
task5_file.write("Line---1\nLine---2\nLine---3\nLine---4\nLine---5\nLine---6\nLine---7\nLine---8\nLine---9\nLine--10\n")
task5_file.seek(0)
print("Before:\n"+ task5_file.read()+"\n")
task5_file.close()

# [ ] code here
task5_file = open('task5_file.txt', 'r+')
for item in range(1,5):
    task5_file.write("append#" + str(item)+ "\n")
    task5_file.seek(item*18)

task5_file_text = task5_file.read()
print(task5_file_text)

