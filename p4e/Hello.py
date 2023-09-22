#Object-Oriented Programming : A paradigm where classes represent
                             # and define concepts,while objects are instances of classes.

class Apple:
    pass #shows the body is empty (just a placeholder)

class Apple:
    color = " " #Attributes
    flavor = " "

delali = Apple() #New instance
delali.color = "red"
delali.flavor = "sweat"

print(delali.color) # Uses Dot notation to access any methods or attributes
print(delali.flavor)# the instance might have.
print(delali.color.upper()) #.upper() is a method

green = Apple()
green.color = "green"
green.flavor = "sour"

print(green.color)
print(green.flavor)
