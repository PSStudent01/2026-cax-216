
# Task 2: Creating and Importing a Custom Module
r'''
Task 2: Creating and Importing a Custom Module
    Create a new Python file named utilities.py that defines at least the following functions:
        greet(name): Returns a greeting string for the given name.
        factorial(n): Returns the factorial of n (you may use functions from the math module if needed).
    Organize utilities.py into a package:
        Create a folder named mypackage and move utilities.py inside it.
        Include an empty __init__.py file in the mypackage folder.
    Write another script (e.g., use_utilities.py) that:
        Imports your custom module using the package name (e.g., from mypackage import utilities).
        Calls both greet and factorial functions and prints their outputs.
'''


# //////////////////////////////////// Code Begin:///////////////////////////////////////////////

import math

#r'''  
## Returns a greeting string for a given name.
def greet(name):  
    return (f"Hello {name}!")

# print(greet('Rod')) #  For testing purposes only. Call to function, passing an argument.
#'''

#r''' 
## Returns the factorial of n:
def factorial(n): 
    return math.factorial(n) # 1a)is like saying " 5! = 5 × 4 × 3 × 2 × 1 = 120 ". Is what the requirement actually asks for
    # return (f"The factorial of 5 is {factorial(n)}")
    # return (f"The factorial of {n} is {factorial(n)}")
    # return (f"The factorial of {n} is {math.factorial(n)}") # 1b) I wanted to use for best readibility, but AI suggests putting
                                                              #  the string result in the 'use_utilities.py' file instead





# print(greet('Rod')) # Repositioned this call from its original place above. Should comment out when calling file 'use_utilities.py' is created
# print(factorial(5)) # call to function. Should comment out when calling file 'use_utilities.py' is created
# print(f"The factorial of 5 is {factorial(5)}")
#'''

# //////////////////////////////////// Code End:///////////////////////////////////////////////


# //////////////////////////////////// Side Notes ///////////////////////////////////////////////

r'''
#
- A 'factorial' is a math operation on a whole number. You take the number and multiply it by every whole number below it, all the way down to 1. It's written with an exclamation mark: 5! is read "five factorial."
- Examples:
3! = 3 * 2 * 1 = 6
4! = 4 * 3 * 2 * 1 = 24
5! = 5 * 4 * 3 * 2 * 1 = 120
- Factorials are only defined for zero and positive whole numbers, so something like factorial(-3) or factorial(2.5) doesn't make sense (the math.factorial function raises an error for those).
Where it's used:
- The most common use is counting arrangements. If you have 3 books and want to know how many different orders you can put them in, the answer is 3! = 6.

#
- Note: The quick test only runs when you execute this file directly, BUT NOT when it is imported from another script.
- for example:
if __name__ == "__main__":
    print(greet("Rod"))
    print(factorial(5))
- This keeps your testing, but it won't interfere with the import.


# 
- How to move file to subfolder, both within same directory:
#
psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/356-alab1-modules_packages_pip-rod-gaitan (main)
$ mv utilities.py mypackage/

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/356-alab1-modules_packages_pip-rod-gaitan (main)
$ ls
builtin_usage.py  mypackage/  README.txt

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/356-alab1-modules_packages_pip-rod-gaitan (main)
$ cd mypackage/

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/356-alab1-modules_packages_pip-rod-gaitan/mypackage (main)
$ ls
utilities.py
'''

# ///////////////////////////////////////////////////////////////////////////////////


