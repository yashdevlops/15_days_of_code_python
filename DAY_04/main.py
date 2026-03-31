#for loops

name = "Abhishek"#Example: Iterating over a string
for char in name:
    print(char, end=", ")
colors = ["Red", "Green", "Blue", "Yellow"]#Example: Iterating over a list
for color in colors:
    print(color)
for i in range(5):#Default range (starts from 0)
    print(i)
for i in range(4, 9):#Example: Custom range
    print(i)    
for i in range(1, 10, 2):#range(start, stop, step)
    print(i)    

#while loops

count = 5 #Example:
while count > 0:
    print(count)
    count -= 1    
x = 3 # else with while 
while x > 0:
    print(x)
    x -= 1
else:
    print("Done")  
while True: #Do-While
    number = int(input("Enter a number: "))
    print(number)
    if number <= 0:
        break    

# Break and Continue
for i in range(1, 101):
    if i == 50:
        break
    print(i)
for i in range(12):
    if i == 10:
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)

for item in items:
    if item == target:
        print("Found")
        break
for i in [2, 3, 4, 6, 8, 0]:
    if i % 2 != 0:
        continue
    print(i)        

# Built in Functions :

print("Hello")
len([1, 2, 3])
max(10, 20)

# User Defined Functions 

def greet(name):
    print("Hello", name)

greet("Abhishek")

def add(a, b):   # parameters
    return a + b

add(2, 3)        # arguments

# 1. Default Arguments
def greet(fname, mname="John", lname="Watson"):
    print("Hello", fname, mname, lname)

greet("Amy")
greet("Sam", "Wilson", "Smith")
# 2. Keyword Arguments
def greet(fname, mname , lname):
    print("Hello" , fname , mname , lname)
greet("Yash", "Sachin" , "Devansh")    
#3. Required (Positional) Arguments
def greet(fname, mname , lname):
    print("Hello" , fname , mname , lname)
greet("Yash", "Sachin" , "Devansh") 
greet("Peter", "Quill")   # Wrong code
#5. Return Statement (VERY IMPORTANT)
def add(a, b):
    result = a + b
    return result
output = add(5, 3)
print("Result is:", output)
# 1. *args (Multiple Values → Tuple)
def add_numbers(*numbers):
    print("Received:", numbers)
    
    total = 0
    for num in numbers:
        total += num
    
    print("Sum =", total)

add_numbers(1, 2, 3)
add_numbers(5, 10, 15, 20)
# 2. **kwargs (Key-Value → Dictionary)
def student_info(**data):
    print("Received:", data)
    
    for key, value in data.items():
        print(key, "=", value)

student_info(name="Sam", age=20)
student_info(name="John", age=22, course="Python")
# MIXING BOTH ARGS AND KWARGS
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
demo(1, 2, 3, name="Sam", age=20)

