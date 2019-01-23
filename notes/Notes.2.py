# Creating a list
colors = ["Blue", "turquoise", "red", "green", "yellow" "pink", "black"]
print(colors)
print(colors[1])
print(colors[0])

# Lenth of the list
print("There are %d things in the list." % len(colors))

# Changing Elements in a list
colors[1] = "Violet"
print(colors)

# Looping through lists
for item in colors:
    print(item)

'''
1. Make a list with 7 items
2. change the 3rd thing in the list
3. print the item
4. print the full list
'''

dog_breeds = ["Bulldog", "Poodle" "Labrador", "Pitbull" "Chihuahua"]
dog_breeds[2] = "Clifford"
print(dog_breeds[2])
for item in dog_breeds:
    print(item)

new_list = ["eggs", "cheese", "oranges", "raspberries"]
new_list[2] = "bacon"
print(new_list)
print("The last thing in the list is %s" % new_list[len(new_list) - 1])

# Slicing a list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:])
print(new_list[:4])

food_list = ["ham", "turkey", "pie", "chicken", "potatoes", "salad", "chili", "salmon", "tuna", "sushi", "pizza",
"lasagna", "carne asada", "eggs", "hamburger", "cheese", "tamales", "pancakes", "beans", "rice", "churros"]

# Adding stuff to a list
food_list.append("bacon")
food_list.append("eggs")
# Notice that everything is object.method(perameters)
print(food_list)

# Removing things from a list
food_list.remove("salad")
print(food_list)

"""
1. Make a new list with 3 items
2. Add a 4th item to the list
3. Remove one of the first three items from the list
"""
# Tuples are immutable
letter_list = ["a", "b", "c"]
letter_list.append("d")
letter_list.remove("a")
print(letter_list)

# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)

string1 = "turquoise"
list1 = list(string1)
print(list1)

for i in range(len(list1)): # i goes through all indicies
    if list1[i] == "u":
        list1.pop(i)
        list1.insert(i, "*")

# Turn a list into a string
print("".join(list1))

# Function Notes
# a**2 + b**2 = c**2
def pythagorean(a, b):
    return (a**2 + b**2)**(1/2)


print(pythagorean(3, 4))


import string
print(list(string.ascii_letters_))
print(string.digits)