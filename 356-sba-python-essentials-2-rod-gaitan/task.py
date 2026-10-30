'''
Task 1: Define the Task Class
Create a new module (e.g., task.py) and define a class Task with the following:
    Attributes:
        title: A short description of the task.
        due_date: An optional due date (as a datetime.date object or a string).
        completed: A boolean status indicating whether the task is complete.
    Initializer:
        __init__(self, title, due_date=None, completed=False) to set up the attributes.
    Methods:
        __str__(self): Returns a well-formatted string representation of the task, e.g., "[-] Submit assignment 
        (due 2025-03-10)", where [X] indicates a completed task.
'''

class Task:  # 1) Defining class 'Task'...
    def __init__(self, title, due_date=None, completed=False): # 2)...with attributes and an initializer to set up those attributes.
        self.title = title # setting up 'instance attribute assignment' for attribute 'title'
        self.due_date = due_date # setting up 'instance attribute assignment' for attribute 'due_date'
        self.completed = completed  # setting up 'instance attribute assignment' for attribute 'completed'

    # Methods:
    def __str__(self):
        # return f"Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance:.2f}" #2a) Displays cs dashboard by default.
        # "'[-] Submit assignment (due 2025-03-10)', where [X] indicates a completed task."

        if self.completed is False:
            # return "-"
            # return f"Task: {self.title} - Due Date: {self.due_date} - Completed: [-]" # This works equally, but it's my design
            # return f"[-] Task: {self.title} - Due Date: {self.due_date}." # This works equally, but it's my design
            return f"[-] Task: {self.title} (due {self.due_date})"
        elif self.completed is True:
            # return "x"  
            # return f"Task: {self.title} - Due Date: {self.due_date} - Completed: [x]"  # This works equally, but it's my design
            return f"[X] Task: {self.title}  (due {self.due_date})"

if __name__ == "__main__":
    print("============================= Personal To-Do List Manager ============================== \n")
    task_1 = Task("'ALAB 356.4 - Generators, Closures, and Utility Methods'", "2026-11-20", True)
    task_2 = Task("'SBA 356 - Python Essentials 2'", "2026-11-20", False)
    task_3 = Task("'KBA 356 - Python Essentials 2'", "2026-11-20", False)
    task_4 = Task("'End of Course Survey'", "2026-11-20", False)
    task_5 = Task("'End of Course Survey'", "2026-11-20")
    task_6 = Task("'End of Course Survey'") # Interesting, returns "[-] Task: 'End of Course Survey' (due None)"
    print(task_1)
    print(task_2)
    print(task_3)
    print(task_4)
    print(task_5)
    print(task_6)






# //////////////////////////////////////// SIde Notes: //////////////////////////////////////////////



 

# =============== Pending Improvement to be applied NEXT 10-24-26 according to chatgpt: ============================ 

'''     
What you've done correctly
- Class and initializer: Task and __init__() are correctly defined.
- Instance attributes: self.title, self.due_date, and self.completed are set correctly.
- Multiple objects: You created four tasks with different titles and completion statuses.
- Conditional logic: Your if/elif checks correctly distinguish completed from incomplete tasks.
- Needed fix, format returns to SBA requirement:
FROM:
Task: Last date to submit 'ALAB 356.4 - Generators, Closures, and Utility Methods' - Due Date: 2026-11-20 - Completed: [x]
Task: Last date to submit 'SBA 356 - Python Essentials 2' - Due Date: 2026-11-20 - Completed: [-]
...
TO:
[X] Task: 'ALAB 356.4 - Generators, Closures, and Utility Methods'  (due 2026-11-20)
[-] Task: 'SBA 356 - Python Essentials 2' (due 2026-11-20)
...

- AI answer to Task 1:
One improvement to your __str__() method
Your current method returns something like:
- Task: Last date to submit 'SBA 356 - Python Essentials 2' - Due Date: 2026-11-20 - Completed: [-]
- That works, but the SBA's example uses the completion marker at the beginning of the string:
[-] Submit assignment (due 2025-03-10)
- You can simplify your method using a conditional expression:
%
def __str__(self):
    status = "[X]" if self.completed else "[-]"

    if self.due_date is not None:
        return f"{status} {self.title} (due {self.due_date})"

    return f"{status} {self.title}"

Notice that you don't need elif here because there are only two possible Boolean states: True and False.

One thing to keep in mind
Your initializer allows:
%
due_date=None

...But your current __str__() always displays self.due_date.For example:
%
task3 = Task("Study Python")print(task3)

Your current output would be:
[-] Task: Study Python - Due Date: None

- One important distinction: You've tested the Task class by creating objects directly, which is great. Later, Task 2 will 
introduce functions that create and manage tasks for the user.

Other Observations from GPT:
1. Match the spec's format and handle due_date=None.
The spec's example is "[-] Submit assignment (due 2025-03-10)", with no Task: prefix. Your (due None) output (task_6) is also a
bit ugly. Since the class accepts either a datetime.date or a string, a simpler __str__ can cover both cases:
%
class Task:
    """Represents a single to-do item."""

    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date      # datetime.date, string, or None
        self.completed = completed

    def __str__(self):
        status = "[X]" if self.completed else "[-]"
        due = f" (due {self.due_date})" if self.due_date else ""
        return f"{status} {self.title}{due}"
    Small notes on the changes:

...if self.completed is False / elif ... is True can be one conditional expression. Comparing booleans with is True also isn't idiomatic.
Your two-branch version has no fallback return. It works only because completed is always a bool, but a conditional expression avoids the gap.
Note that "[X]" appears for completed tasks, matching the spec.

2. Put the test code behind a guard.
Your print(...) and task_1 = ... lines run every time task.py is imported. Once main.py does from task import Task, your banner 
and test output would print on every launch. Wrap them like this:
%
if __name__ == "__main__":
    print("===== Personal To-Do List Manager =====\n")
    print(Task("Submit assignment", "2026-11-20"))
    print(Task("Finished item", "2026-11-20", True))
    print(Task("No due date"))

3. Keep the titles clean.
You're embedding quotes inside the titles ("'SBA 356 - Python Essentials 2'"). That will carry through to the file saving in 
Task 4 and look odd. Plain titles are safer, especially because a CSV save will add its own quoting if a title contains a comma.

A heads-up for Task 2: list_tasks has to check overdue status by comparing against today's date, so it will need due_date to be
a real datetime.date rather than a string. Your add_task will do the parsing with datetime.strptime(...).date(), which means 
Task will mostly receive date objects. The __str__ above handles that fine, since an f-string prints a date as 2026-11-20.

Addt'l Observation:
Handle due_date=None in __str__. You noticed that task_6 prints (due None). That's a good catch, and it's worth fixing now. 
A cleaner output omits the due clause entirely when there's no date.
'''


