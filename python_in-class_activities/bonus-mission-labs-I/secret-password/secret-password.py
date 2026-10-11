
r'''
#
The "Secret Password" Sentinel (While Loops & Logic):
Goal: Use a while loop to keep a program running until a specific logical condition is met.
Your Mission:
Write a program that continuously asks the user to input a password.
The loop should only stop if the user types "python123" OR if they have guessed incorrectly 3 times (intruder alert!).
If they get it right, print: "Access granted."
If they run out of attempts, print: "Account locked. Try again later."

Hint: You will need to track two things: the user's current guess and a counter variable that starts at 0 and goes up by 1 every time they guess wrong. Use the and or or logical operators to combine your loop conditions.
'''

r''' 
# Attempt 1 - Works w/ many bugs:
password = input("enter password: ")

count = 0

while count < 3:
    # password = input("enter password: ")
    if password == "hello":
        print("Access granted!")
    else:
        print("Try again!")
    count += 1
# Bugs:
# - whether user guesses correctly or not, the application exits out immediately.
# - whether user guesses correctly or not, the appropriate message gets printed multiple times (itc 3x).
'''

r'''
# Attempt 2 - Semi-Succesful - it works but w/out a while loop, consequently it only gives user 1 try before it exits. You want
# to allow 3 guesses before it exits out.
password = input("enter password: ")

if password == "hello":
        print("Access granted!")
else:
        print("Please, try again!")
# Bug:
#- whether user guesses correctly or not, the application exits out immediately.
'''

r''' 
# Attempt 3 - Works but w/ bugs:
pwd_entered = input("enter password: ")

count = 0
password = 'hello'

while count < 3:
    if pwd_entered == password:
        print("Access granted!!")
        break
        #count += 1
    else:
        print("Account locked. Try again later!")
        count += 1
    #count += 1
#count += 1

[Returns...
"psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials
$ C:/Users/psrga/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/psrga/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/python_in-class_activities/bonus-mission-labs/secret-password/secret-password.py"
enter password: hello
Access granted!!

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials
$ C:/Users/psrga/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/psrga/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/python_in-class_activities/bonus-mission-labs/secret-password/secret-password.py"
enter password: hi
Account locked. Try again later!
Account locked. Try again later!
Account locked. Try again later!""]

"The main problem is that you ask for the password only once, before the while loop starts. If the user enters the wrong password,
the loop repeats, but it keeps checking the same incorrect password instead of asking for another attempt.
Also, your message says "Account locked. Try again later!" after every incorrect attempt, even though you intend to allow three 
attempts."
'''

r''' 
# Attempt 4 - Works but w/ bugs - it ignores the limit of 3 attempts and never reaches the "Account locked..." message:
count = 0
password = 'hello'

while count < 3:
    pwd_entered = input("enter password: ")
    if pwd_entered == password:
        print("Access granted!!")
        break
        #count += 1
    # elif count != 0:
    elif pwd_entered != password:
        print("Try again!")
        #count += 1
    else:
        print("Account locked. Try again later.")
        #count += 1
    #count += 1
#count += 1
'''

#r''' 
# Attempt 5 - works with bug, at the last try it not only prints ""Account locked..." but also "Try again!" :
count = 0
password = 'hello'

while count < 3:
    pwd_entered = input("enter password: ")

    if pwd_entered == password:
        print("Access granted!!")
        break
        #count += 1
    # elif count != 0:
    elif pwd_entered != password:
        print("Try again!")

    count += 1

    if count == 3:
        print("Account locked. Try again later.")

#if count == 3:
    #print("Account locked. Try again later.")

# This was teh best I could do to get it to work. "Try again!" still shows even on teh 3rd attempt when the account locked 
#'''



