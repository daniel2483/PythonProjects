
# Function
def list_o_matic(list,string):

    if string == "":
        list.pop()
        return print(list)
    else:
        if string in list:
            list.remove(string)
            return print(list)
        else:
            list.append(string)
            return print(list)
    
    
def main():
    string_input = input("enter a name of an animal: ")

    if not list:
        print("Goodbye!")
        exit
        
    elif string_input == "quit":
        print("Goodbye!")
        exit

    else:
        list_o_matic(list,string_input)
        main()


# Main program

# Init list
list = ["cat","dog","jiraff"]
print (list)
# Call Main function
main()
