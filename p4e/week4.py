name = "Delali "
food = 'eggs'
color = ""

print(name)
print(food)
print(color)

print(len(name))

# ['D','e','l','a','l','i',' ']
print(name[0])
print(name[:3])

print(name[-2])

for letter in name:
    print(letter)

#.format
print("Hi my name is {} and I like {}".format(name,food))
