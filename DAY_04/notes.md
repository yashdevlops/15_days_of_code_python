
# 📘 Introduction to Loops

Loops are used to execute a block of code multiple times.
Types of loops in Python:
for loop
while loop
🔁 for Loop
Used to iterate over a sequence (like strings, lists, tuples, sets, dictionaries).
🔁 Python while Loop
A while loop executes a block of code as long as a condition is True.
⚠️ Important
The loop stops when the condition becomes False
Always update the loop variable (increment/decrement)
Otherwise, it may create an infinite loop
🔹 else with while
The else block runs when the loop condition becomes False.
🔄 Do-While Loop (Emulated in Python)
Python doesn’t have a built-in do-while loop.
👉 But we can simulate it using while True + break

# Introduction To Break and Continue

🛑 break Statement
The break statement is used to exit the loop immediately, even if the loop condition is still True.
⏭️ continue Statement
The continue statement skips the current iteration and moves to the next one.
⚠️ Important Tip
break → exits loop completely
continue → only skips that iteration
⚡ Final Takeaway
Use break when you want to stop early
Use continue when you want to skip unwanted cases

 # 🧩 Python Functions :
A function is a block of reusable code that performs a specific task.
👉 Helps in:
Code reusability
Better organization
Cleaner programs
🔹 Types of Functions
Built-in Functions
User-defined Functions
⚙️ Built-in Functions

Predefined functions available in Python.
Examples:
min(), max(), len(), sum(), type()
range(), dict(), list(), tuple(), set(), print()

🛠️ User-defined Functions

Functions created by the user for custom tasks.

Syntax:

def function_name(parameters):
    # code
📌 Rules for Creating Functions
Use def keyword
Function name should follow variable naming rules
Parameters go inside ()
Use : after declaration
Indent the function body
📥 Parameters vs Arguments
Parameter → variable in function definition
Argument → actual value passed

# 🧩 Function Arguments & Return Statement (in Python)
🔹 Types of Arguments
Default Arguments
Keyword Arguments
Required (Positional) Arguments
Variable-length Arguments (*args, **kwargs)
⚙️ Default Arguments

Provide default values in function definition.
🔑 Keyword Arguments

Pass arguments using key = value.
📌 Required Arguments

Arguments must match number + order.
🔄 Variable-length Arguments
⭐ *args (Tuple) Real-Life Thinking:*args = “I don’t know how many inputs will come”

⭐ **kwargs (Dictionary)
🔙 return Statement

Returns value back to caller.
Print vs Return (VERY IMPORTANT)
❌ Using print:
def add(a, b):
    print(a + b)

result = add(5, 3)
print(result)
📌 Output:
8
None

👉 Why None?

Because function didn’t return anything
✅ Using return:
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
📌 Output:
8
