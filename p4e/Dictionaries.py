# Dictionaries are used to organize elements into collections but you don't access elements inside using their position.
# Instead of indexs Dictionaries uses pairs of keys and values. Dictionaries values are mutable but keys in Dictionaries are not
# Syntax of declaring a dictionary
#             Key: Value,  Key: Value,   Key: Value,    Key: Value
studentAge = {"Mark":16,   "Ash":16,   "Delali":20,    "Ronnie":21}
print(studentAge)
# {'Mark': 16, 'Ash': 16, 'Delali': 20, 'Ronnie': 21}
print(studentAge["Ash"])
# 16

# Checks if a key is found in the dictionary
print("Delali" in studentAge)
# True

# How to add new element to a dictionary
studentAge["Brandon"] = 18
print(studentAge)
# {'Mark': 16, 'Ash': 16, 'Delali': 20, 'Ronnie': 21, 'Brandon': 18}

# Remember Dictinaries are mutable so setting an exisiting key to another value would overide the previous value
studentAge["Delali"] = 10
print(studentAge)
# {'Mark': 16, 'Ash': 16, 'Delali': 10, 'Ronnie': 21, 'Brandon': 18}

# How to delete an element in a dictionary
del studentAge["Ash"]
print(studentAge)
# {'Mark': 16, 'Delali': 10, 'Ronnie': 21, 'Brandon': 18}

for student in studentAge:
    print("Hi {}".format(student))
# Hi Mark
# Hi Delali
# Hi Ronnie
# Hi Brandon

# .items() function makes the keys and values in a dictionary into tuples
#    Key:    Value
for student, age in studentAge.items():
    print("{} is {} years old".format(student,age))
# Mark is 16 years old
# Delali is 10 years old
# Ronnie is 21 years old
# Brandon is 18 years old

# List and tuples can be values in dictionaries
studentInfo = {"Delali":['1D',20], "Brandon":['2D',17]}

print(studentInfo)
# {'Delali': ['1D', 20], 'Brandon': ['2D', 17]}
print(studentInfo["Delali"])
 # ['1D', '20']
