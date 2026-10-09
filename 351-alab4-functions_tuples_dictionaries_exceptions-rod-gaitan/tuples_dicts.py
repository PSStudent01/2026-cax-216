
'''
- Write a script tuples_dicts.py that:
-- Creates a tuple months containing the names of the twelve months.
-- Prints the first and last month from the tuple (index 0 and index -1).
-- Attempts to modify the tuple (e.g., months[0] = "NewMonth") inside a try/except block to demonstrate that tuples are immutable. Catch the exception and print a message like: "Tuples are immutable, error: <error_message>".
-- Creates a dictionary students where keys are student names and values are their grades (choose 3-5 sample name-grade pairs).
-- Adds a new student and grade to the dictionary, then prints all student names and grades.
-- Updates one of the existing student’s grades, then prints the updated entry.
-- Uses a loop to print out each student’s name and grade in a formatted way, e.g., "Alice: 90".
'''

## Create a tuple months containing the names of the twelve months:
print("1) Create a tuple months containing the names of the twelve months:")
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", 
          "December") # Creating a tuple "months" that contains the names of the 12 months.
print(months) # although NOT required, I wanted to ensure I'm displaying outpuht for each requirement.
print()

## Prints the first and last month from the tuple:
print("2) Print the first and last month from the tuple:")
# print(months[0], months[-1]) # Printing the first and last month from the tuple
print(months[0]) # Printing the first month from the tuple
print(months[-1]) # Printing the last month from the tuple
print()

## Attempt to modify the tuple inside a try/except block, to demonstrate that tuples are immutable.
print("3) Attempt to modify the tuple inside a try/except block, to demonstrate that tuples are immutable.")
try:
    # months.sort() # generates an AttributeError ("no attribute 'sort'"), which is different error coming from changing a tuple
    months[0] = "NewMonth" # attempt to modify with string, fails, is caught by the try/catch block and appropriate message displayed!
    # months[0] = "summer" # attempt to modify with another string, fails, is caught by the try/catch block and appropriate message displayed!
    # months[11] = 11  # attempt to modify with integer, fails, is caught by the try/catch block and appropriate message displayed!
                       # Note: use a loop, if you want 3 above scenarios.
# except: # it catches everything, including typos and unrelated bugs
except TypeError as e: # 'except' = says "if the code in the try block raised an exception, check whether I should handle it."
                    # 'TypeError' = is the filter. Only a TypeError is caught here. If something else were raised 
                    # (like the AttributeError from months.sort()), this block would be skipped and the program would crash with 
                    # a traceback.
                    # 'as e' = gives the caught exception object a name, so you can use it inside the block. That's what makes {e} work in your f-string.
                    # ':' = starts the block of code that runs when the catch happens.
    # print("Tuples are immutable, error: <error_message>")
     print(f"Tuples are immutable, error: {e}") # user-friendly error triggered by an attempt to modify the tuple
print()

## Create a dictionary students where keys are student names and values are their grades:
print("4) Create a dictionary students where keys are student names and values are their grades:")
students = {
     "Rob": 75,
     "Mary": 85,
     "Mike": 98,
     "Peter": 52,
     "Emily": 75
}
print(students)
print()

## Add a new student and grade to the dictionary, then print ALL student names and grades:
print("5) Add a new student and grade to the dictionary, then print ALL student names and grades:")
students["Martin"] = 92
print(students)  # although NOT required, I wanted to ensure I'm displaying output for each requirement.
print()  

## Update one of the existing student’s grades, then print the updated entry:
print("6) Update one of the existing student’s grades, then print the updated entry:")
students["Rob"] = 78  # updated grade score from 75 to 78
# print(students["Rob"]) # this sufices, but removed and used more refined explicit version right below.
print(f"Rob: {students['Rob']}") # Alternative, more refined. Note the single quotes inside the double-quoted f-string. 
                                   # Using double quotes both inside and outside would break the string in older Python versions.
print()

## Use a loop to print out each student’s name and grade in a formatted way, e.g., "Alice: 90":
print("7) Use a loop to print out each student's name and grade in a formatted way, e.g., 'Alice: 90':")
for i in students:
     # print(i)
     # print(students[i])
     print(f"{i}: {students[i]}")
print()





# =============================== PENDING ================================================== #
'''
Also, since the assignment asks for notes on each part, a README in the repo with a short section per script would cover all 
five files in one place, with sample outputs included. If you keep this block in calc_with_functions.py, it only covers that 
one script.
'''

# =============================== SIDE NOTES ================================================== #

'''
as e doesn't know anything on its own. The message comes from Python itself, at the moment the error happens.

Here's the sequence:

When you run months[0] = "NewMonth", Python tries to assign to an item and discovers that tuples don't support that. The tuple 
type has no way to handle item assignment.
At that point Python creates an exception object, in this case a TypeError, and builds the message text into it: 'tuple' object 
does not support item assignment. The message is written by Python's developers and baked into the interpreter for this specific
situation.
Python then raises that object, which interrupts your code and looks for a matching except block.
except TypeError as e: says "if the raised exception is a TypeError, catch it and give me a variable name (e) that refers to 
that exception object."

So e is just a name pointing to the exception object that was already created. When you put {e} in an f-string, Python converts
the exception to a string, which gives you its message.

Trying it:
%
try:
    months[0] = "NewMonth"
except TypeError as e:
    print(type(e))   # <class 'TypeError'>
    print(e.args)    # ("'tuple' object does not support item assignment",)
    print(e)         # 'tuple' object does not support item assignment

Also, e is just a conventional name. as error or as err works exactly the same, as long as you use the same name inside the block.
This is also why different errors give different messages. If you did int("abc"), you'd catch a ValueError and e would hold 
"invalid literal for int() with base 10: 'abc'", because that's the message Python attaches to that kind of failure.
'''

# =============================== WHAT I LEARNED  ================================================== #

r'''
Tuples
Creating a tuple with parentheses, and indexing it: months[0] is the first item, months[-1] is the last. Negative indexes count from the end.
Immutability: a tuple can’t be changed after it’s created. Assigning to an item (months[0] = "NewMonth") raises a TypeError.
Different mistakes give different errors. months.sort() raises an AttributeError (tuples have no sort method), which is not the same as the TypeError from item assignment. Your comment calls this out, and it’s exactly why catching the specific type matters.
Exception handling
except TypeError as e catches only that type, and as e names the exception object, which already holds Python’s message ('tuple' object does not support item assignment). Nothing is fetched or translated; your f-string just prints the stored text.
A bare except: catches everything, including typos and unrelated bugs, so a specific type is the better habit.
Lines after the error never run. Once the first assignment raises, Python jumps to except, so the other two assignments wouldn’t execute. You commented them out and noted that a loop would be needed to demonstrate all three. That’s the right fix.
Dictionaries
Creating one with names as keys and numeric grades as values. Numbers were a good choice over letters because they work with later calculations.
Adding a new item: students["Martin"] = 92.
Updating an existing item uses the same syntax, which overwrites the old value: students["Rob"] = 78. If the key exists, it updates; if not, it adds.
Terminology: each key: value pair is an item. Keys must be unique, values don’t have to be (Rob and Emily both started at 75).
Looping over a dictionary: for i in students gives the keys, and students[i] looks up each value.
Strings and f-strings
Quote nesting: f"Rob: {students['Rob']}" uses single quotes inside double quotes so the string doesn’t end early.
Formatting output with f-strings, like "Rob: 78".
Process lessons
Printing for each requirement (numbered headings) makes the sample output easy to match to the lab.
Using comments to explain why, not just what: your except breakdown is a good learning record.
Keeping old experiments commented shows your reasoning, though you may want to trim them.
Tidy before submitting
Section 5 prints the raw dictionary, but the requirement says to print all student names and grades. Your loop in section 7 covers formatted output, but I’d add a loop here too, or at least be aware that a grader could want it in section 5.
Indentation: the print inside except is indented 5 spaces, and the dictionary entries and loop body are too. Use 4 consistently.
Typo: “outpuht” should be “output.”
Comment wording: your comment on the try block says “try/catch”; Python’s term is try/except.
Optional: for name, grade in students.items(): is clearer than for i in students: and students[i], since i suggests a number rather than a name.
Docstring/header: since the submission asks for well-commented code, a short comment at the top stating what the script demonstrates would help.
'''