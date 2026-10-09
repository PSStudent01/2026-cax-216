'''
Create a script data_processing.py that simulates a simple data processing scenario:
- Define a function get_average_grade(grades_tuple) that takes a tuple of numeric grades and returns the average. Include a try/except to handle the case if the tuple is empty (to avoid division by zero), returning None or printing a warning in that case.
- Define a dictionary course_grades where keys are course names (e.g., “Math”, “Science”, “History”) and values are tuples of grades.
- Use a loop to iterate over course_grades. For each course, call get_average_grade(grades_tuple) and print a message like: "The average grade for Math is 85.2". Handle any None values or exceptions gracefully.
- Intentionally include an edge case, such as one course having an empty tuple of grades, to demonstrate your exception handling works.
'''

# ======================================================= WORK BEGINS ================================================== #
###########################################################################################################################

## Define a function get_average_grade(grades_tuple) that takes a tuple of numeric grades and returns the average.
r''' 
# Old code block:
grades_tuple = (78, 85, 98, 52, 75, 92) # 1) defining/declaring tuple 'grades_tuple'

def get_average_grade(grades_tuple): # 2) declaring function 'get_average_grade' to receive values for tuple 'grades_tuple'
    for i in grades_tuple: # 3) loop iterates through tuple, one number at a time
        return sum(grades_tuple) / len(grades_tuple) # 4) calculates their total sum; then devides it by total count of numbers
                                                     # in the tuple to get the average; returns the avg.

print(get_average_grade(grades_tuple)) # 5) calls the function "get_average_grade()" while passing it the 'grades_tuple' and 
                                        # simultaneously printing the results.
'''
grades_tuple = (78, 85, 98, 52, 75, 92) # 1) defining/declaring tuple 'grades_tuple'

def get_average_grade(grades_tuple): # 2) declaring function 'get_average_grade' to receive values for tuple 'grades_tuple'
    # for i in grades_tuple: # 3) loop iterates through tuple, one number at a time. UPDATE: Had to remove it bc it prevents
                             # the calls the function 'get_average_grade()' without a tuple from executing
        try: # 6a) try/except block build
            return sum(grades_tuple) / len(grades_tuple) # 4) calculates their total sum; then devides it by total count of numbers
                                                         # in the tuple to get the average; returns the avg.
        except ZeroDivisionError: # 6b) try/except block build
            # Handle the empty-tuple case instead of crashing
            print("Warning: cannot calculate an average of an empty tuple.") # 6c) try/except block build
            return None # 6d) # try/except block build

print(get_average_grade(grades_tuple)) # 5) calls the function "get_average_grade()" while passing it the 'grades_tuple' and 
                                        # simultaneously printing the results.
                                         # Rendering:
                                         ## 80.0 as teh avg of all 6 numbers in the tuple

###### Handling Exception for 'get_average_grade' with empty argument - Attempt 1 - Fails: ######
## Empty tuple case triggers and exception, so we attempt to handle a None value as a result of calling a function with an 
## empty argument, but it returns 'None'.
## So decided to replace this line with the code block below, see 'Handling Attempt 2':
# print("Average:", get_average_grade(())) # 6e) try/except block build. Calls function 'get_average_grade()' with an empty tuple!
                                         # Rendering:
                                         ## "Warning: cannot calculate an average of an empty tuple.""
                                         ## "Average: None"

###### Handling Exception for 'get_average_grade' with empty argument - Attempt 2 - Successful: ######
# Attempt to handle a None value as a result of calling a function with an empty argument.
result = get_average_grade(()) # stored the returned value from a 'get_average_grade' function call with empty argument
if result is None:
    print("Average: not available (no grades to average)")
else:
    print("Average:", result)
print()

###########################################################################################################################

## Define a dictionary 'course_grades' where keys are course names (e.g., “Math”, “Science”, “History”) and 
# values are tuples of grades.

grades_tuple1 = (78, 85, 98, 52, 75, 92) # assigning 1st tuple to variable "grades_tuple1", to make tuple indirectly available
grades_tuple2 = (88, 91, 67, 74, 83, 95) # assigning 2nd tuple to variable "grades_tuple2", to make tuple indirectly available
grades_tuple3 = (60, 72, 89, 94, 55, 81) # assigning 3rd tuple to variable "grades_tuple3", to make tuple indirectly available
grades_tuple4 = () ### EDGE CASE tuple ###: course having an empty tuple of grades, to demonstrate your exception handling works.

course_grades = {  # Defining dictionary 'course_grades' with...
     "Math": grades_tuple1,  # key 'Math' and tuple value 'grades_tuple1'  
     "Science": grades_tuple2,  # key 'Science' and tuple value 'grades_tuple2'  
     "History": grades_tuple3,  # key 'History' and tuple value 'grades_tuple3'   
     "EdgeCase1": grades_tuple4 ### EDGE CASE dictionary item ###: key 'EdgeCase1' and tuple value 'grades_tuple4'  
}

###########################################################################################################################

## Use a loop to iterate over course_grades. For each course, call function 'get_average_grade(grades_tuple)' and print a
## message like: "The average grade for Math is 85.2". Handle any None values or exceptions gracefully.
for i in course_grades: # loop to iterate over each key:value pair of 'course_grades' dictionary
     # get_average_grade(grades_tuple)
     # get_average_grade(course_grades[i]) # [@!-1] REMOVED: this works well to get the average of grade scores for each course. 
                                         # However, this call is unnecessary here, because the same call happens within
                                         # the 'print' function below, causing teh app to call the function twice per course.
                                         # and for the edge case warning "Warning: cannot calculate an average of an empty tuple." to get displayed
                                         # twice.
     # print(i) # renders only course names
     # print(f"The average grade for Math is {get_average_grade(course_grades)}") # renders Traceback error, bc parameter being passed to it is incorrect
     # print(f"The average grade for Math is {get_average_grade(grades_tuple)}") # renders the score avg for only 'Math' course 3x.
     # print(f"The average grade for Math is {get_average_grade(course_grades[i])}") # renders the score avg for each individual course, associates each with 'Math' only.
    # {symbol ``} print(f"The average grade for {i} is {get_average_grade(course_grades[i])}") # [@!-2] Finally, renders the score avg for each individual course, while correctly mapping each avg to the appropriate course.
                                                                                 # even still I had to remove it anyway, because
                                                                                 # it does not handle the exception apropriately:
                                                                                # "The average grade for EdgeCase1 is None"

    ###### {symbol ``}  Handling Exception for 'get_average_grade' with empty argument - Attempt 2 - Successful: ######
    # Attempt to handle a None value as a result of calling a function with an empty argument.
    average = get_average_grade(course_grades[i])   # call once, store the result

    if average is None:
        print(f"The average grade for {i} is not available (no grades).")
    else:
        print(f"The average grade for {i} is {average}")

# =================================================== WORK ENDS ================================================== #

# =============================== WHAT I LEARNED - (Add to README.txt file!!!!!!)  ================================================== #
'''  
Here’s a summary of what your work in data_processing.py (and this session) shows you learned.

Functions:
- Defining and calling a function that takes a parameter (grades_tuple) and returns a value.
- Return values matter: return hands a result back to the caller. A function with no return, or one that exits early, gives back None by default.
- Calling a function once and storing the result (average = get_average_grade(...)) instead of calling it repeatedly. 
- A tuple holds a fixed sequence of grades, and it can be empty (()).
- Tuples are passed to functions and stored as dictionary values.
- sum() and len() work on a whole tuple, so no loop was needed to compute the average.

Dictionaries:
- Building a dictionary whose keys are course names and values are tuples.
- Looping over it, and looking up values with course_grades[i]. (.items() is the next step: it gives key and value together, so you don’t need the lookup.)

Exceptions:
- try/except with a specific exception: an empty tuple makes len() 0, so the division raises ZeroDivisionError, which your except block catches to print a warning and return None.
- Catching a specific type (ZeroDivisionError, TypeError) rather than a bare except, which would hide unrelated bugs.
- as e names the exception object, which already holds Python’s message. It doesn’t translate anything.
- Execution order: once an exception is raised, the rest of the try block is skipped.

Debugging lessons (the most valuable part):
- Code inside a loop doesn’t run if the loop has zero iterations. Your try/except inside for i in grades_tuple: never ran for an empty tuple. Removing the loop fixed it.
- Handling an exception is not the same as handling its result. Catching ZeroDivisionError returned None, but printing “is None” isn’t graceful. You fixed it by storing the result and checking if result is None.
- Use 'is None', 'not == None'.
- Your commented trial-and-error (Attempt 1 fails, Attempt 2 succeeds) documents real debugging, including why passing course_grades or grades_tuple gave wrong output.

Smaller details
- Python needs straight quotes ("), not curly ones (“ ”) copied from documents.
- An empty tuple () is different from calling a function with no argument, which would raise a different error.
- Only keys must be unique in a dictionary, not values.
- Notes for your README
- “An empty tuple has length 0, so dividing by len() raises ZeroDivisionError. The function catches it, prints a warning, and returns None. The calling code then checks if average is None and prints a friendly message instead of crashing or displaying None.”
'''
# ===================================================================================================================================== #

# =============================== PENDING ================================================== #
'''
Also, since the assignment asks for notes on each part, a README in the repo with a short section per script would cover all 
five files in one place, with sample outputs included. If you keep this block in calc_with_functions.py, it only covers that 
one script.
'''

# =============================== SIDE NOTES ================================================== #
'''
{symbol ``} = 

'''



'''
One small correction to a comment: you wrote that the empty call is made "without a tuple." It actually passes an empty 
tuple, (). That's an important distinction, since calling get_average_grade() with no argument at all would raise a TypeError 
(missing required argument) instead of triggering your ZeroDivisionError handling. Since the lab asks for accurate comments 
on exception handling, I'd change it to something like "Calls the function with an empty tuple ()."

'''

'''  
## AI suggested solution to handling the 2 separate exceptions illustrated in this exercise, caused by passing empty arguments to
## the 2 average functions.
     # if get_average_grade(course_grades[i]) is None: # returns "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
     average = get_average_grade(course_grades)
     if average is None:
         # print(f"No grades available for {course}, so no average was calculated.")
          print(f"No grades available for {i} so no average was calculated.")
     else:
        print(f"The average grade for {i} is {average:.1f}")
###########################
'''

# =============================== WHAT I LEARNED   ================================================== #
'''
Functions
Defining and calling a function that takes a parameter (grades_tuple) and returns a value.
Return values matter: return hands a result back to the caller. A function with no return, or one that exits early, gives back None by default.
Calling a function once and storing the result (average = get_average_grade(...)) instead of calling it repeatedly. Your own comment in the loop captures this: the double call made the warning print twice.
Tuples
A tuple holds a fixed sequence of grades, and it can be empty (()).
Tuples are passed to functions and stored as dictionary values.
sum() and len() work on a whole tuple, so no loop was needed to compute the average.
Dictionaries
Building a dictionary whose keys are course names and values are tuples.
Looping over it, and looking up values with course_grades[i]. (.items() is the next step: it gives key and value together, so you don’t need the lookup.)
Exceptions
try/except with a specific exception: an empty tuple makes len() 0, so the division raises ZeroDivisionError, which your except block catches to print a warning and return None.
Catching a specific type (ZeroDivisionError, TypeError) rather than a bare except, which would hide unrelated bugs.
as e names the exception object, which already holds Python’s message. It doesn’t translate anything.
Execution order: once an exception is raised, the rest of the try block is skipped.
Debugging lessons (the most valuable part)
Code inside a loop doesn’t run if the loop has zero iterations. Your try/except inside for i in grades_tuple: never ran for an empty tuple. Removing the loop fixed it.
Handling an exception is not the same as handling its result. Catching ZeroDivisionError returned None, but printing “is None” isn’t graceful. You fixed it by storing the result and checking if result is None.
Use is None, not == None.
Your commented trial-and-error (Attempt 1 fails, Attempt 2 succeeds) documents real debugging, including why passing course_grades or grades_tuple gave wrong output.
Smaller details
Python needs straight quotes ("), not curly ones (“ ”) copied from documents.
An empty tuple () is different from calling a function with no argument, which would raise a different error.
Only keys must be unique in a dictionary, not values.
Notes for your README

A short version you could adapt: “An empty tuple has length 0, so dividing by len() raises ZeroDivisionError. The function catches it, prints a warning, and returns None. The calling code then checks if average is None and prints a friendly message instead of crashing or displaying None.”

'''

'''
Functions
You defined get_average_grade(grades_tuple), which takes a tuple, computes sum() / len(), and returns the result.
return hands a value back to the caller, and a function that falls off the end returns None by default.
Call a function once and store the result. Your [@!-1] comment records the bug: calling it twice per course printed the empty-tuple warning twice.
Tuples and dictionaries
A tuple can be empty (()), and sum() and len() work on a whole tuple without a loop.
You built a dictionary where keys are course names and values are tuples, including an intentional edge case ("EdgeCase1": ()).
You looped over the dictionary and looked up each value with course_grades[i].
Exception handling
Why it fails: an empty tuple has length 0, so the division raises ZeroDivisionError.
How it’s handled: the except block prints a warning and returns None, so the program doesn’t crash.
Catching a specific exception (ZeroDivisionError) is better than a bare except.
Handling the result, not just the exception

This was the biggest lesson. Catching the error wasn’t enough, because printing “The average grade for EdgeCase1 is None” isn’t graceful. You fixed it by storing the result and checking if average is None, in both the standalone test and the loop. You also used is None rather than == None.

Debugging lessons
Code inside a loop doesn’t run if the loop has zero iterations. The try/except inside for i in grades_tuple: never ran for an empty tuple, so removing the loop fixed it.
Passing the wrong thing gives wrong output. Your commented experiments show that passing course_grades crashed, and passing grades_tuple gave Math’s average three times.
Documenting attempts (Attempt 1 fails, Attempt 2 works) gives you a clear record of your reasoning.
Still to tidy before submitting
Indentation: the try/except inside get_average_grade is still 8 spaces deep. Dedent it to 4, and delete the commented-out for line.
Inaccurate comment: “calls the function without a tuple” should say “with an empty tuple,” since calling with no argument would raise a TypeError.
Docstring: add one to get_average_grade covering the parameter and return value, since the submission asks for that.
Typos: “teh,” “devides,” “apropriately,” and the stray {symbol ``} markers.
Optional: the lab’s example shows 85.2, but yours prints 75.16666666666667. Using {average:.1f} in the else branch rounds it, and it’s safe there because None never reaches that line.

'''