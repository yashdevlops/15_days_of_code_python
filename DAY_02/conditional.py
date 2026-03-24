# 1. Order Matters
num = 8
if num > 8:
    print("Greater than 8")
elif num > 5:
    print("Greater than 5")
# 2. Range Check
num = 15
if num >= 1 and num <= 10:
    print("1-10")
elif num >= 11 and num <= 20:
    print("11-20")
else:
    print("Out of range")
# 3. Even or Odd
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
# 4. Nested Condition
num = 12
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Negative")
# 5. Login System
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")
# 6. Largest of 3 Numbers
a = 10
b = 25
c = 15
if a > b and a > c:
    print("A is largest")
elif b > c:
    print("B is largest")
else:
    print("C is largest")
# 7. Leap Year Check
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")