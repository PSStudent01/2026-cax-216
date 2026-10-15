'''
Task 2: List Management with Error Handling
    Write a Python script (e.g., list_manager.py) that manages a list of integers using a text-based menu. The menu should offer
    the following options:
        (a) Add a number: Prompt the user for an integer and append it to the list.
        (b) Remove a number: Prompt for an index and attempt to remove the element at that index using list.pop(index).
        (c) Display the list: Print the current list of numbers.
        (d) Quit: Exit the program.
    Use a loop to continuously display the menu until the user chooses to quit. <------{ STOPPED HERE 10-14-26!!! }
    Implement error handling using try/except:   
        Catch errors when a non-integer is entered for the number or index.
        Catch an IndexError if the user provides an invalid index for removal.
    Display clear error messages for any exceptions without terminating the program abruptly.
'''

r''' 
# 1st Attempt - Works but needs polishing:
numbers = [12, 45, 7, 89, 23, 56, 3, 71, 34]

def add_num():
    integer = int(input("Enter an integer: "))
# integer = input("Enter an integer: ")

# numbers = numbers + integer
    numbers.append(integer) # a) Add a number: Prompt the user for an integer and append it to the 'numbers' list.
    ######## print(numbers)
# numbers.pop(numbers)
# numbers.pop(int(integer[-1]))# 
# numbers.pop(integer)
# numbers.pop(numbers[integer])
def subtract_num():
    numbers.pop(-1) # (b) Remove a number: Prompt for an index and attempt to remove the element at that index using list.pop(index).
    ######## print(numbers)

def display_list():
    print(numbers) # (c) Print the current list of numbers.

def exit_app():
    exit()


def main():
    selection = ""
    while selection != 'd':
        # selection = input("Select a menu option: ")
        print("""Integers menu: 
            (a) Add a number
            (b) Remove a number 
            (c) Display the list 
            (d) Quit
            """)
        selection = input("Select a menu option: ")

        if selection == 'a':
            add_num()
        if selection == 'b':
            subtract_num()
        if selection == 'c':
            display_list()
        if selection == 'd':
            exit_app()
        #else:
            #print("Enter a valid option!")
main()
'''

'''
Needed fixes:
1. 
subtract_num() doesn't prompt for an index. It always pops the last item (-1). The lab wants you to 
- ask the user for an index, 
- convert it with int(), 
- and pass it to pop. That's also where your IndexError and ValueError handling will go later.
....{PENDING}
2. 
exit_app.() does nothing. Writing exit without parentheses just names the function without calling it. You don't need it, 
though. [[[[When the user picks d, selection != 'd' becomes False and the loop ends by itself]]]. You can delete the function, 
or use that branch to print a goodbye message....{DONE in "2nd Attempt"}
3. 
Use elif and else instead of separate ifs. Your four 'if' statements all get checked on every pass, even after one matches. 
With 'elif', Python stops at the first match, and a final else can handle invalid options. You already have that idea in your 
commented-out lines....{DONE in "2nd Attempt"}
'''

r''' 
# 2nd Attempt - Works Perfectly for points 1) & 2) of Task 2:
numbers = [12, 45, 7, 89, 23, 56, 3, 71, 34]

def add_num():
    integer = int(input("Enter an integer: "))
# integer = input("Enter an integer: ")

# numbers = numbers + integer
    numbers.append(integer) # a) Add a number: Prompt the user for an integer and append it to the 'numbers' list.
    ######## print(numbers)
# numbers.pop(numbers)
# numbers.pop(int(integer[-1]))# 
# numbers.pop(integer)
# numbers.pop(numbers[integer])
def subtract_num():
    # numbers.pop(-1) # (b) Remove a number: Prompt for an index and attempt to remove the element at that index using list.pop(index).
    ######## print(numbers)
    index = int(input("Enter the index to remove: "))
    removed = numbers.pop(index)
    # print(f"Removed: {removed}")
    print("Removed: ", removed)
    print(numbers)

def display_list():
    print(numbers) # (c) Print the current list of numbers.

#def exit_app(): # 1)You don't need it. When the user picks d, selection != 'd' becomes False and the loop ends by itself
    #exit() # 2)You don't need it. When the user picks d, selection != 'd' becomes False and the loop ends by itself


def main():
    selection = ""
    while selection != 'd':
        # selection = input("Select a menu option: ")
        print("""\nIntegers menu: 
            (a) Add a number
            (b) Remove a number 
            (c) Display the list 
            (d) Quit
            """)
        selection = input("Select a menu option: ")

        if selection == 'a':
            add_num()
        elif selection == 'b':
            subtract_num()
        elif selection == 'c':
            display_list()
        elif selection == 'd':
            #exit_app() # 3) You don't need it. When the user picks d, selection != 'd' becomes False and the loop ends by itself
            print("Good-Bye! \n") # 4) Instead, skip the logic and go straight into a final message, example "Good-Bye!"
        else:
            print("Enter a valid option!")
main()
'''

r''' 
# THIS IS PROBABLY USELESS, DELETE IT ALL, i already added the .pop(index) to the 2nd attempt above
# 3rd Attempt:
numbers = [12, 45, 7, 89, 23, 56, 3, 71, 34]

def add_num():
    integer = int(input("Enter an integer: "))
# integer = input("Enter an integer: ")

# numbers = numbers + integer
    numbers.append(integer) # a) Add a number: Prompt the user for an integer and append it to the 'numbers' list.
    ######## print(numbers)
# numbers.pop(numbers)
# numbers.pop(int(integer[-1]))# 
# numbers.pop(integer)
# numbers.pop(numbers[integer])
def subtract_num():
    # numbers.pop(-1) # (b) Remove a number: Prompt for an index and attempt to remove the element at that index using 
                        # list.pop(index), and '-1' is an INDEX, '.pop()' only acts on indexes NOT numbers. 
    ######## print(numbers)
    index = int(input("Enter the index to remove: "))
    removed = numbers.pop(index)
    # print(f"Removed: {removed}")
    print("Removed: ", removed)
    print(numbers)

def display_list():
    print(numbers) # (c) Print the current list of numbers.

#def exit_app(): # 1)You don't need it. When the user picks d, selection != 'd' becomes False and the loop ends by itself
    #exit() # 2)You don't need it. When the user picks d, selection != 'd' becomes False and the loop ends by itself


def main():
    selection = ""
    while selection != 'd':
        # selection = input("Select a menu option: ")
        print("""\nIntegers menu: 
            (a) Add a number
            (b) Remove a number 
            (c) Display the list 
            (d) Quit
            """)
        selection = input("Select a menu option: ")

        if selection == 'a':
            add_num()
        elif selection == 'b':
            subtract_num()
        elif selection == 'c':
            display_list()
        elif selection == 'd':
            #exit_app() # 3) You don't need it. When the user picks d, selection != 'd' becomes False and the loop ends by itself
            print("Good-Bye! \n") # 4) Instead, skip the logic and go straight into a final message, example "Good-Bye!"
        else:
            print("Enter a valid option!")
main()
'''


# 3rd Attempt - to complete the remining 2 points 3) & 4):
r'''
When you attempt to enter input other than of integer data type, you encounter the following and the whole app crashes, preventing
the user himself (NOT the developer), the ability to rectify their entry:
%
Select a menu option: a
Enter an integer: w
Traceback (most recent call last):
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-alab2-strings_string_n_list_methods_exceptions\list_manager.py", line 256, in <module>
    main()
    ~~~~^^
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-alab2-strings_string_n_list_methods_exceptions\list_manager.py", line 246, in main
    add_num()
    ~~~~~~~^^
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-alab2-strings_string_n_list_methods_exceptions\list_manager.py", line 207, in add_num
    integer = int(input("Enter an integer: "))
ValueError: invalid literal for int() with base 10: 'w'

Because, you have 2 parts working on this functionality:
- one is your separate function.
- and the other is the call to function from the main function.
..it looks like you apply your try_except handler to the fucntion itself:
'''
numbers = [12, 45, 7, 89, 23, 56, 3, 71, 34]
# numbers = [ ]

def add_num():
    try: # 1) if the following code throws an error (itc, a 'ValueError') due to invalid data input....
        integer = int(input("Enter an integer: "))
        # integer = input("Enter an integer: ")

        # numbers = numbers + integer
        ######## print(numbers)
        # numbers.pop(numbers)
        # numbers.pop(int(integer[-1]))# 
        # numbers.pop(integer)
        # numbers.pop(numbers[integer])
        numbers.append(integer) # a) Add a number: Prompt the user for an integer and append it to the 'numbers' list.
        print(f"Added: {integer}")
    except ValueError: # 2) replace the ValueError long Traceback message with the following, so that the app will not break and
                       # therefore, allow the user to rectify her/his entry.
                       # [to be clear, user can retry, but not automatically. If you want it to ask again right away, you’d need 
                       # a small loop inside add_num(). The lab doesn’t require that.]
        print("Invalid input: please enter a whole number.")

def subtract_num():
    try:
        # numbers.pop(-1) # (b) Remove a number: Prompt for an index and attempt to remove the element at that index using list.pop(index).
        ######## print(numbers)
        index = int(input("Enter the index to remove: "))
        removed = numbers.pop(index)
        # print(f"Removed: {removed}")
        print("Removed: ", removed)
        # print(numbers)
    except IndexError:
        print("Invalid index: please enter a valid index.")
    except ValueError:
        print("Invalid input: please enter a whole number.")

def display_list():
    print(numbers) # (c) Print the current list of numbers.

#def exit_app(): # 1)You don't need it. When the user picks d, selection != 'd' becomes False and the loop ends by itself
    #exit() # 2)You don't need it. When the user picks d, selection != 'd' becomes False and the loop ends by itself


def main():
    selection = ""
    while selection != 'd':
        # selection = input("Select a menu option: ")
        print("""\nIntegers menu: 
            (a) Add a number
            (b) Remove a number 
            (c) Display the list 
            (d) Quit
            """)
        selection = input("Select a menu option: ").lower()

        if selection == 'a':
            add_num()
        elif selection == 'b':
            subtract_num()
        elif selection == 'c':
            display_list()
        elif selection == 'd':
            #exit_app() # 3) You don't need it. When the user picks d, selection != 'd' becomes False and the loop ends by itself
            print("Good-Bye! \n") # 4) Instead, skip the logic and go straight into a final message, example "Good-Bye!"
        else:
            print("Enter a valid option!")
main()

# //////////////////////////////// Side Notes ///////////////////////////////////////

r'''   
#
Try and except example for illustration purposes:
- referencing the example below:
The risky line is int(input(...)), because that's where a ValueError is raised when the user types something like abc or 3.5. 
Put that line (and anything that depends on it) in a try block, then add an except ValueError that prints a friendly message.
%
The pattern, on a different task:
try:
    age = int(input("Enter your age: "))
    print("Next year you'll be", age + 1)
except ValueError:
    print("That's not a whole number. Try again.")

- If int() succeeds, the rest of the try block runs and the except is skipped.
- If int() fails, Python jumps straight to the except, skipping the remaining lines in try.
- Either way, the program keeps running instead of crashing.

#
Q:
- Does is matter, which order I placed handlers when there are more than 1?
A:
- For these two, no. ValueError and IndexError are unrelated, and a single error can only be one of them, so only one handler 
can ever match.
- However, under different cicumstances, order does matter when one exception is a more general version of another. Python checks
the except clauses from top to bottom and runs the first one that matches. For example, IndexError is a kind of LookupError,
and every exception is a kind of Exception.
- Here's a simplified version of the tree with the ones you're most likely to meet:

BaseException
 ├── KeyboardInterrupt        (user presses Ctrl+C)
 ├── SystemExit               (from exit())
 └── Exception                (parent of almost everything you'd catch)
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError     (bad list position)
      │    └── KeyError       (missing dictionary key)
      ├── ValueError          (right type, bad value)
      ├── TypeError           (wrong type)
      ├── NameError           (undefined variable)
      ├── OSError
      │    └── FileNotFoundError
      └── ... many more
Exception Reule to the above:
Put the exceptions you expect (ValueError, IndexError, ZeroDivisionError, and so on) first.
If you add a catch-all, make it except Exception: and put it last.
If two exceptions are unrelated, like ValueError and IndexError, their order doesn't matter.

#
Optional polish, not required by the lab:
- Case: typing A or D currently gives “Enter a valid option!”. Adding .lower() (selection = input(...).lower()) fixes that.
- Feedback on add: add_num() prints nothing when it succeeds, so the user has to pick (c) to see the result. A short message like print("Added:", integer) would make it clearer.
- Starting list: it's pre-filled with numbers. That'ss fine for the lab, but you might start with [] for the final version, or keep it so graders have data to test removal against.

#
Tests:
- Add a valid number, then display the list ...{PASSED!}
- Add abc. You should see the error message and the menu again ...{PASSED!}
- Remove a valid index, such as 0 ...{PASSED!}
- Remove with abc, then with 50 ...{PASSED!}
- Remove from an empty list (remove everything first, then try again) ...{PASSED!}
- Enter an invalid menu option, then quit with d  ...{PASSED!}

#
VIP:  YOU PLACE THE 'Try' handler around that which causes (raises) the error message to beging with!!!!!!
'''