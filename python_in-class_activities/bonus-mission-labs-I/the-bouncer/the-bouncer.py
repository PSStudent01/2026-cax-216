r'''  
# Challenge: 
The Bouncer (Booleans & Conditionals) 
Goal: Understand how Python uses True and False to make decisions using if, elif, and else.
Your Mission
Write a script for a virtual club bouncer. The program should ask the user for their age.
If they are under 18, print: "Access denied. Too young!"
If they are between 18 and 20 (inclusive), print: "You can come in, but no drinking! 🚫🍷"
If they are 21 or older, print: "Welcome in! Enjoy your night."
- Hint: Remember that the input() function always reads data as a string. You'll need to convert it to an integer using int() 
before doing any math comparisons!
'''
 
age = int(input("Enter your age: "))

if age < 18:
    print("Access denied. Too young!")
elif age >= 18 and age <= 20:
    print("You can come in, but no drinking! 🚫🍷")
else:
    print("Welcome in! Enjoy your night.")


