# OPERATORS #
Operators in Python are used to perform operations on variables and values. Arithmetic operators are the most common and are used for basic mathematical calculations.

These include addition (+), subtraction (-), multiplication (*), exponentiation (**), division (/), modulus (%), and floor division (//). Each operator performs a specific operation, such as adding numbers, finding remainders, or dividing values while returning either exact or rounded-down results.

# Exercise 1 - Create a Calculator 
Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers.

# Typecasting in python :

Typecasting in Python refers to converting one data type into another. Python provides several built-in functions like int(), float(), and str() to perform these conversions.

There are two types of typecasting. Explicit typecasting is done manually by the programmer using functions to convert data from one type to another as needed. Implicit typecasting is done automatically by Python when performing operations on different data types, where the lower data type is converted into a higher one to avoid data loss.

This makes Python flexible and helps ensure smooth execution of operations involving mixed data types.

| Level       | Data Type | Description                    |
| ----------- | --------- | ------------------------------ |
| 1 (Highest) | complex   | Complex numbers (e.g., 3+2j)   |
| 2           | float     | Decimal numbers (e.g., 3.14)   |
| 3           | int       | Integer numbers (e.g., 10, -5) |
| 4           | bool      | Boolean values (True, False)   |
int + float → float
float + complex → complex

# Taking User Input in python
In Python, user input can be taken using the input() function, which always returns data as a string. To use the input as another data type like integer or float, we need to apply typecasting.

The input() function can also display a message (prompt) to guide the user while taking input. This makes it easier to interact with users and collect the required data effectively.

Overall, typecasting is often used along with input() to ensure the data is in the correct format for further operations.

# STRINGS
Strings in Python are sequences of characters enclosed within single (' ') or double (" ") quotes. They are commonly used to store and work with text data, and both quote styles produce the same result. If a string contains quotes inside it, the other type of quotation mark can be used for convenience.

Python also supports multi-line strings using triple quotes, making it easy to work with text spanning multiple lines. Strings behave like arrays, allowing access to individual characters using indexing, where indexing starts from 0. Additionally, strings can be iterated using loops to access each character one by one.

# String Slicing & Operations on String :
Strings in Python are sequences of characters, which means they can be accessed like arrays. You can find the length of a string using the len() function. String slicing allows you to extract parts of a string by specifying start and end indices. Python also supports negative indexing for reverse access. Since strings are iterable, you can loop through each character using a loop.

# String Methods :
This section covers commonly used string methods in Python, which are essential for manipulating and analyzing text data. Python provides built-in functions to change the case of strings, remove unnecessary spaces, replace or split text, and format strings for better readability.
upper() – Converts all characters in the string to uppercase.
lower() – Converts all characters in the string to lowercase.
strip() – Removes whitespace from both the beginning and end of the string.
rstrip() – Removes trailing characters (or whitespace) from the end of the string.
replace() – Replaces all occurrences of a substring with another substring.
split() – Splits the string into a list based on a specified separator.
capitalize() – Converts the first character to uppercase and the rest to lowercase.
center() – Aligns the string in the center with specified padding.
count() – Returns the number of times a substring appears in the string.
endswith() – Checks if the string ends with a specified value.
find() – Returns the index of the first occurrence of a substring, or -1 if not found.
index() – Returns the index of a substring, but raises an error if not found.
isalnum() – Returns True if the string contains only letters and numbers.
isalpha() – Returns True if the string contains only letters.
islower() – Returns True if all characters are lowercase.
isprintable() – Returns True if all characters in the string are printable.
isspace() – Returns True if the string contains only whitespace characters.
istitle() – Returns True if each word starts with an uppercase letter.
isupper() – Returns True if all characters are uppercase.
startswith() – Checks if the string starts with a specified value.
swapcase() – Converts uppercase letters to lowercase and vice versa.
title() – Capitalizes the first letter of each word in the string.
# CONDITIONAL STATEMENTS :
Conditional statements in Python are used to control the flow of a program based on certain conditions. The if, elif, and else statements allow the program to execute different blocks of code depending on whether a condition evaluates to True or False.

An if statement checks a condition and executes its block if the condition is true. The else block runs when the condition is false. The elif statement is used to check multiple conditions in sequence. Python also supports nested conditional statements, where one condition can be placed inside another for more complex decision-making.

These statements are essential for building logic-driven programs.