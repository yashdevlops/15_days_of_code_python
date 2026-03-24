print(5+6)
print(15-6)
print(15*6)
print(15/6)
print(15//6)
print(5%3)
print(2**4)

# EXCERCISE 1

a = int(input("ENTER THE 1st NUMBER : "))
b = int(input("ENTER THE 2nd NUMBER : "))

print("The value of", a, "+", b, "is: ", a + b)
print("The value of", a, "-", b, "is: ", a - b)
print("The value of", a, "*", b, "is: ", a * b)
print("The value of", a, "/", b, "is: ", a / b)

# TYPE CASTING
a = "1"
b = "2"
print(int(a) + int(b))
# Implicit TypeCasting
c = 1.9
d = 8
print(c + d)
# TAKING USER INPUT
name = input("Enter your name: ") # Taking string input
print("Hello,", name)
age = int(input("Enter your age: "))# Taking integer input
print("Your age is:", age)
price = float(input("Enter the price: "))# Taking float input
print("Price is:", price)
x = input("Enter first number: ")# alternative method
y = input("Enter second number: ")
print(x  + y)
print(int(x) + int(y))
# STRINGS
name = "Harry" # Creating and printing a string
print("Hello, " + name)

print('He said, "I want to eat an apple".')# Using quotes inside a string
# Multiline string
text = """This is line 1
This is line 2
This is line 3"""
print(text)

print(name[0])# Accessing characters using index
print(name[1])

for character in name:# Looping through a string
    print(character)
#String Slicing & Operations on String

fruit = "Mango" # Length of a string
print(len(fruit))

pie = "ApplePie" # String slicing
print(pie[:5])    # From start
print(pie[5:])    # Till end
print(pie[2:6])   # In between
print(pie[-8:])   # Negative index

print(pie[6])# Accessing single character

alphabets = "ABCDE" # Looping through string 
for i in alphabets:
    print(i)

# STRING METHODS
text = "  Hello World!  "

print(text.upper()) # Case conversion
print(text.lower())

print(text.strip())# Remove spaces
print(text.rstrip("!"))

print(text.replace("World", "Python"))# Replace and split
print(text.split())

print("hello world".capitalize())# Capitalization and alignment
print("hello".center(20, "-"))

print("banana".count("a"))# Searching and counting
print("hello world".find("world"))

print("Hello123".isalnum())# Boolean checks
print("Hello".isalpha())
print("hello".islower())
print("HELLO".isupper())
print("   ".isspace())
print("Hello World".istitle())

print("Python".startswith("Py"))# Start/End check
print("Python".endswith("on"))

print("Hello World".swapcase())# Case conversion variations
print("hello world".title())