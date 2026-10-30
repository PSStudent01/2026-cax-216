'''
Task 3: Develop the User Interface

    Create a main script (e.g., main.py) that:
        Presents a text-based menu with the options:
            (A) Add a new task.
            (C) Mark a task as completed.
            (D) Delete a task.
            (L) List all tasks.
            (Q) Quit.
        Implements the menu loop so that after each operation the menu is shown again until the user chooses to quit.
        For each menu option, prompts the user for necessary input and calls the corresponding function from todolist.py.
        Before quitting, prompts the user to save the current task list to a file.
'''

# from task import Task
from todolist import add_task, complete_task, delete_task, list_tasks # importing all functions from 'todolist.py' file
from todolist import load_tasks  # % 1) importing task 'load_task'. This is done at the very end as part of connecting to 
                                 # the "file loading process".
from todolist import save_tasks # [ PART 2a, look at PART 1 in 'todolist.py']
''' 
# Omited these since these functions already exist in the 'todolist.py' file, which we've imported as seen above:
def add_task():
   pass
def completed_task():
    pass
def delete_task():
    pass
def list_all_tasks():
    pass
def quit_tasks():
    pass
'''

def main(): # defining the 'main()' function.
    # task_list = [] # created list container inside 'main()' (or before it), so the same list is passed to every call.
    task_list = load_tasks() # % 2) Replace the above line. This is done at the very end as part of connecting to the "file loading process"
    selection = "" # Since we're working w/ 'while loop', this is starting point. Similar to count = 0 for a 'while' loop.
    # while selection != "q": # says "for as long as the selection made is not 'q' run the following action, see below:"
    while selection not in ("q", "Q"): # says "for as long as the selection made is not 'q' or 'Q', run the following action, 
                                       # see below, which is essentially... 
                                       # a) the persisting 'Main Menu'
                                       # b) prompting user for a 'Main Menu' option, which eventually may turn prompts user for 
                                       # sub-menu options."
        print("""\n==================== Task Manager ==========================: 
            (A) Add a new task.
            (C) Mark a task as completed.
            (D) Delete a task.
            (L) List all tasks. 
            (Q) Quit.
            """)
        selection = input("Select menu option: ") # Selection input function for Main Menu. BTW, without it'll get caught in loop

        # Menu selection to add a task:
        # if selection == 'a' or selection == 'A':
        if selection in ('a', 'A'): # a more simplified approach to the above line
            # pass
            # add_task() # this would never work here!
            title = input("Enter task title: ") # this captures user input specific to adding the task title and stores it in 
                                                # variable 'title' for later manipulation of its contents.
            duedate = input("Enter task due date: ") # this captures user input specific to adding the task due date and stores 
                                                     # it in variable 'duedate' for further manipulation of its contents.
            if duedate == "": # conditional branch says that if no input is entered for 'due date' by the user...
                duedate = None # ...the value None is be reassigned to variable 'duedate'.
            add_task(task_list, title, duedate) # Interesting, here we're calling the function 'add_task(task_list, title, duedate)'
                                                # with all 3 arguments that we need, by importing such function from the 
                                                # 'todolist' script, rather than having the function in this same file and calling it
                                                # from here.

        # Menu selection to mark a task completed:
        # elif selection == 'c' or selection == 'C':
        elif selection in ('c', 'C'): # a more simplified approach to the above line
            # pass
            # complete_task() # this would never work here!
            # title = input("Enter task title: ")
            # duedate = input("Enter task due date: ")
            list_tasks(task_list) # here we momentarily extract/pull the 'task_list' by calling its fuction 
                                    # 'list_tasks(task_list)' to manipulate one of its items (itc, mark task(0) as completed!).
                                    # you can place it further to the bottom as seen below and it'll still work.
            try: # A) Exception handling for invalid characters and crashes ONLY, NOT for bad index.
                index = int(input("Number of the task to mark completed: ")) # this captures user input identifying which task INDEX
                                                                         # is to be marked completed & store it in variable 'index' 
                                                                         # for further manipulation of its contents, like 
                                                                         # identifying the item to be marked completed.
                #list_tasks(task_list) # see comments 2 line above.
                complete_task(task_list, index) # Interesting, here we're calling the function 'complete_task(task_list, index)'
                                            # with all 2 arguments that we need, by importing such function from the 
                                            # 'todolist' script, rather than having the function in this same file and calling it
                                            # from here.
            except ValueError:  # B) Exception handling for invalid characters and crashes ONLY, NOT for bad index.
                print("\nError: please enter a number, like 0 or 1.")  # C) Exception handling for invalid characters and crashes ONLY, NOT for bad index.

        # Menu selection to delete a particular task:
        # elif selection == 'd' or selection == 'D':
        elif selection in ('d', 'D'): # a more simplified approach to the above line
            # pass
            # delete_task() # this would never work here!
            list_tasks(task_list) # here we momentarily extract/pull the 'task_list' by calling its fuction 
                                  # 'list_tasks(task_list)' to manipulate one of its items (itc, delete task(0)).
                                  # you can place it further to the bottom as seen below and it'll still work.
            try: # A) Exception handling for invalid characters and crashes ONLY, NOT for bad index.
                index = int(input("Number of the task to be deleted: ")) # this captures user input identifying which task INDEX
                                                                     # is to be deleted & store it in variable 'index' 
                                                                    # for further manipulation of its contents, like identifying
                                                                    # the item to be deleted.
                # list_tasks(task_list) # see comments 2 line above.
                # task_list.pop(index)
                delete_task(task_list, index) # Interesting, here we're calling the function 'delete_task(task_list, index)'
                                          # with all 2 arguments that we need, by importing such function from the 
                                          # 'todolist' script, rather than having the function in this same file and calling it
                                          # from here.
            except ValueError: # B) Exception handling for invalid characters and crashes ONLY, NOT for bad index.
                print("\nError: please enter a number, like 0 or 1.") # C) Exception handling for invalid characters and crashes ONLY, NOT for bad index.

        # Menu selection to list all existing tasks:
        # elif selection == 'l' or selection == 'L':
        elif selection in ('l', 'L'): # a more simplified approach to the above line
            # pass
            # list_tasks() # this would never work here!
            list_tasks(task_list) # here we momentarily extract/pull the 'task_list' by calling its function 
                                  # 'list_tasks(task_list)' to manipulate one of its items (itc, simply VIEW the entire list).

        # Menu selection to quit out of the script/app:
        # elif selection == 'q' or selection == 'Q':
        elif selection in ('q', 'Q'): # a more simplified approach to the above line
            # pass
            # print("Please save the current task to a file! \n")
            # exit_app() # this would never work here!
            save = input("Save tasks before quitting? (Y/N): ").lower()# this captures user input identifying whether yes or no
                                                                     # to saving the list of tasks and then storing the answer in
                                                                     # variable 'save' for further manipulation of its contents, like identifying
                                                                    # the for the answer to be processed by the next nested
                                                                    # logical branch.
            if save == 'y':
                # print("Saving...") # [ PART 2b, look at PART 1 in 'todolist.py']. Here we replace this placeholder with 
                                     # code blcok below:
                save_tasks(task_list) # [ PART 2c, look at PART 1 in 'todolist.py']. is a 'function call'. It runs the 'save_tasks'
                                      # function you wrote in 'todolist.py' and hands it the current list of tasks to write to the file.
                print("Tasks saved!")
            print("Good Bye! \n") # 2)... move to here, so that now The spec just says to prompt before quitting, and either 
                                  # answer should end the program cleanly.
            #else:
                #print("Good Bye! \n") # 1) The goodbye only prints when the user answers anything other than y. Your if/else puts 
                                       # print("Good Bye!") in the else, so if the user types y, it prints “Saving...” and then 
                                       # never says goodbye. The spec just says to prompt before quitting, and either answer 
                                       # should end the program cleanly.
                                       # Fix: Moving the 'goodbye' out of this 'else' bracnh into the 'elif' branch above...

        # Default message if no valid entry made:
        else:
            print("Enter a valid option!")
        
main() # calls the function 'main()' to action.

'''
################################ STOPPED 10-28-26 #######################
################################ PENDING ################################
One heads-up: negative numbers. Python treats -1 as “the last item”, so typing -1 would complete or delete the last task instead of raising an error. If you want to block that, add if index < 0: raise IndexError as the first line inside the try in each function. It’s optional.

3. load_tasks: the None issue from earlier. Since add_task returns None on a bad date, add a check before the line that sets completed:

python
task = add_task(task_list, title, duedate)
if task is not None:
    task.completed = (completed == 'True')
'''


############################### STOPPED 10-27-26 ########################################
r'''
# PENDING Exception Management:
Q:
ok but I'm assuming we would have to do it for each of the 3 script files? if so can we do one at a time starting with 'task.py'?
A:
Not quite. Exception handling only goes where something can actually fail, and 'task.py' has nothing like that. It only stores three values and builds a string, so there’s nothing to wrap in try/except. Here is where each remaining piece lives:

File	                What can fail	                                                                                    Handling
task.py	                Nothing	                                                                                            None needed
todolist.py	            Bad date in add_task, bad index in complete_task and delete_task, file I/O (the part we just did)	try/except ValueError and IndexError; I/O is already done
main.py	                int(input(...)) when the user types letters	                                                        try/except ValueError

So task.py is already finished as far as the rubric goes. If you want to go one file at a time, the order I’d suggest is:
1) task.py: done, nothing to add.
2) todolist.py: the remaining three functions. File I/O is already covered.
3) main.py: the int(input(...)) calls in the complete and delete branches.
''' 

# /////////////////////////////////////// Side Notes ////////////////////////////////////////

r'''
Yes, that’s exactly what I meant. Your output shows both crashes:

Bad index: 90 at the delete prompt raised IndexError: list index out of range from task = task_list[index] in delete_task.
Letters: text_input_here_will_crash_script at the complete prompt raised ValueError: invalid literal for int() from the int(input(...)) line in main.py.

Both kill the program, which the rubric’s “does not crash under erroneous input” line penalizes. Don’t put those tracebacks in your submission log. Here are the fixes, one file at a time.

1. todolist.py: bad index in complete_task and delete_task

python
def complete_task(task_list, index):
    try:
        task = task_list[index]
        task.completed = True
        return task
    except IndexError:
        print(f"Error: there is no task number {index}.")
        return None


def delete_task(task_list, index):
    try:
        task = task_list.pop(index)
        return task
    except IndexError:
        print(f"Error: there is no task number {index}.")
        return None

2. main.py: letters at the number prompt

Wrap the int(input(...)) in the complete branch and the delete branch:

python
elif selection in ('c', 'C'):
    list_tasks(task_list)
    try:
        index = int(input("Number of the task to mark completed: "))
        complete_task(task_list, index)
    except ValueError:
        print("Error: please enter a number, like 0 or 1.")

elif selection in ('d', 'D'):
    list_tasks(task_list)
    try:
        index = int(input("Number of the task to be deleted: "))
        delete_task(task_list, index)
    except ValueError:
        print("Error: please enter a number, like 0 or 1.")

One heads-up: negative numbers. Python treats -1 as “the last item”, so typing -1 would complete or delete the last task instead of raising an error. If you want to block that, add if index < 0: raise IndexError as the first line inside the try in each function. It’s optional.

3. load_tasks: the None issue from earlier. Since add_task returns None on a bad date, add a check before the line that sets completed:

python
task = add_task(task_list, title, duedate)
if task is not None:
    task.completed = (completed == 'True')

Re-run these demos for your log:

Select menu option: c
Number of the task to mark completed: 99
Error: there is no task number 99.

Select menu option: d
Number of the task to be deleted: abc
Error: please enter a number, like 0 or 1.

Both should print the message and bring the menu back instead of a traceback. Then include them, along with the bad-date demo, in your sample_output.txt.
'''

'''
To test the final Script:
#
To test: 
- add a task, 
- press q, answer y, 
- then open tasks.csv and check your new task is in it.
- Run main.py again and press l to confirm it loads back. That round trip is the persistence demo the assignment wants for the sample outputs.
'''

r'''
Traceback (most recent call last):
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-sba-python-essentials-2-rod-gaitan\main.py", line 142, in <module>
    main() # calls the function 'main()' to action.
    ~~~~^^
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-sba-python-essentials-2-rod-gaitan\main.py", line 113, in main
    list_tasks(task_list) # here we momentarily extract/pull the 'task_list' by calling its function
    ~~~~~~~~~~^^^^^^^^^^^
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-sba-python-essentials-2-rod-gaitan\todolist.py", line 282, in list_tasks
    for index, task in enumerate(task_list): # Interesting, usually when you run through a loop, you do so for one item (ex, 'i'),
                       ~~~~~~~~~^^^^^^^^^^^
TypeError: 'NoneType' object is not iterable
[[[
TypeError: 'NoneType' object is not iterable means task_list is None when list_tasks tries to loop over it. So load_tasks() 
returned None instead of a list.
Cause: return task_list is still indented inside the with block. In the file you pasted, it sat at 12 spaces. If Python never
gets into that block (for example, because tasks.csv isnt found), it never reaches the return, and the function hands back None.
]]]
'''

r'''
Issue:
- when entering a non-valid date, an exception is encountered when you press enter. you get teh following exception:
%
==================== Task Manager ==========================: 
            (A) Add a new task.
            (C) Mark a task as completed.
            (D) Delete a task.
            (L) List all tasks. 
            (Q) Quit.
            
Select menu option: l
0: [-] Task: Past due task (due 2020-01-01) OVERDUE
1: [X] Task: Future task  (due 2026-11-20) 
2: [-] Task: No date task (due None) 
3: [-] Task: super_test (due 2026-10-30) 

==================== Task Manager ==========================: 
            (A) Add a new task.
            (C) Mark a task as completed.
            (D) Delete a task.
            (L) List all tasks. 
            (Q) Quit.
            
Select menu option: a
Enter task title: test 1
Enter task due date: 2026-36-36
Traceback (most recent call last):
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-sba-python-essentials-2-rod-gaitan\main.py", line 147, in <module>
    main() # calls the function 'main()' to action.
    ~~~~^^
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-sba-python-essentials-2-rod-gaitan\main.py", line 65, in main
    add_task(task_list, title, duedate) # Interesting, here we're calling the function 'add_task(task_list, title, duedate)'
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-sba-python-essentials-2-rod-gaitan\todolist.py", line 144, in add_task
    due_date = datetime.strptime(due_date, "%Y-%m-%d").date() # "...then convert 'string due_date' to 'date due_date'"
               ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\psrga\AppData\Local\Programs\Python\Python314\Lib\_strptime.py", line 815, in _strptime_datetime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
                                    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\psrga\AppData\Local\Programs\Python\Python314\Lib\_strptime.py", line 555, in _strptime
    raise ValueError("time data %r does not match format %r" %
                     (data_string, format))
ValueError: time data '2026-36-36' does not match format '%Y-%m-%d'

Fix:
in 'todolist.py' script, wrap "strptime" in the 'add_task' function:
%
def add_task(task_list, title, due_date=None):
    if isinstance(due_date, str):
        try:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            print(f"Error: '{due_date}' is not a valid date. Use YYYY-MM-DD.")
            return None

    new_task = Task(title, due_date)
    task_list.append(new_task)
    return new_task

Important Note:
There's one important distinction:
- Your existing try/except ValueError handles invalid date input. For example, if someone enters 2026-15-40, it displays an 
error instead of crashing.
- Task 4's file I/O error handling concerns operations such as opening, reading, and writing your task file. Those errors 
typically involve exceptions such as OSError or IOError.
Your add_task() function doesn't read from or write to a file, so you don't need to add file I/O exception handling to this 
function to satisfy that part of the rubric.

Note:
- Your try/except ValueError block satisfies the invalid date handling requirement ONLY!
- Need to identify more exceptions, that may come about and handle them:
%
What you need for file I/O: In the part of your code that loads or saves tasks, you'll need try/except blocks to handle errors 
such as:
- FileNotFoundError — your program attempts to open a file doesn't exist (although your program may handle this normally using
'os.path.exists())'. For example, temporarily add this to a test script or run it separately in your terminal:
%
with open("missing_tasks.txt", "r") as file:    contents = file.read()
- PermissionError — Python doesn't have permission to access the file. Your program tries to read or write a file without the
 necessary permissions.
- OSError — another operating-system error occurs while reading or writing. An operating-system-level problem prevents a file 
operation. This is a broader category that includes FileNotFoundError and PermissionError.
'''

# ////////////////////////////////////////// PENDING //////////////////////////////////////////////////
'''
(Optional) Task 5: External Package Enhancement

    Optionally, use a third-party package (such as colorama or prettytable) to enhance the user interface:
        For example, color-code overdue tasks or format the task list as a table.
        Include a comment at the top of your code explaining how to install the package (e.g., # Requires colorama; install with: pip install colorama).

'''