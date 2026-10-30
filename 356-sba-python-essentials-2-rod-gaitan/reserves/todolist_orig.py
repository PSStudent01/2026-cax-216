
################# VIP File: this is the original todolist Taks 2 only ############################
'''
I just decided to make a copy of it BEFORE adding the requirements of Task 4 on to it, so as to keep a copy of the original 
Task 2 intact!!!!!!
'''

'''
Task 2: Implement To-Do Manager Functions

Create a new module (e.g., todolist.py) that includes functions to manage tasks:
    - add_task(task_list, title, due_date=None): Creates a new Task and adds it to the list. If due_date is provided as a string, 
    parse it into a datetime.date (assume format “YYYY-MM-DD”). Use exception handling to catch parsing errors and inform the user.
    - complete_task(task_list, index): Marks the task at the given index as completed. If the index is invalid, handle the error 
    gracefully.
    - delete_task(task_list, index): Removes the task at the given index. Include error handling for invalid indices.
    - list_tasks(task_list): Returns or prints a formatted list of tasks showing index, status, title, and due date. Indicate if 
    a task is overdue by comparing the due date with today’s date.
''' 

########################################  Creates a new Task and adds it to the list: ######################################
from task import Task # import class 'Task' from the script 'task'
from datetime import datetime, date # import 'datetime' and 'date' functions from 'datetime' module
r'''
# 1st  Attempt Failed!!!:
%
def add_task(task_list, title, due_date=None):
    # isString = True # if you comment out, That version will crash. You commented out isString = True, so the name isString 
                        # no longer exists, and the first time add_task runs it raises a NameError on the if line.
    if due_date is isString:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    
    new_task = Task(title, due_date)
    # return new_task  # wrong place
    task_list.append(new_task)
    return new_task
    # print(new_task)
'''

# Final Attempt Worked!!!:
# task_list = []  # the actual list, created outside the functions
def add_task(task_list, title, due_date=None):
    if isinstance(due_date, str): # says "if due date input is of string data type... "
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date() # "...then convert 'string due_date' to 'date due_date'"

    new_task = Task(title, due_date) # then using the 'Task()' class imported from 'task.py' script, create a new task...
    task_list.append(new_task) # ...and add such task to the list defined in the 'add_task()' function.
    # print(add_task(task_list)) # this would cause infinite recursion if you ever uncommented it, since the function would call 
                                # itself. It’s safe as a comment.
    return new_task # return the contents of 'new_task' variable
     

print(add_task([], "Testing adding a task", "2026-11-20")) # To test creation or task object:
                                                           # print-calling the 'add_task()' function while passing it 3 arguments.
                                                           # creates a throwaway list, so you can’t see what ended up in it. 
                                                           # To confirm the append works, build the list outside and print it:

# To test if list is being built as you add tasks:
task_list = []
add_task(task_list, "Testing adding a task", "2026-11-20")
add_task(task_list, "Task with no date")

for task in task_list:
    print(task)


############################### Marks the task at the given index as completed. ########################################
r'''
# 1st Attempt Failed!!! 
# Marks the task at the given index as completed:
def complete_task(task_list, index): 
    completed = True
    for task in task_list:
        if task_list[task] is completed:
            # task[0] = '[X]'
            # index = task[0] 
            index = task[0].append('[X]')


# print(add_task([], "Testing adding a task", "2026-11-20"))
complete_task(True)
'''

r''' 
#2nd Attempt Failed!!! 
# Marks the task at the given index as completed. If the index is invalid, handle the error gracefully.:
# {I believe index is for the tasklist's task itself so that you can choose which is completed}
# {user gives index and marks that task's index as completed by placing an 'X' at the beggining of thats task}
%
def complete_task(task_list, index):
    index = task_list[task]
    for task in task_list:
        if index:
            return "completed"

print(complete_task(3))
'''

r''' 
# 3rd Attempt Failed!!! 
task_list = []

def complete_task(task_list, index): 
    # pass
    completed = True
    for task in task_list:
        if task is completed:
            # return "completed"
            # index = task[0].append('[X]')
            # return task[0].append('[X]')
            index = task_list[task]
'''

# Final Attempt Passed !!! 
def complete_task(task_list, index):
    task = task_list[index]   # 1) grab the task at that position
    # task_completed = task.completed 
    task.completed = True     # 2) mark it as completed
    return task # Option 2a:  [X] Task: Testing adding a task (due 2026-11-20)

# complete_task(task_list, 0) # Option 1a
# print(task_list[0]) # Option 1b
print(complete_task(task_list, 0)) # Option 2b: [X] Task: Testing adding a task (due 2026-11-20)

r'''
Renders:
psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials
$ C:/Users/psrga/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/psrga/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/356-sba-python-essentials-2-rod-gaitan/todolist.py"
[-] Task: Testing adding a task (due 2026-11-20)
[-] Task: Testing adding a task (due 2026-11-20)
[-] Task: Task with no date (due None)
[X] Task: Testing adding a task  (due 2026-11-20)
{Notice, it simply added a new task but this time marked with an X, rather than updating the existing task}
'''

########################################## Removes the task at the given index. ###############################################

r''' 
# 1st Attempt Failed!!! 
def delete_task(task_list, index):
    pass
    task = task_list[index]
    task_list.pop(task)
    return(task)

print(delete_task(task_list, 0))

- This generates an error as follows:  TypeError: 'Task' object cannot be interpreted as an integer
- The error comes from task_list.pop(task). pop() expects a position (a number), but you gave it the task object itself, so 
Python raises a TypeError.
- You already have the task on the line above. To remove it, pass the index instead:
'''

# 2nd Attempt Worked!!! 
def delete_task(task_list, index):
    task = task_list[index]
    # task_list.pop(task) # '.pop()' method works on numbers ONLY, NOT strings, so using the str 'task' will cause the exception:
                          # 'TypeError: 'Task' object cannot be interpreted as an integer'
    task_list.pop(index) # so Python gives you the option to refer to that same task, by number as well, iows, by its index.
    return(task)

print(delete_task(task_list, 0))

for task in task_list:
    print(task)

r'''
Returned:
Traceback (most recent call last):
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-sba-python-essentials-2-rod-gaitan\todolist.py", line 152, in <module>
    print(delete_task(task_list, 2))
          ~~~~~~~~~~~^^^^^^^^^^^^^^
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-sba-python-essentials-2-rod-gaitan\todolist.py", line 146, in delete_task
    task = task_list[index]
           ~~~~~~~~~^^^^^^^
IndexError: list index out of range
( "The tasks printed on lines 1 and 4 are repeats or belong to another list, so they don’t add positions to task_list." SEE 
SIDENOTES 3) for the output Im seeing)
Fix: either 
- add more tasks
- or don't go beyond index 1, when deleting since there only 2 tasks currently in your task list.
'''

########################################## Returns or prints a formatted list of tasks ###############################################
''' 
- list_tasks(task_list): Returns or prints a formatted list of tasks showing index, status, title, and due date. Indicate if 
a task is overdue by comparing the due date with today's date.
'''
r''' 
# 1st Attempt - Rendered Object only - Failed!!:
def list_tasks(task_list, index, task.completed, title, due_date):
    pass
    for task in task_list:
        # return task_list
        print(f"Index: {index} - Status: {task.completed} - Title: {title} - Due Date: {due_date}")
        # return f"Index: {index} - Status: {task.completed} - Title: {title} - Due Date: {due_date}"

# print(list_tasks(task_list))
# list_tasks(task_list)
list_tasks(task_list, index, task.completed, title, due_date)
'''

''' 
# 2nd Attempt - Returns only 'index', 'status', 'title' :
def list_tasks(task_list):
    for index, task in enumerate(task_list): # Interesting, usually when you run through a loop, you do so for one item (ex, 'i'),
                                            # in this case however, you're doing it for 2 items ('index', 'task'), 'task' being
                                            # the declared variable to which 'task_list[index]' was assigned to.
                                            # 'enumerate()' gives you the 'position' and the 'task' together, avoiding having 
                                            # to count the  indexes yourself.
        print(f"{index}: {task}") 

# Test for code above:
task_list = []
add_task(task_list, "Past due task", "2020-01-01")   # overdue
add_task(task_list, "Future task", "2026-11-20")     # not overdue
add_task(task_list, "Task with no date")             # no due date

complete_task(task_list, 1)                          # mark the future task done

list_tasks(task_list)

Returns:
0: [-] Task: Past due task (due 2020-01-01)
1: [X] Task: Future task  (due 2026-11-20)
2: [-] Task: Task with no date (due None)

- So this code covers only 'index', 'status', 'title', and 'due date'. Missing is the 'overdue' part which depends on the "date 
import".
'''

# 3rd Attempt - It works!!!! :
def list_tasks(task_list):
    for index, task in enumerate(task_list): # Interesting, usually when you run through a loop, you do so for one item (ex, 'i'),
                                            # in this case however, you're doing it for 2 items ('index', 'task'), 'task' being
                                            # the declared variable to which 'task_list[index]' was assigned to.
                                            # 'enumerate()' gives you the 'position' and the 'task' together, avoiding having 
                                            # to count the indexes yourself
        # print(dir(datetime))
        # print(dir(date))
        overdue = ""
        # if task.due_date < date.today():
        if task.due_date is not None and task.due_date < date.today(): # This says "If today's date is greater/surpassed
                                                                       # 'task.due_date', it means 'task.due_date' is "OVERDUE"
                                                                       # if this calculation is not properly set up, tasks will
                                                                       # be marked "OVERDUE" incorrectly.
                                                                       # Also without "task.due_date is not None", the script
                                                                       # will crash with "TypeError: '<' not supported between
                                                                       # instances of 'NoneType' and 'datetime.date'"as soon as 
                                                                       # it encounters a task that has no due date, bc 'task.due_date'
                                                                       # can not compare to 'None' values                                                 
            overdue = "OVERDUE"

        # print(f"{index}: {task}") 
        print(f"{index}: {task} {overdue}")

# Test for code above:
task_list = []
add_task(task_list, "Past due task", "2020-01-01")   # overdue
add_task(task_list, "Future task", "2026-11-20")     # not overdue
add_task(task_list, "Task with no date")             # no due date

complete_task(task_list, 1)                          # mark the future task done

list_tasks(task_list)


# //////////////////////////////////////////// Side Notes /////////////////////////////////////////////
'''
1)
isinstance() is a built-in function, so you don’t need to import anything to use it.

It takes an object and a type (or a tuple of types) and returns True if the object is an instance of that type, False otherwise:
% 
isinstance("2026-11-20", str)   # True
isinstance(5, str)              # False
isinstance(5, (int, float))     # True (checks against either type)

You can see the full list of built-ins in the Python docs under “Built-in Functions.”
'''

'''
2)
but wait,  I don't see task index '0' being deleted instead I see like an additional task instead:  psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials
$ C:/Users/psrga/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/psrga/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/356-sba-python-essentials-2-rod-gaitan/todolist.py"
[-] Task: Testing adding a task (due 2026-11-20)
[-] Task: Testing adding a task (due 2026-11-20)
[-] Task: Task with no date (due None)
[X] Task: Testing adding a task  (due 2026-11-20)
[X] Task: Testing adding a task  (due 2026-11-20)

Note:  That last line in the output is the deleted task being printed, not an extra task. delete_task removes the task from the 
list and also returns it, and your print(delete_task(task_list, 0)) prints whatever gets returned. So you see the removed task 
one more time.
'''

'''
3)
Your output has 3 task lines at the top, so I see why it looks like index 2 should exist. But the first line doesn’t belong to task_list. I also made a mistake last time: I said an earlier delete had left only one task, and that wasn’t what happened in this run.

Here’s where each line comes from:

[-] Testing adding a task comes from print(add_task([], ...)). That call used a throwaway list, so it was never added to task_list.
[-] Testing adding a task is the first item in task_list (index 0).
[-] Task with no date is the second item in task_list (index 1).
[X] Testing adding a task comes from print(complete_task(task_list, 0)). It’s the same task as line 2, printed again, not a new item.

So task_list has only 2 tasks, at positions 0 and 1. Position 2 would be a third task, which doesn’t exist, so you get IndexError.

The tasks printed on lines 1 and 4 are repeats or belong to another list, so they don’t add positions to task_list.
'''