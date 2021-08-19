# Final Task

# [] create Element_Quiz
# [] copy and paste in edX assignment page

def get_names():
    element_list = []
    number_of_counts = 5
    while number_of_counts > 0:
        element = input("Enter the name of an element: ")
        element = element.strip()
        #print("Counter : ",number_of_counts)
        number_of_counts -= 1
        if element != "":
            for number in range(len(element_list)):
                if element_list[number].lower() == element.lower():
                    print(element.lower()," was already entered!")
                    number_of_counts += 1
                    element_list.pop(number)
                    break
            element_list.append(element.title()) 
        else:
            number_of_counts += 1
            print("Not empty string is allowed!")
            
    return element_list

!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt  -o elements1_20.txt
elements1_20_file = open('elements1_20.txt','r')

#elements1_20_list = elements1_20_file.readlines()
elements_from_file = []

#print(elements1_20_list)
for count in range(0,20):
    element = elements1_20_file.readline().strip()
    #element[] = element.lower()
    elements_from_file.append(element.lower())

#print(elements1_20_list)
#print(elements_from_file)
element_list = get_names()
#print(element_list)

correct = []
incorrect = []

for element_from_file in elements_from_file:
    for element in element_list:
        if element.lower() == element_from_file:
            correct.append(element)
            #print(element_from_file," ",element)
            element_list.remove(element)
        #print(element_from_file," ",element)

incorrect = element_list
        
quiz_result = len(correct)*20
print("\n",quiz_result," % correct")
print("Found: "," ".join(correct))
print("Not Found: "," ".join(incorrect))

