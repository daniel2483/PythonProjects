print ("\n\n### Task 1 ###\n\n")
# [ ] create a list of 4 to 6 strings: birds
# print each bird in the list
birds = ["tucan","eagle","bluebird","bird"]
for bird in birds:
    print(bird)

# [ ]  create a list of 7 integers: player_points
# [ ] print double the points for each point value
list = [45,53,62,41,88,34,67]
for points in list:
    print(points*2)

# [ ] create long_string by concatenating the items in the "birds" list previously created
# print long_string - make sure to put a space betweeen the bird names
birds = ["tucan","eagle","bluebird","bird"] 
long_string = ""
for bird in birds:
    long_string = long_string + " " + bird
    
print(long_string)


print ("\n\n### Task 2 ###\n\n")
# [ ] Using cities from the example above iterate throught the list using "for"/"in"
# [ ] Print only cities starting with "m"
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
for city in cities:
    #print(city[0].lower())
    if city[0].lower() == "m":
        print(city)

# [ ] Using cities from the example above iterate throught the list using "for"/"in"
# cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# [ ] sort into lists with "A" in the city name and without "A" in the name: a_city & no_a_city
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
a_city = []
no_a_city = []
non_a_city = cities
for city in cities:
    for city_letters in city:
        if city_letters.lower() == "a":
            a_city.append(city)
            non_a_city.remove(city)
            break

print("Cities with 'a':",a_city)
print("Cities without 'a':",non_a_city)


print ("\n\n### Task 3 ###\n\n")
# [ ] complete paint stock
paint_colors = ["red","blue","yellow","magenta","brown","white"]
color_request = input("Search for a color: ")

for color in paint_colors:
    if color == color_request:
        print("Color found...")
    else:
        print("Color Not found...")

print ("\n\n### Task 4 ###\n\n")

def footbone(string,list):
    
    for foot_bone in list:
        if foot_bone == string:
            list.remove(string)
            return print("Foot bone is correct..")

    return print("Foot bone is incorrect..")

foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]

foot_bone_input1 = input("\nWhich Foot Bone 1? ")
footbone(foot_bone_input1.lower(),foot_bones)


foot_bone_input2 = input("\nWhich Foot Bone 2? ")
footbone(foot_bone_input2.lower(),foot_bones)

