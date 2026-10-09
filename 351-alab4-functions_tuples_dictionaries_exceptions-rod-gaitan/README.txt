
# =============================== WHAT I LEARNED ================================================== #

#
- basic_functions.py:
greet_user uses a default parameter (name="") so it can be called with or without a name, and prints a generic greeting when the name is empty. add_two_numbers returns the sum instead of printing it, so the caller can print it, store it, or use it in further calculations. is_even uses the modulo operator and returns True or False. No exceptions were needed in this file.

#
- calc_with_functions.py:
Each operation is its own function that returns its result, and calculate uses if/elif to call the right one based on the operator symbol. divide catches ZeroDivisionError and returns a friendly message. The main program wraps the inputs and the calculate call in one try/except ValueError, so invalid numeric input prints a clear message instead of crashing. My first attempt used a separate try/except per input, which left variables undefined after a failure; combining them into one block fixed that.

#
tuples_dicts.py:
A tuple is immutable, so assigning to months[0] raises a TypeError. I caught it with except TypeError as e and printed the message stored in e. I used a dictionary to map student names to grades, added and updated entries by assigning to a key, and looped through the dictionary to print each name and grade.

#
data_processing.py:
An empty tuple has length 0, so dividing by len() raises ZeroDivisionError. get_average_grade catches it, prints a warning, and returns None. The loop stores each result and checks if average is None, printing a friendly ‘not available’ message instead of crashing or displaying None. The edge-case course EdgeCase1 demonstrates this.

#
exception_demo.py:
safe_divide raises a ValueError when the divisor is zero. The calling loop catches it with except ValueError as e and prints the message stored in e. The finally clause prints ‘Division operation completed’ after every attempt, whether it succeeded or raised. A separate demo catches the ValueError from int("abc") using except Exception as e, which works because ValueError is a subclass of Exception.