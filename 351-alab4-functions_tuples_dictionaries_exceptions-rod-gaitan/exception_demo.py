'''
Write a script exception_demo.py that contains the following:
- A function safe_divide(a, b) that returns the result of a / b if b is not zero. If b is zero, the function should raise a ValueError with a message like “Cannot divide by zero”.
- Use a try/except structure to call safe_divide with some test values that include a zero divisor. Catch the ValueError and print an error message to the user.
- Include a finally clause in the try/except that prints a message like “Division operation completed” whether or not an error occurred.
- Also demonstrate catching a generic exception by performing an unsafe operation (for example, converting an invalid string to int in a try block) and catching the generic Exception to print a message.
This will showcase your understanding of raising and catching exceptions.
'''
# ======================================================= WORK BEGINS ================================================== #
###########################################################################################################################

## A function safe_divide(a, b) that returns the result of a / b, the function should raise a ValueError with a message like 
## “Cannot divide by zero”.
r''' 
# Attempt 1 - Failed
def safe_divide(a, b):
    try:
        # if b == 0
        b == 0
    except ValueError:
        print("Cannot divide by zero.")
        # return None
    else:
        return  a / b
'''

r'''   
# Attempt 2 - Semi-Successful:
## It now runs since 'ZeroDivisionError' is the right exception to catch. But it still doesn’t meet the requirement, which says 
## the function should raise a "'ValueError' when b is zero". Yours catches the error inside the function and prints a message, 
## so nothing is raised.
## this function detects the problem and raises it, and the code that calls the function catches it and decides what to do. 
## That’s different from where the function handled the problem itself and returned None, like I did in data_processing.py. For this
## requirement, the function must raise a ValueError, BUT NOT handle the problem and return None.

def safe_divide(a, b):
    try:
         return  a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        # return None

# print/call for test purposes only:
print(safe_divide(10, 5))
print()
print(safe_divide(9, 3))
print()
print(safe_divide(10, 0))
print()
'''

# Attempt 3 - Successful:
def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
''' 
# print/call for test purposes only:
print(safe_divide(10, 5))
print()
print(safe_divide(9, 3))
print()
print(safe_divide(10, 0))
print()
# The output is that a Traceback error is returned. This crash is the proof that the function works
'''

###########################################################################################################################

## Use a try/except structure to call safe_divide with some test values that include a zero divisor. Catch the ValueError 
## and print an error message to the user.

r'''   
# Attempt 1 - Semi-Successful:
## Only one test value is actually caught. Because the zero call is in the same try as the good calls, you can’t test more than one
## bad case, since the first error ends the try block. If you want to show several test values, loop over them with the try 
## inside the loop:
try:
    print(safe_divide(15, 3))
    print()
    print(safe_divide(10, 0))
    print()
    print(safe_divide(3, 0))
    print()
except 
     print("Warning: cannot devide by zero.")
'''

# Attempt 2 - Successful   :
test_values = [(15, 3), (10, 5), (10, 0), (3, 0), (8, 0)]

for a, b in test_values:
    try:
        print(safe_divide(a, b))
    except ValueError as e:
        # print("Warning: cannot divide by zero.") # Removed because, while it does render a message accordigly, it does not 
        # use the exception ('e') that I created earlier in this code to render that message:
        # ('raise ValueError("Cannot divide by zero")')
        print(f"Warning: {e}") # use the exception ('e') that I created earlier
    
###########################################################################################################################

## Include a finally clause in the try/except that prints a message like “Division operation completed” whether or not an error
##  occurred.
    finally:
        print("Division operation completed")
###########################################################################################################################

## Also demonstrate catching a generic exception by performing an unsafe operation (for example, converting an invalid string 
## to int in a try block) and catching the generic Exception to print a message.
try:
    number = int("abc")
    print(number)
except Exception as e:
    print(f"A generic exception was caught: {e}")

# raise ValueError("Cannot divide by zero")


# =================================================== WORK ENDS ================================================== #



# =============================== PENDING ================================================== #

# =============================== SIDE NOTES ================================================== #

r'''
Raising an exception:

1)
- somewhere in an earlier declared function, you'd raise it:
%
raise ValueError("Cannot divide by zero") <------------{assigned message "Cannot divide by zero" to 'ValueError'}

2)
- then you can reference it from different parts in your code, for example itc from a call to function within a loop:
%
test_values = [(15, 3), (10, 5), (10, 0), (3, 0), (8, 0)]

for a, b in test_values:
    try:
        print(safe_divide(a, b))
    except ValueError as e: <-------------------{ then here 'ValueError' passes it message value to 'e' and so now 'e' contains message "Cannot divide by zero"}
        # print("Warning: cannot divide by zero.") # Removed because, while it does render a message accordigly, it does not 
        # use the exception ('e') that I created earlier in this code to render that message:
        # ('raise ValueError("Cannot divide by zero")')
        print(f"Warning: {e}") # use the exception ('e') that I created earlier <-------------------{ then here you print the contents of 'e', aka the message "Cannot divide by zero"}


[Returns.....
"5.0
Division operation completed
2.0
Division operation completed
Warning: Cannot divide by zero
Division operation completed
Warning: Cannot divide by zero
Division operation completed
Warning: Cannot divide by zero
Division operation completed"]

////////////////////////////////////////////////////////////////////////////////////////////////////////////////

## Also demonstrate catching a generic exception by performing an unsafe operation (for example, converting an invalid string 
## to int in a try block) and catching the generic Exception to print a message.
try:
    number = int("abc")
    print(number)
except Exception as e:
    print(f"A generic exception was caught: {e}") <---{here we print not a raised exception, but rather a generic exception}

[Returns generic excption: 
"A generic exception was caught: invalid literal for int() with base 10: 'abc'"]

[[[  Converting a string like "abc" with int() raises a ValueError, and catching it with except Exception as e demonstrates the generic catch:
%
# Demonstrate catching a generic exception
try:
    number = int("abc")   # unsafe operation: "abc" is not a valid integer
    print(number)         # never runs, because int() raises first
except Exception as e:
    print(f"A generic exception was caught: {e}")

Why this works: Exception is the parent class of nearly all built-in errors, including ValueError, TypeError, ZeroDivisionError, and KeyError. So except Exception matches whatever goes wrong in the try block. as e works exactly as before: e points to the exception object, and its message was written by Python’s int() code when the conversion failed.

Why you don’t normally use it: earlier I said a bare except: hides unrelated bugs. except Exception has the same weakness, just slightly narrower (a bare except: also catches things like Ctrl+C). It will catch a typo-caused NameError as readily as the error you meant to handle, so it’s best used as a last-resort safety net after specific handlers. You can show that order in your demo:

%
try:
    number = int("abc")
except ZeroDivisionError:
    print("Caught a division error")        # skipped: wrong type
except Exception as e:
    print(f"Caught a generic exception: {e}")   # catches the ValueError

'''

# =============================== WHAT I LEARNED  ================================================== #
''' 
Raising vs. handling exceptions
raise creates and throws an exception: raise ValueError("Cannot divide by zero"). The function detects the problem and reports it, and the calling code decides what to do.
except catches it. In data_processing.py the function handled the problem itself (warning plus return None). Here the lab asked for the opposite, so the function raises and the caller handles it. You learned to read the requirement’s wording (“return None or print” vs. “raise”) to decide which pattern fits.
An uncaught raise crashes the program with a traceback. Your Attempt 3 crash showed the function was working, and the traceback pointed to the raise line and the call that triggered it.
Choosing the right exception type
Dividing by zero naturally raises ZeroDivisionError, not ValueError. Attempt 1 failed because except ValueError didn’t match, so the program crashed.
Only a matching except runs. Everything else passes through.
Where the message in e comes from
e doesn’t fetch or translate anything. It names the exception object, which already holds the message.
For safe_divide, you wrote that message in the raise line. For the tuple error and int("abc"), Python’s interpreter wrote it.
Printing {e} uses the stored message, so changing the raise wording changes the output without touching the caller. Your own comment captures this: the hardcoded print never used e.
try/except structure
Put the try inside the loop so each test case is handled separately. In one try, the first error skips everything after it.
finally runs after the success path and after the caught error. Five test cases gave five “Division operation completed” lines.
Indentation controls structure: finally has to line up with try and except.
Generic exceptions
except Exception as e catches almost any built-in error, including the ValueError from int("abc"), because ValueError is a subclass of Exception.
It’s a last-resort safety net. Used alone, it hides unrelated bugs, so specific handlers go first, since Python runs the first matching except from top to bottom.
Process lessons
Attempts 1 to 3 in your comments document real debugging: wrong exception type, catching instead of raising, then the correct raise.
Keep each attempt’s comment about that attempt only. Mixing in the fix’s explanation makes the notes confusing.
Test with several values (good, zero, repeated zeros) to show the handling works every time.
Notes for your README

“safe_divide raises a ValueError when the divisor is zero. The calling loop catches it with except ValueError as e and prints the message stored in e. The finally clause prints “Division operation completed” after every attempt, whether it succeeded or raised. A separate demo catches the ValueError from int("abc") using except Exception as e, which works because ValueError is a subclass of Exception.”
''' 