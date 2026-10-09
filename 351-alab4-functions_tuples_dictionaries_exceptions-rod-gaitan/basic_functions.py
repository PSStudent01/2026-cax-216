
# 1)
# Define a function greet_user() that takes a name (string) as a parameter and prints a greeting, e.g., "Hello, <name>! Welcome!". If no name is provided (you can simulate this by calling greet_user() with an empty string or by using a default parameter value), it should print "Hello! Welcome!".

r'''  
# 1st Attempt - works, but not with 100% !!!
def greet_user(name):
    print(f"Hello, {name}! Welcome!")
    if name == "":
        print("Hello! Welcome!")

greet_user("")
'''

# 2nd Attempt - Successful!
## This function prints a greeting. If no name is given, print a generic greeting.
# def greet_user(name): # works but does not validate 'without name' as required.
def greet_user(name=""): # 1. While the assignment allows an 'empty' string, greet_user("") is acceptable... 
                         # but to be precise changing function definition to "def greet_user(name="")" allows for 'without' a 
                         # character case. So 'name' defaults to "" so greet_user() can be called with no argument.
    if name == "":  # if users no input and presses enter...
        print("Hello! Welcome!") # the program prints "Hello! Welcome!".
    else:
        print(f"Hello, {name}! Welcome!") # otherwise, if user enters a name and presses enter, it prints: "Hello,[name]! Welcome!"
# greet_user("Rod") # Testing it out. It works!
# greet_user("") # Testing it out. It works!
# greet_user() # Testing it out. It works!   # .2 and call greet_user() with no argument.


# 2)
# Define a function add_two_numbers(a, b) that returns the sum of two numbers a and b.

# 1st Attempt - Successful!
## This function returns the sum of a and b (does not print anything from within the function).
def add_two_numbers(a, b):
    return a + b
    # total_sum = add_two_numbers(5, 6) # assigment does not require for returned value to be assigned to a variable while inside the function 'add_two_numbers(a, b)'
# add_two_numbers(5, 6) # this passes the 2 arguments to the 2 parameters, but there is no print() function anywhere
# print(add_two_numbers(5, 6)) # Intermidiate test. It works!
# total_sum = add_two_numbers(5, 6) # 1. Intermidiate test. It works!
# print(total_sum) # 2. Intermidiate test. It works!


# 3)
# Define a function is_even(num) that returns True if num is even or False otherwise.

# 1st Attempt - Successful
## This function returns 'True' if 'num' is even, otherwise it returns 'False' (does not print anything from within the function).
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
# is_even(2)  # this passes the argument to the parameter, but there is no print() here.
# print(is_even(2)) # Intermidiate test. It works!
# print(is_even(3)) # Intermidiate test. It works!

# 4)
# In the main part of the script (outside the functions), demonstrate each function:
# 1.
print('1)')
greet_user("Rod Gaitan") # calling function with a name
# greet_user("") # calling function without a name
greet_user() # .2  calling greet_user() with no argument.
print()
# 2.
print('2)')
print(add_two_numbers(5, 6))  # printing the result directly
total_sum = add_two_numbers(5, 6) # 1. Storing the returned value in variable 'total_sum'.
print(total_sum) # 2. Then printing the result indirectly via variable 'total_sum'.
print(f"The current total sum of {total_sum} multiplied by 2 will give us twice as much. In this case it will "
      f"give us: {total_sum * 2}") # Returned value from 'total_sum' variable being used in an expression '{total_sum * 2}'.
print()
# 3.
print('3)')
# print(f"Is the number 2 an even number? {is_even(2)}") 
# print(f"Is the number 3 an even number? {is_even(3)}") 
result = is_even(2)  # 1. Storing the returned value in variable 'result' for an even number.
print(f"Is the number 2 an even number? {result}") # 2. then using the stored value as part of a string
result = is_even(3) # 3. Storing the returned value in variable 'result' for an odd number.
print(f"Is the number 3 an even number? {result}")  # 4. then using the stored value as part of a string

# =============================== WHAT I LEARNED - (Add to README.txt file)  ================================================== #
r'''  
Defining functions
Parameters let a function receive input: greet_user(name), add_two_numbers(a, b), is_even(num).
Default parameter values (name="") make an argument optional, so greet_user() works with no argument at all. You noticed the difference between the assignment’s allowed shortcut (greet_user("")) and the more precise version that handles a call with nothing passed.
Order of logic matters. Your 1st attempt printed the full greeting and then checked for an empty name, so an empty string printed both messages. The 2nd attempt checks first, then uses if/else so only one greeting prints. That’s the main debugging lesson here.
print vs. return
greet_user prints inside the function (it performs an action). add_two_numbers and is_even return a value and print nothing, leaving the caller to decide what to do with it.
Your own comments capture the key point: calling add_two_numbers(5, 6) without print() computes the answer but shows nothing.
This is the same idea as in data_processing.py: a returned value is only useful once you store it or print it.
Using returned values
Print it directly: print(add_two_numbers(5, 6)).
Store it in a variable: total_sum = add_two_numbers(5, 6), then reuse it.
Use it in an expression: total_sum * 2.
Use it inside an f-string: f"... {result}".
Booleans and operators
The modulo operator % gives the remainder, so num % 2 == 0 tests for even numbers.
is_even returns a boolean (True/False), and f-strings display it directly.
Note that == compares, while = assigns.
Process lessons
Test as you go. Your commented-out intermediate tests (# Works!) show you checked each piece before moving on.
Keep the function definitions separate from the demo code, as the lab asked (“in the main part of the script, outside the functions”).
Comment each attempt honestly, including where something worked “but not with 100%”.
Optional improvements
Simplify is_even: since num % 2 == 0 is already True or False, this does the same thing:
python
  def is_even(num):
      return num % 2 == 0

Your if/else version is correct and clearer for a beginner, so keeping it is fine.

Add docstrings to each function (parameters and return values), since the submission asks for comments on those.
Fix typos: “Intermidiate” should be “Intermediate”, and “assigment” should be “assignment”.
One comment is inaccurate: “if users no input and presses enter” suggests the function reads keyboard input, but it doesn’t. It just checks whether name is an empty string. Rewording it avoids confusion.
Trim the long comments on the default parameter, and keep the ones that explain why.
'''

# =============================== PENDING ================================================== #
'''
Also, since the assignment asks for notes on each part, a README in the repo with a short section per script would cover all 
five files in one place, with sample outputs included. If you keep this block in calc_with_functions.py, it only covers that 
one script.
'''

