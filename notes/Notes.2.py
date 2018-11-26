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



