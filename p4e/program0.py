
print("hi\thello \n")

x = 10 #Int
y = "Hello World" #String aka Str
z = 20.5 #Float
word = "10"

userInput = input("Enter a number: ")

print("My number is " + str(x))

print(str(x) + y)

def my_function(name):
    print(name + " Ekpeh")

my_function("Delali")
my_function(y)
my_function(str(z))

def total(num,numTwo):
    print(num * numTwo)

total(100,z)

def minus(number,numberTwo):
    return number - numberTwo

minus(10,5)
print(minus(10,5))
solution = minus(20,10)
print("Hey the solution is " + str(solution))

# == - Equals. Ex: a == b
# != - Not Equals To. Ex: a != b
# < - Less Than. Ex: a < b
# > - Greater Than. Ex: a > b
# >= - Greater Than or Equal to. Ex: a >= b

a = 33
b = 200

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are eqaul")
else:
    print("a is greater than b")
