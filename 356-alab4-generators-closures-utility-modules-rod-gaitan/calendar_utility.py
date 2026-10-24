'''
Task 4: Date and Calendar Utility
Write a Python script (e.g., calendar_utility.py) that:
    - Prompts the user for a year and a month (e.g., 2025 and 3 for March 2025) ...{DONE} 
    - Uses the calendar module to display the calendar for that month in a neatly formatted grid ...{DONE} 
    - Uses the datetime module to determine today's date.
    - If today's date falls in the specified month and year, prints a message indicating so (e.g., “Today is March 4, 2025”) or highlights the day in the output.
    - Clearly labels all outputs for readability.
'''

import calendar # importing the 'calendar' module to help display the calendar
import datetime # importing the 'datetime' to determine today's date.

today = datetime.date.today()
 
# print(dir(calendar)) # allows me to see all the tools in the 'calendar' toolbox

try: 
    print("See a calendar month for a year of choice!")
    year = int(input("Enter the year: ")) # takes in year input from user.
    month = int(input("Enter the month (1-12): ")) # takes in month input from user.
    print()
    print("===== Calendar =====")
    print(calendar.month(year, month)) # calls the 'month(year, month)' function from the 'calendar' module with 2 separate 
                                    # values/arguments of 'year' and 'month' to import the calendar for the month & year specified.

    if month == today.month and year == today.year:
        # print(f"Today falls inside the month and year entered. Today is {today.month} {today.day}, {today.year}")
        print(f"Today falls inside the month and year entered. Today is {calendar.month_name[today.month]} {today.day}, {today.year}")
    else:
        print("Today's date DOES NOT fall inside the month and year entered!")

except ValueError: # a 'try/catch block' ('try/except block') to ensure the correct data type input is entered, since a 
                    # deliberate 'int()' was done to cast any string input obtained via the 'input()' function.
                    # this covers both issues 1) invalid data 2) "calendar.IllegalMonthError" if some enters value > 12 for 'month'.
    print("Invalid input. Enter the year as a number and the month as a number from 1 to 12!")

print() # space
# print(dir(datetime)) # allows me to see all the tools in the 'datetime' toolbox
# print(datetime) # Returns: <module 'datetime' from 'C:\\Users\\psrga\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\datetime.py'>
# print(datetime.date()) # Returns: TypeError: function missing required argument 'year' (pos 1)
# print(datetime.date)  # Retruns: <class 'datetime.date'>
# print(dir(datetime.date)) # allows me to see all the tools in the 'datetime.date' toolbox
## print("Today's date is: ", end=" ") # Returns: Today's date is:  2026-10-23
## print(datetime.date.today()) # Finally, this gives me today's date. Returns: Today's date is:  2026-10-23
# print(f"Today is {datetime.date.month()}, {datetime.date.day()}, {datetime.date.year()}") # Returns: objects not callable. 
# print(f"Today is {datetime.date.month}, {datetime.date.day}, {datetime.date.year}") # Returns: "Today is <attribute 'month' of 'datetime.date' objects>, <attribute 'day' of 'datetime.date' objects>, <attribute 'year' of 'datetime.date' objects>"
## today = datetime.date.today() moved this to the top of script (NOT inside try/except block)
## print(today) # Returns: 2026-10-23
## print(today.month) # Returns: 10
## print(today.day) # Returns: 23
## print(today.year) # Returns: 2026

# if today.month == month and today.month == month 
# if month in today.month and year in today.year 
# if month in today and year in today: # TypeError: argument of type 'datetime.date' is not a container or iterable

r''' 
# Placing conditional block inside the Try/Catch block
if month == today.month and year == today.year:
    # print(f"Today falls inside the month and year entered. Today is {today.month} {today.day}, {today.year}")
    print(f"Today falls inside the month and year entered. Today is {calendar.month_name[today.month]} {today.day}, {today.year}")
else:
    print("Today's date DOES NOT fall inside the month and year entered!")
'''

# ///////////////////////////////////// PENDING Optional: ///////////////////////////////////////
''' 
Unusual years. Entering something like -5 won't crash, but it prints a meaningless calendar. If you want to be thorough, add a 
check like year >= 1. It's optional.
'''

# ///////////////////////////////////// Side Notes ///////////////////////////////////////////////

'''
File name. Save the script as calendar_utility.py, as the lab specifies. Never name it calendar.py, because Python would import 
your file instead of the real calendar module and break everything.
'''

r'''
- So initially, when entering a month a text, the script crashed and gave:
%
Traceback (most recent call last):
  File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\356-alab4-generators-closures-utility-modules-rod-gaitan\calendar_utility.py", line 52, in <module>
    if month == today.month and year == today.year:
       ^^^^^
NameError: name 'month' is not defined
- so the fix was to encapsulate the following conditional block within the try/except (try/catch) block:
%
    if month == today.month and year == today.year:
        # print(f"Today falls inside the month and year entered. Today is {today.month} {today.day}, {today.year}")
        print(f"Today falls inside the month and year entered. Today is {calendar.month_name[today.month]} {today.day}, {today.year}")
    else:
        print("Today's date DOES NOT fall inside the month and year entered!")

Q:
- So my question became, why not also do a try/except specifically for the 'NameError' exception generated?
A:
You could, and it would work, but it’s the weaker choice. There are two reasons.
1. NameError is a symptom, not the real problem. The real problem is that the user typed bad input, and your except ValueError 
already handles that. If the if check sat after the try/except and you caught NameError there, you’d be catching the side effect 
of a failed input instead of the failure itself. The code would be harder to follow, because a reader would wonder why a name 
might not exist.
2. NameError usually means a bug in your own code. It’s what Python raises for a typo like yeer or a variable used before it 
was defined. It falls into the same trap as a bare except:: if you catch it, a real typo later in the script gets silently 
reported as “bad input,” and you lose the traceback that would have shown you the mistake.
The better approach is to structure the code so the problem can’t happen. You have 2 clean options:
- Option A: put the check inside the try (what I suggested)
- Option B: use the else clause you saw earlier. It runs only if the try succeeded, so year and month are guaranteed to exist:
try:
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    calendar_text = calendar.month(year, month)
except ValueError:
    print("Invalid input. Enter the year as a number and the month as a number from 1 to 12.")
else:
    print("===== Calendar =====")
    print(calendar_text)

    today = datetime.date.today()
    if today.year == year and today.month == month:
        print(f"Today is {calendar.month_name[today.month]} {today.day}, {today.year}")
    else:
        print("Today's date is not in the month you selected.")

- The general rule is to catch the exceptions you expect from user input or the outside world (ValueError, FileNotFoundError), 
and fix NameError-type problems by correcting the code, not by catching them.
'''

'''
month_name is a built-in sequence inside the calendar module that holds the full names of the months. It behaves like a list,
so you look up a name by putting the month number in square brackets:
%
import calendar

print(calendar.month_name[3])    # March
print(calendar.month_name[10])   # October
'''

''' 
#
<< print(dir(datetime)) >> :
['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
'__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

#
<< print(dir(datetime.date)) >> :
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', 
'__reduce__', '__reduce_ex__', '__replace__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', 
'__subclasshook__', 'ctime', 'day', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'isocalendar', 
'isoformat', 'isoweekday', 'max', 'min', 'month', 'replace', 'resolution', 'strftime', 'strptime', 'timetuple', 'today', 
'toordinal', 'weekday', 'year']
'''