r'''
Create a script calc_with_functions.py that refactors the calculator from Module 2 (Task 2.3) using functions:

    - Write separate functions for each operation: add(a,b), subtract(a,b), multiply(a,b), divide(a,b) – each returning the 
      result.
    - Write a calculate(a, b, op) function that takes two numbers and a symbol for operation, and uses if/elif to call the 
      correct operation function. It should handle an invalid operation by returning or printing an error message.
    - In the main program, ask the user for two numbers and an operation (just like before), but now use the calculate function 
      to get the result and print it.
    - Add exception handling to gracefully handle errors such as division by zero or invalid numeric input. Use try/except 
      around the input conversion and the division operation at minimum.

This task will demonstrate functions calling other functions and basic exception handling.
'''


# =============================== LOGIC ================================================== #
# add(a,b), subtract(a,b), multiply(a,b), divide(a,b) – each returning the result.

## Description: these are four individual functions that handle each of the 4 types of operations (+, -, *, /):
def add(a, b): # 'a' and 'b' are the two numbers to add
    return a + b  #returns their sum

def subtract(a,b): # 'a' is the number to subtract from; 'b' is the number to subtract
    return a - b # returns the difference

def multiply(a,b): # 'a' and 'b' are the two numbers to multiply
    return a * b # returns their product

def divide(a,b):  #  'a' is the number to be divided (numerator); 'b' is the number to divide by (denominator)
    try:
        return a / b # returns the quotient, or an error message if b is 0
    except ZeroDivisionError: # catches division by zero and returns a friendly message instead of crashing
        return "Error: cannot divide by zero!"
# Encapsulated the expression 'return a / b' within a 'try/except' block, so that if a number is ever divided by zero, rather than
# displaying a highly technical message for the user to figure out, this block catches the error and returns the exception in
# a much more simplified exception message, in this case "Error: cannot divide by zero!"


# Write a calculate(a, b, op) function that takes two numbers and a symbol for operation, and uses if/elif to call the 
# correct operation function. It should handle an invalid operation by returning or printing an error message.

## Description: this function applies/executes any of the above functions on 2 given operands, depending on the 
## operation symbol entered!
def calculate(a, b, op): # 'a' and 'b' are the numbers; 'op' is the symbol (+, -, *, /)
    if op == "+":
        # add = a + b
        # add(a, b)
        return add(a, b) # returns the sum total of 2 numbers, by calling the function 'add(a, b)' onto them.
    elif op == "-":
        # minus = a - b
        # subtract(a,b)
        return subtract(a,b) # returns the difference between 2 numbers, by calling the function 'subtract(a, b)' onto them.
    elif op == "*":
        # times = a * b
        # multiply(a,b)
        return multiply(a,b)  # returns the product of 2 numbers, by calling the function 'multiply(a, b)' onto them.
    elif op == "/":
        # divide = a / b
        # divide(a,b)
        return divide(a,b)  # returns the quotient of 2 numbers, by calling the function 'divide(a, b)' onto them.
    else:
        print("Invalid operation. Try again!") # or an error message if 'op' is invalid



# =============================== MAIN ================================================== #
# In the main program, ask the user for 2 numbers and an operation (just like before), but now use the calculate function to get the result and print it.

## This is the main program, made up of 
## 1) INPUT: 3 separate input functions, 2 for each number entered and the one in the middle for the operation of chioce.
## 2) OUTPUT: the output made of... 
### the function call
### the result print

r''' 
### 1st Attempt - it has a bug!!
try:
    a = float(input("Enter first number: "))
except:
    print("Invalid input. Try again!")

op = input("Enter operation sign: ")

try:
    b = float(input("Enter second number: "))
except:
    print("Invalid input. Try again!")

result = calculate(a, b, op)
print(result)
'''

### 2nd Attempt - Successful:
try:
    # INPUT:
    a = float(input("Enter first number: ")) # takes in the 1st float character and stores it in 'a' variable
    op = input("Enter operation sign: ") # takes in the operation symbol
    b = float(input("Enter second number: ")) # takes in the 2nd float character and stores it in 'b' variable
    # OUTPUT:
    result = calculate(a, b, op)  # a call to the function 'calculate' is made when the user enters values for each of 3 variables
    print(result) # then the result is printed
except ValueError:
    print("Invalid input. Please enter valid numbers.")  
# Encapsulated the main program within a 'try/except' block, so that if any input type other than 'float' is entered at the
# first input request, rather than displaying a highly technical message for the user to figure out, this block catches the 
# error and returns the exception in a much more simplified exception message in this case...
#  "Invalid input. Please enter valid numbers."


# =============================== WHAT I LEARNED - (Add to README.txt file!!!!!!)  ================================================== #

'''
#
- how in Pyhton...
-- the logic must be established and placed first before the main, unlike JS!
-- first functions were created for the arithmetic specifically and sorta buffer their result  via the 'return' keyword, so that
other outside functions like 'calculate()' can later make use of them.
--- then the function 'calculate()' was created to specifically be able call on and make use of such arithmetic mini functions
--- then in the main program is where 
-- the function 'calculate()' gets called on by 
--- the same 'input()' functions that live in the main, which receive input data from the user, when the user interacts with app.
--- it is also where output functionality like 'print()'lives
#
-- Also how the 'try/except blocks' come in handy to gracefully handle all sort of exceptions to make the flow of the app more
user-friendly
-- most common standard exceptions:
--- ZeroDivisionError: dividing by zero
--- TypeError: wrong type for an operation, like "5" + 3
--- NameError: using a variable or function that doesn't exist yet.
--- KeyError: looking up a dictionary key that isn't there
--- IndexError: list or tuple index out of range
--- FileNotFoundError: opening a file that doesn't exist
-- For example, referring to this lab,
--- the 'ValueError' is caught around the float(input(...)) conversions, so typing 'abc' prints a friendly message instead of a 
traceback message.
--- the 'ZeroDivisionError' is caught inside divide(), which returns an error message instead of crashing the app.
'''
# =============================== PENDING ================================================== #
'''
Also, since the assignment asks for notes on each part, a README in the repo with a short section per script would cover all 
five files in one place, with sample outputs included. If you keep this block in calc_with_functions.py, it only covers that 
one script.
'''
# =============================== WHAT I LEARNED ================================================== #
r'''
Functions calling other functions
calculate(a, b, op) doesn’t do any math itself. It decides which operation to run with if/elif and hands the work to add, subtract, multiply, or divide.
Each small function does one job and returns its result, so calculate can pass those results back to the caller.
Parameters and return values: a and b carry the numbers in, and return carries the answer out.
Avoiding a naming trap
Your commented-out lines like add = a + b would have replaced the function add with a number inside calculate, because a variable with the same name as a function shadows it. Commenting them out and calling add(a, b) directly was the right fix.
Exception handling
divide: try/except ZeroDivisionError catches division by zero and returns a friendly message instead of crashing.
Main program: float(input(...)) raises ValueError if the user types something that isn’t a number, and except ValueError catches it and prints a clear message.
You caught specific exceptions in your 2nd attempt, instead of the bare except: from your 1st.
Debugging lesson: the 1st attempt’s bug
In the 1st attempt, each input had its own try/except, but nothing stopped the program after a failure. If the first number was invalid, a was never created, and calculate(a, b, op) crashed with a NameError.
The 2nd attempt puts all three inputs and the calculate call inside one try. The first failure jumps straight to the except, so the later lines never run with missing values.
Process lessons
Keep logic and main program separate, with the functions defined first and the user interaction below.
Document attempts honestly, including the one with the bug.
Explain why in comments: you noted that the try/except exists so the user sees a simple message instead of a technical traceback.
Things worth tidying before submitting
Invalid operation: calculate prints “Invalid operation. Try again!” and returns None, so the main program then also prints None. Either return the message instead of printing it, or check for None before printing, the same pattern as in data_processing.py.
divide returns a string on error. That works for this lab, but it mixes a number and a text message in the same return value, so a caller can’t easily tell them apart. Raising a ValueError (as in exception_demo.py) and catching it in the main program is the cleaner design. If you keep your version, say in the notes that it was a deliberate choice.
ZeroDivisionError in divide: your lab says to use try/except around the division, and you did, so that requirement is met.
Docstrings: add short ones to each function listing parameters and return values, as the submission asks.
Comment accuracy: “takes in the 1st float character” should say “number”, since a float isn’t a character. Also fix the typo “chioce”.
Optional: wrap the main program in a while loop so the user can try again after a bad input, since the message says “Try again!” but the program just ends.
'''