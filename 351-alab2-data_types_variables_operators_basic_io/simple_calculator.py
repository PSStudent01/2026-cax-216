print()
##################################### Part 2 - User Interaction and Input ##################################################

# Write a Python script simple_calculator.py:

## VERSION 1: Asks the user to input two numbers (use two separate input() calls). Make sure to convert these inputs from strings to integers or floats as needed:
#num1 = int(input("Please enter the first number: ")) # takes 1st input and casts it to integer. Had to remove, it conflicts w/ isdigit()
#num2 = int(input("Please enter the second number: ")) # takes 1st input and casts it to integer. Had to remove, it conflicts w/ isdigit()
num1 = input("Please enter the first number: ") # takes 1st input, no casting input to integer here. 
num2 = input("Please enter the second number: ")  # takes 2nd input, no casting input to integer here. 

## Asks the user to choose an operation (e.g., addition, subtraction, multiplication, division). This can be a simple prompt like "Choose an operation (+, -, *, /): ":
operator = input("Please choose operator: ") # allows you to select the operator, but in this case, it's limited to only multiplication because the logic below allows for only multiplication

## Performs the chosen operation on the two numbers:
# if num1.isdigit() == False or num2.isdigit() == False: # this code line implements 'isdigit()' & works but goes agains DRY code
if not num1.isdigit() or not num2.isdigit(): # # this code line implements 'isdigit()' as a better technique
    print("Please enter a valid input!")
else:
    num1 = int(num1)
    num2 = int(num2)

    if operator == '+':
        sum = num1 + num2 # logic performing addition.
        print(f"{num1} + {num2} = {sum}") # Prints the result in a user-friendly way
    elif operator == '-':
        difference = num1 - num2 # logic performing substraction.
        print(f"{num1} - {num2} = {difference}") # Prints the result in a user-friendly way
    elif operator == '*':  
        product = num1 * num2 # logic performing multiplication.
        print(f"{num1} * {num2} = {product}") # Prints the result in a user-friendly way
    elif operator == '/':
        if num2 == 0:
            print("Cannot devide by zero!")
        else:
            quotient = num1 / num2  # logic performing division.
            print(f"{num1} / {num2} = {quotient}") # Prints the result in a user-friendly way
    else:
        print("please enter a valid operator!")
    print() 



# ///////////////// Side Notes /////////
r'''
1)
- .isdigit() rejects valid numbers like negatives and decimals
- isdigit() only returns True for strings made entirely of digit characters (0-9). That means:
%
"-5".isdigit()   # False  (the minus sign isn't a digit)
"3.5".isdigit()  # False  (the decimal point isn't a digit)
"7".isdigit()    # True
- So if a user enters -5 or 3.5 — both perfectly reasonable numbers — your program tells them it's "invalid," even though your calculator could technically handle them.
Fix: use a small helper function that actually tries to convert the value, instead of checking string composition:
%
def is_valid_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")

if not is_valid_number(num1) or not is_valid_number(num2):
    print("Please enter a valid input!")
else:
    n1 = float(num1)
    n2 = float(num2)
    product = n1 * n2
    print(f"{n1} * {n2} = {product}")

This correctly accepts negatives and decimals, and rejects true garbage input like "abc".
'''

r'''
2)
Q:
encountered the following error on the final draft:
"Traceback (most recent call last):
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\351-alab2-data_types_variables_operators_basic_io\simple_calculator.py", line 15, in <module>
    if not num1.isdigit() or not num2.isdigit(): # # this code line implements 'isdigit()' as a better technique
           ^^^^^^^^^^^^
AttributeError: 'int' object has no attribute 'isdigit'"
A:
The error is because num1 and num2 are integers, but .isdigit() is a string method — it doesn't exist on integers.
Fix...
Don't cast at input time — keep them as raw strings until after validation:
num1 = input("Please enter the first number: ")   # keep as string for now
num2 = input("Please enter the second number: ")

operator = input("Please choose operator: ")

if not num1.isdigit() or not num2.isdigit():
    print("Please enter a valid input!")
else:
    num1 = int(num1)   # cast only after validation
    num2 = int(num2)
    if operator == '+':
        sum_ = num1 + num2
        print(f"{num1} + {num2} = {sum_}")
    elif operator == '-':
        difference = num1 - num2
        print(f"{num1} - {num2} = {difference}")
    elif operator == '*':
        product = num1 * num2
        print(f"{num1} * {num2} = {product}")
    elif operator == '/':
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            quotient = num1 / num2
            print(f"{num1} / {num2} = {quotient}")
    else:
        print("Please enter a valid operator!")

print()
'''

r'''
3)
AI's version of Final draft:
num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")
operator = input("Please choose operator: ")

if not num1.isdigit() or not num2.isdigit():
    print("Please enter a valid input!")
else:
    num1 = int(num1)
    num2 = int(num2)

    if operator == '+':
        sum_ = num1 + num2
        print(f"{num1} + {num2} = {sum_}")
    elif operator == '-':
        difference = num1 - num2
        print(f"{num1} - {num2} = {difference}")
    elif operator == '*':
        product = num1 * num2
        print(f"{num1} * {num2} = {product}")
    elif operator == '/':
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            quotient = num1 / num2
            print(f"{num1} / {num2} = {quotient}")
    else:
        print("Please enter a valid operator!")

print()
'''

r'''
Bonus: fixing the negative-number rejection too
Since you'll likely want -2 to actually work (it's a valid number, just not accepted by isdigit()), you can swap the validation
to the try/except float() approach we discussed earlier:
def is_valid_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")
operator = input("Please choose operator: ")

if not is_valid_number(num1) or not is_valid_number(num2):
    print("Please enter a valid input!")
else:
    num1 = int(num1)
    num2 = int(num2)

    if operator == '+':
        ...
'''

