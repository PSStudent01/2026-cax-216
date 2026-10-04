
r'''
#
print("My name is", "Python.", end=" ") # 'end=" "' will PULL the line below up into the end of the line above.
print("Monty Python.")

#
print("My name is ", end="") # no space in the string value. Will PULL the line below up into the end of the line above.
print("Monty Python.")

#
print("My", "name", "is", "Monty", "Python.", sep="-") # 'sep=' is keyword argument for the print() function that controls what gets inserted

#
print("My", "name", "is", sep="_", end="*") # you can combine both keyword arguments
print("Monty", "Python.", sep="*", end="*\n")

# 2.1.12   LAB   The print() function and its arguments
print("Programming","Essentials","in", sep="***", end="...")
print("Python")
# Programming***Essentials***in...Python

# 2.1.15 SECTION QUIZ

# 1) What is the output of the following program?
print("My\nname\nis\nBond.", end=" ")
print("James Bond.") 

# 2) What is the output of the following program?
# print(sep="&", "fish", "chips")  # returns error "SyntaxError: positional argument follows keyword argument"
                                    # Remember: Keyword arguments should be passed after any required positional arguments.

# 3) Which of the following print() function invocations will cause a SyntaxError?
print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.") 
# print('"Greg's book."') # this 'print()' function invocation will cause a SyntaxError

#
print(11,111,111) # Python treats them as three separate arguments being passed to print()
#print(11.111.111) # python will throw back an error
print(11_111_111) # python will treat as literal interger

#
print(0o123) # returns 83

#
print(6.62607E-34) # returns 6.62607e-34

#
print(0.0000000000000000000001) # returns 1e-22

#
# print(I like "Monty Python") # returns error: SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("I like 'Monty Python'") # returns... I like 'Monty Python'
print("I like \"Monty Python\"") # returns... I like "Monty Python"
print("I like \"Monty Python\"") # returns... I like "Monty Python"
print('I like "Monty Python"') # returns... I like "Monty Python"

#
print('I\'m Monty Python')
print("I'm Monty Python.")

#
print(True > False) # returns... True, bc True = 1 and False = 0, and since 1 > 0, this returns True
print(True < False) # returns... False, bc True = 1 and False = 0, and since 1 > 0, this returns False
'''

r'''
# 2.2.6   LAB   Python literals - strings

Expected Output:
#"I'm"
#""learning""
#"""Python""" 

print("I'm learning Python") # Returns... I'm learning Python
print(' "I\'m" ""learning"" """Python""" ') # Returns... "I'm" ""learning"" """Python""" 
print()
print(' "I\'m"\n ""learning""\n """Python""" ') 
# returns...   
# "I'm"
#""learning""
# """Python""
'''

r'''
#
print()
print(2 ** 3)  # Returns... 8
print(2 ** 3.) # Returns... 8.0 , but I thought this would return an error
print(2. ** 3) # Returns... 8.0 , but I thought this would return an error 
print(2. ** 3.) # Returns... 8.0 , but I thought this would return an error 

#
print()
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
# Note: The result produced by the division operator is ALWAYS a float, regardless.

# If you absolutely want an integer result from 2 whole integers, Python provides an option, the 'floor division (//)':
print(6 // 3)  # returns 2  # <------{*}
print(6 // 3.)  # returns 2.0
print(6. // 3)  # returns 2.0
print(6. // 3.)  # returns 2.0
# VIP: Please note it not only gives a whole number result, but ROUNDS OFF to the bottom number, for example, 6/4 should give you 1.5. However...
print()
print(6 / 4)
print(6 // 4)  # returns 1
print(6. // 4)  # returns 1.0
# Note: This is very important: when dealing with POSITIVE numbers, the rounding always goes to the LESSER integer.
print()
print(-6 // 4)  # returns 2
print(6. // -4)  # returns 2.0
# Note: This is very important: when dealing with NEGATIVE numbers, the rounding always goes to the GREATER integer.

print()
print(14 % 4) # returns 2, which is the remainder/modulo of this opeartion

print()
print(12 % 4.5)  # returns 3.0

print()
print(-4 + 4)  # returns 0
print(-4. + 8)  # returns 4.0

print()
print(-4 - 4) # return -8, is an example of binary operation
print(4. - 8) # return -4.0, is an example of binary operation
print(-1.1) # return -1.1, is an example of unary operation

print()
print(9 % 6 % 2) 

print()
print(2 * 3 % 5) # 2 * 3, / 5 = 1
# Note: Both operators (* and %) have the same priority, so the result can be guessed only when you know the binding direction

# illustrating order of operations:
print()
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))

#
print()
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

#
print()
var = "3.14.7"
print("Python version: " + var) 

#
print()
var = 1
print(var)
var = var + 1
print(var)

# illustrating re-assignment of a variable
print()
var = 100
var = 200 + 300 # the new sum value of '500' REPLACES the existing value of '100' that was stored in 'var' just a few secs ago.
print(var) 
# notice, a re-assignmet took place here bc 'var = var + 200 + 300' was what was needed to keep track of var. For example:
print()
var = 100
var = var + 200 + 300 #the new sum value of '500' REPLACES the existing value of '100' that was stored in 'var' just a few secs ago.
print(var)

print()
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)


#  how shortcut operators work:
# WRONG WAY - this instead illustrates re-assignment:
x = 10
sheep = 2

print()
x = x * 2
print(x) # returns... 20
x *= 2
print(x) # returns... 40

print()
sheep = sheep + 1
print(sheep) # returns... 3
sheep += 1 
print(sheep) # returns... 4

# RIGHT WAY
x = 10
y = 10
sheep = 2
sheep_2 = 2

print()
x = x * 2
print(x)
y *= 2
print(y)

print()
sheep = sheep + 1
print(sheep)
sheep_2 += 1 
print(sheep_2)

print()
a = 6
b = 3
#a = a / 2 * b  returns... 9.0  <---{incorrect}
#a = a / (2 * b)  returns... 1.0  <---{correct}
a /= 2 * b  # returns... 1.0  <---{correct}



#commenting out the whole thinhg cz causing error
#print()
#anything = input("Enter a number: ")
#something = anything ** 2.0
#print(anything, "to the power of 2 is", something)
#Returns... 
#Traceback (most recent call last):
  #File "c:\Users\psrga\Desktop\Per Scholas Python Essentials\2026 Python Essentials\2026-cax-216\python_in-class_activities\compliment_notes_netacad\code_practice_netacad.py", line 229, in <module>
    #something = anything ** 2.0
#TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
#Fix...
#The fix: convert anything to a number before using it in a math operation
#anything = float(anything)  
#something = anything ** 2.0 

print()
# using variable 'hypo' to store the logic that acts on the input to calculate output
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

print()
# same code as above but rather than using variable 'hypo' to store the logic, we insert the logic as an argument into teh print() function directly
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

print()
# when using + sign to be a concatenator, not an adder, you must ensure that both its arguments are strings.
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# VIP This simple program "draws" a rectangle, making use of an old operator (+) in a new role:
print()
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
# Try practicing to create other shapes or your own artwork!!!!!!

#
print()
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
# note, with 'str()' we can pass the whole result to the print() function as one string, forgetting about the commas.

'''

r'''
############################## 3.1 Section 1 – Making decisions in Python ####################
# comaprison using teh '==' operator
var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

# comaprison using teh '!=' operator
var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)

# If you want to know if there are more black sheep than white ones, you can write it as follows:
black_sheep = 5
white_sheep = 3
print(black_sheep > white_sheep)  # based on the initialized variables, this boolean statement is True

# If we want to find out whether or not we have to wear a warm hat, we ask the following question:
centigrade_outside = 10.0

if centigrade_outside >= 0.0:  # Greater than or equal to
  print("Good weather to be outside!")
'''

#
'''
current_velocity_mph < 85  # Less than is an example of a STRICT sibling
current_velocity_mph <= 85  # Less than or equal to is an example of a NON-STRICT sibling
'''

r'''
# 3.1.6   LAB   Variables ‒ Questions and answers

Scenario
Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.
Don't create any if blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.

#
n = 100 # if n = 100...
print(n <= 55) # then 'n <= 55' is False
#
n = 100
print(n <= 99)
#
n = 100
print(n <= 100)
#
n = 100
print(n <= 101)
#
n = 100
print(n <= -5)
#
n = 100
print(n <= 123)

- As you can see, making a bed, taking a shower and falling asleep and dreaming are all executed CONDITIONALLY – when 
'sheep_counter' reaches the desired limit. Feeding the sheepdogs, however, is always done (i.e., the feed_the_sheepdogs() 
function is NOT indented and DOES NOT belong to the if block, which means it is always executed.)

print()
n = 11
if n == 11:
  print("hi") # this statement is inside the condition, thus gets executed ONLY if the condition is met!
  print("this is the correct number")  # this statement is inside the condition, thus gets executed ONLY if the condition is met!
  print("you guessed correctly") # this statement is inside the condition, thus gets executed ONLY if the condition is met!
  print(f"you get a {n} for guessing correctly!") # this statement is inside the condition, thus gets executed ONLY if the condition is met!
print("play again!") # this statement is outside the condition, bc is not indented, thus it's always executed, regardless of 
                     # whether the number  was guessed correctly or not, meaning it does not belong to the if block, which 
                     # means it is always executed, regardless of what the conditianal statement returns
'''


'''
Now we know what we'll do if the conditions are met, and we know what we'll do if not everything goes our way. In other words, 
we have a "Plan B". ITC 'else' this would be Plan B
'''

r'''
#"Nested if-else statements"
Plans for Sunday:
If the weather is fine, we'll go for a walk. If we find a nice restaurant, we'll have lunch there. Otherwise, we'll eat a
sandwich. If the weather is poor, we'll go to the theater. If there are no tickets, we'll go shopping in the nearest mall.
%
if the_weather_is_good:               # if 'the_weather_is_good' is True, do as follows:
                                  # go_for_a_walk() # then 1) run function 'go_for_a_walk()' <-----{AI said this line missing from author example.}
    if nice_restaurant_is_found:      # 2) AND IF 'nice_restaurant_is_found' is True.
        have_lunch()                  # then run function 'have_lunch()'
    else:                             # otherwise if 'nice_restaurant_is_found'is False...
        eat_a_sandwich()              # then run function 'eat_a_sandwich()'
else:                                 # otherwise if function 'the_weather_is_good' is False, do If logic as follows:
    if tickets_are_available:         # IF 'tickets_are_available' is True
        go_to_the_theater()           # then run function 'go_to_the_theater()'
    else:                             # otherwise If 'tickets_are_available' is False...
        go_shopping()                 # # then run function 'go_shopping()'

Side notes:
-  Ureka: 
-- 'nested if-else statements' are connected by 'AND IF'
-- 'nested if-else statements' is like saying "IF something is True run next If, AND IF that If is also True run next If, and so on.
'''

r'''
- elif is used to check more than just one condition, and to stop when the first statement which is true is found.
- Our next example resembles nesting, but the similarities are very slight. Again, we'll change our plans and express them as follows: If the weather is fine, we'll go for a walk, otherwise if we get tickets, we'll go to the theater, otherwise if there are free tables at the restaurant, we'll go for lunch; if all else fails, we'll stay home and play chess.
- Let's write the same scenario using Python:
%
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()
'''

r'''
Q:
- Using the above 2 examples as reference, in general is it safe to say that: code # 1 is like chaining if statements, like saying if something is true AND if something is true, so on  where all conditions must be True in order for code to run...  whereas code #2 like saying if something is true OR something id true, OR something is true, and so on where at least 1 condition must be True in order for code to run? 
A:
- Where your instinct isn't wrong: if you strip away the else branches, nesting starts to resemble AND:
%
if condition_a:
    if condition_b:
        do_something()
# no else anywhere — if either is False, nothing happens at all

- Where your instinct isn't wrong: if all the branches in an elif chain do the exact same action, it starts to resemble OR:
%
if condition_a:
    do_something()
elif condition_b:
    do_something()
elif condition_c:
    do_something()
# no else anywhere — something will happens if any is True. IOWs, at least one must be True for something to run
'''

r'''
# 3.1.8 Analyzing code samples
# All the programs solve the same problem – they find the largest of several numbers and print it out:

# Example 1:
# We'll start with the simplest case – how to identify the larger of two numbers:

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

print("The larger number is:", larger_number)
# Ureka moment: here we create a variable to serve as storage for the result value of that statement that is True, so that we
can create a print() statement outside of the if, elif, else branches.
'''

r'''
# Example 2:
# Now we're going to show you one intriguing fact. Python has an interesting feature – look at the code below:

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1  # here the action code is placed next to the if statement after the ':'
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)
'''

r'''
# Example 3:
# It's time to complicate the code – let's find the largest of three numbers. Will it enlarge the code? A bit.
# We assume that the first value is the largest. Then we verify this hypothesis with the two remaining values.

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)
'''
#/////////////////////////////////////////////////////////////////
# My Personal Attempts to the above exercises:
r'''
# My example 1: to 'find the largest of several numbers and print it out'
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
  print(f"{num1} is the greater number of the two numbers.")
else:
  print(f"{num2} is the greater number of the two numbers.")

[ It worked Returns...
Enter first number: 3
Enter second number: 1
3 is the greater number of the two.]
'''

r'''
# My example 1b: to 'find the largest of several numbers and print it out'
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
  larger_number = num1
else:
  larger_number = num2

print(f"{larger_number} is the greater number of the two numbers.")

[ It worked Returns...
Enter first number: 3
Enter second number: 1
3 is the greater number of the two.]
'''

r'''
# My example 3: to 'find the largest of 3 numbers and print it out'
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: ")) 

if num1 > num2 and num1 > num3:
  largest_num = num1
elif num2 > num1 and num2 > num3:
  largest_num = num2
else:
  largest_num = num3

print(f"{largest_num} is the greater number of the three numbers.")
'''

r'''
##### WRONG APPROACH
number1 = 30
number2 = 45
number3 = 60
number4 = 13

largest_number = number1  # assumes so far that number1 is the largest
if number2 > largest_number: # if conditional statemet is True...
    largest_number = number2 # then reassign value of number2 to largest_number, stop the conditional statement and jump to print
elif number3 > largest_number: # elif 'number2 > largest_number:' is False, the evaluate this line and if True...
    largest_number = number3 # then reassign value of number3 to largest_number, stop the conditional statement and jump to print
elif number4 > largest_number: # elif 'number3 > largest_number' is False, the evaluate this line and if True...
    largest_number = number4  # then reassign value of number4 to largest_number, stop the conditional statement and jump to print

print(largest_number)
[Returns 45...
- syntax good
- logic fails!!]
'''

r'''
##### RIGHT APPROACH - replace the elif with if statements
number1 = 30
number2 = 45
number3 = 60
number4 = 13

largest_number = number3  # assumes so far that number3 is the largest
if number2 > largest_number:  # check number2 independently
    largest_number = number2  # update if number2 is bigger
if number3 > largest_number:  # check number3 independently — always runs, regardless of the check above
    largest_number = number3  # update if number3 is bigger
if number4 > largest_number:  # check number4 independently — always runs, regardless of the checks above
    largest_number = number4  # update if number4 is bigger

print(largest_number)

#[Returns 60...
#- syntax good
#- logic good!!]


# - This method is significantly simpler than trying to find the largest number all at once, by comparing all possible pairs of 
# numbers (i.e., first with second, second with third, third with first). Try to rebuild the code for yourself.

# - Note: number1 is just an arbitrary number and isn't special in any mathematical sense. It's just the most convenient 
# starting point. You could start from any of them — it'd work identically
'''

'''
# In this case, we'll use a kind of notation which is not an actual programming language (it can be neither compiled nor executed), but it is formalized, concise and readable. It's called pseudocode.
# Let's look at our pseudocode below:

largest_number = -999999999
number = int(input())
# number = int(input("enter number: "))
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
    # print(largest_number)

# Lines 02 through 08 make a loop. We'll pass through them as many times as needed to review all the entered values.
# Can you use a similar structure in a program written in Python? Yes, you can

Q:
- so am i right to assume that the above code is the long way of creating a while loop?
A:
Your assessment is right in spirit, but there's a distinction worth tightening up.
What's correct
You're right that this structure — code that says "go back to an earlier line and repeat" — is exactly the behavior a while loop gives you. The intuition that this is "doing loop-like things the long way" is accurate.
What's slightly off
The pseudocode as written isn't actually a working loop on its own — it's a description of loop-like behavior, written using a comment (# Go to line 02) that Python (or any real language) can't execute. # Go to line 02 is just a comment; Python ignores comments entirely at runtime. If you ran this code exactly as-is, it would execute top to bottom exactly once and then simply end — no repetition would actually happen, because nothing in real Python syntax makes it jump backward.
So it's less "the long way of writing a while loop" and more "pseudocode that describes what a while loop needs to accomplish, using a jump instruction (goto) that doesn't exist in Python."
'''

r'''
# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.
largest_number = max(number1, number2, number3)

# Check which one of the numbers is the lowest # <--- perosnally added for practice purposes
# and pass it to the lowest_number variable.  # <--- perosnally added for practice purposes
lowest_number = min(number1, number2, number3)  # <--- perosnally added for practice purposes

# Print the result.
print("The largest number is:", largest_number)
print("The lowest number is:", lowest_number)  # <--- perosnally added for practice purposes
'''

r''' 
# 3.1.10 LAB Comparison operators and conditional execution
Scenario
Spathiphyllum, more commonly known as a peace lily or white sail plant, is one of the most popular indoor houseplants that filters out harmful toxins from the air. Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.
Imagine that your computer program loves these plants. Whenever it receives an input in the form of the word Spathiphyllum, it involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"
- Write a program that utilizes the concept of conditional execution, takes a string as input, and:
    prints the sentence "Yes - Spathiphyllum is the best 
    plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
    prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
    prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!


plant_input = input("Enter plant name: ")

if plant_input == "Spathiphyllum":
    message = "Yes - Spathiphyllum is the best plant ever!"
    print(message)
elif plant_input == "spathiphyllum":
    message = "No, I want a big Spathiphyllum!"
    print(message)
else:
    print(f"Spathiphyllum! Not {plant_input}!")
'''

'''
# 3.1.11 LAB Essentials of the if-else statement ---- VIP VIP VIP VIP 
Scenario
Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
    if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
    if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to write a tax calculator.
    It should accept one floating-point value: the income.
    Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you – you'll find it in the skeleton code in the editor.
Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.
Look at the code in the editor – it only reads one input value and outputs a result, so you need to complete it with some smart calculations.
Test your code using the data we've provided.
'''

r'''
# Tax calculator
income = float(input("Enter your yearly income: "))

if income <= 85528.00:
    tax = (.18 * income) - 556.02  # tax relief
    print(f"This is what you owe to the IRS for the 2025-2026 tax cycle: ")
    # print(round(tax, 2)) # 1) comment out to prevent from negative amnt from showing if income produces 0 or less in taxes
    if tax <= 0.00:
       tax = 0.00
       print(f"Good news, you owe {round(tax, 2)} tax at all!")
    print(round(tax, 2)) # 2) ...and placed it here to delimit both parts (ifs) of the logic, not just one.
#elif income > 85528.00: # comment out bc codebase should end with 'else
else:
    tax =  (income - 85528.00) * .32 + 14839.02
    print(f"This is what you owe to the IRS for the 2025-2026 tax cycle: ")
    print(round(tax, 2))

#print(round(tax, 2))
'''

'''
# Author's method of the above - incomplete:
income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Write the rest of your code here.

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
'''

r'''
PENDING TO DO:
3.1.12   LAB   Essentials of the if-elif-else statement
Scenario
As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.
Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
    if the year number isn't divisible by four, it's a common year;
    otherwise, if the year number isn't divisible by 100, it's a leap year;
    otherwise, if the year number isn't divisible by 400, it's a common year;
    otherwise, it's a leap year.
Look at the code in the editor – it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.
The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.
Test your code using the data we've provided.

Per Netacad:
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")
'''

r'''
x = 10

if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.
'''

r''' 
x = 10

if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.
elif x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.
elif x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.
'''

r'''
# Failed 'AND' nested 'If' attempt:
x = 10

if x > 5: # condition one
    print("pass, go to the second If statement!")
else:
    print("condition, fails at first If and therefore the entire expression is False!")
    if x < 10: # condition two
        print("pass, go to the third If step statement!")
    else:
        print("condition, fails at second If and therefore the entire expression is False!")
        if x == 10: # condition three
            print("x fulfills all 3 conditions, therefore the entire expression is True")  # Executed if condition three is True.
        else:
            print("x did not meet any of the 3 conditions above, therefore the entire expression is False")
'''

r'''  
# Successful 'AND' nested 'If' attempt:
x = 6

if x > 5: # condition one
    # print("pass, go to the second If statement!")
    if x > 10: # condition two
        #print("pass, go to the third If step statement!")
        if x == 6: # condition three
            print("x fulfills all 3 conditions, therefore the entire expression is True")  # Executed if condition three is True.
        else:
            print("x did not meet at least one of the conditions above, therefore the entire expression is False")
    else:
        print("condition, fails at second If and therefore the entire expression is False!")
else:
    print("condition, fails at first If and therefore the entire expression is False!")

# ALTERNATIVELY:
x = 6
if x > 5 and x > 10 and  x == 6:
	    print("All passed")
        # print("x fulfills all 3 conditions, therefore the entire expression is True")
else:
    print("At least one failed")
    # print("condition, fails at __________ If and therefore the entire expression is False!")
'''

r''' 
# another perfect example of Nested If statements!
username = input("Enter UN: ")

if username == "Rod":
    password = input("Enter PWD: ")
    if password == "password":
        print("Welcome!")
    else:
        print("invalid password, please try again!")
else:
    print("invalid username, please try again!")
'''
      
r''' 
# another perfect example of Nested If statements leading to further developments
username = input("Enter UN: ")
logged_in = True
shopping_price = [20, 30, 40, 20, 80, 100, 200]

if username == "Rod":
    password = input("Enter PWD: ")
    if password == "password":
        logged_in
        print("Welcome!")
    else:
        print("invalid password, please try again!")
else:
    print("invalid username, please try again!")

if logged_in:
    for i in shopping_price:
        if i < 50:
            print("price is affordable")
        else:
            print("price is expensive")

[Returns...
 Enter UN: Rod
Enter PWD: password
Welcome!
price is affordable
price is affordable
price is affordable
price is affordable
price is expensive
price is expensive
price is expensive
]
'''

r''' 
# Another good example to always keep in mind
x = 10

if x == 10: # True. This condition is OUTSIDE the if-elif-else chain/group below
    print("x == 10") # This gets printed bc condition is True and it's a separate condition

if x > 15:     # False  # 1) part of if-elif-else chain/group
    print("x > 15") # This does NOT get printed bc condition is False and although it's a separate condition, the next elif gets executed

elif x > 10:   # False # This does NOT get printed bc condition is False and the next elif gets executed. 2) part of if-elif-else chain/group
    print("x > 10")

elif x > 11:   # False # This does NOT get printed bc condition is False and the next else gets executed/printed. 3) part of if-elif-else chain/group
    print("x > 5")

else:           # 4) part of if-elif-else chain/group
    print("else will not be executed")
'''

r'''
# Another good example to always keep in mind
x = 10

if x > 5: # True
    if x == 6: # False
        print("nested: x == 6")
    elif x == 10: # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")
# {This illustrates how 'OR', non-nested conditions are listed and 'AND' nested conditions are listed all within one code block}
'''
# - VIP VIP VIP:
# ALWAYS.......ANY TIME you have comparison operators involved, it means you should be expecting a Boolean value, NOT an integer or string value!!!!!

r'''
# Another good example to always keep in mind
x = 10
 
if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else") 
[Returns
True
True
else]
'''

r''' 
# warming up memory miscle while loop:
fruits = ["apple", "banana", "cherry", "mango"]
step = 0

for i in fruits:
    print('fruit present in cart')
    # step = step + 1
    step += 1
'''


# 3.2.3 The while loop: more examples
# # A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered. 
r'''  
# My 1st attempt
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

count = 0

for i in num_list:
    # print(i)
    if i % 2 == 0:
        print (f"the number {i} is even")
    elif i % 2 == 1:
        print (f"the number {i} is odd")
    count += 1
'''
r''' 
# my 1st attempt
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_list = []
odd_list = []

count = 0

for i in num_list:
    # print(i)
    if i % 2 == 0:
        # print (f"the number {i} is even")
        even_list = even_list + i
        print(even_list)
    elif i % 2 == 1:
        # print (f"the number {i} is odd")
        odd_list = odd_list + i
        print(odd_list)
count += 1
'''

r'''  
# my 2nd attempt
num = 20

while num > 0:
    # print("I'm alive")
    if num % 2 == 0:
        print(f"number {num} is even")
        num -= 1
    elif num % 2 == 1:
        print(f"number {num} is odd")
        num -= 1
'''

r''' 
# VIP VIP VIP
# my third attempt...it worked perfectly:
# AI says remove and move the following and also append each number type in each respective list:
num = 20

even_list = []
odd_list = []

while num > 0:
    # print("I'm alive")
    if num % 2 == 0:
        print(f"number {num} is even")
        even_list.append(num) # appending even number to the 'even_list'
        # num -= 1  # <----{remove}
    elif num % 2 == 1:
        print(f"number {num} is odd")
        odd_list.append(num)  # appending odd number to the 'odd_list'
    num -= 1 # <----{move to the outside to line up with 'elif' and 'if'}

print(f"there are a total of {len(even_list)} even numbers")
print(f"there are a total of {len(odd_list)} odd numbers")
'''
r''' 
# VIP VIP VIP
# my fourth attempt...more polished, by replacing the 'elif'statement with the 'else' statement:
num = 20

even_list = []
odd_list = []

while num > 0:
    # print("I'm alive")
    if num % 2 == 0:
        print(f"number {num} is even")
        even_list.append(num) # appending even number to the 'even_list'
        # num -= 1  # <----{remove}
    #elif num % 2 == 1:
    else:  # <---------------------------{replacing the 'elif'statement with the 'else' statement:}
        print(f"number {num} is odd")
        odd_list.append(num)  # appending odd number to the 'odd_list'
    num -= 1 # <----{move to the outside to line up with 'elif' and 'if'}

print(f"there are a total of {len(even_list)} even numbers")
print(f"there are a total of {len(odd_list)} odd numbers")
'''
# VIP VIP VIP
# Netacad's version: Very interesting:
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

r''' 
odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)
# {PENDING: Now that you understand the actual requirements try to this on your own}
'''

''' 
# Side Notes:
- Certain expressions can be simplified without changing the program's behavior.
-Try to recall how Python interprets the truth of a condition, and note that these two forms are equivalent:
while number != 0: and while number:.
- The condition that checks if a number is odd can be coded in these equivalent forms, too:
if number % 2 == 1: and if number % 2:.
'''

r'''  
# Using a counter variable to exit a loop
# This code is intended to print the string "Inside the loop." and the value stored in the counter variable during a given 
# loop exactly five times. Once the condition has not been met (the counter variable has reached 0), the loop is exited, and 
# the message "Outside the loop." as well as the value stored in counter is printed.
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter) 

Q:
- question, could you have used "while  counter > 0" rather than "while counter != 0"?
A:
- Yes — in this specific case, both would work identically and produce the exact same output.
'''

r'''  
# A more compact of the above – by compacting the condition of the while loop:
counter = 5
while counter:  # <----{removed "!= 0:" from the while loop statement}
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)
# REMEMBER  
# Don't feel obliged to code your programs in a way that is always the shortest and the most compact. Readability may be a 
# more important factor. Keep your code ready for a new programmer.
'''

r''' 
# VIP VIP VIP 
# 3.2.4 LAB Guess the secret number
Scenario
A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who runs 
his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the 
number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.
Your task is to help the magician complete the code in the editor in such a way so that the code:
    - will ask the user to enter an integer number;
    - will use a while loop;
    - will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen 
    by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my 
    loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician,
    the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are 
    free now."

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
secret_num = 18
num_guess = int(input("Guess a number: "))

while num_guess != secret_num:
    print("Ha ha! You're stuck in my loop!")
    # break
    num_guess = int(input("Guess a number: ")) # nice, so it looks, like anything other than print() here will break the loop anyway
else:
    print( f"{num_guess} is the correct number. Well done, muggle! You are free now.")
'''

r''' 
# 3.2.5 Looping your code with for
# Imagine that a loop's body needs to be executed exactly one hundred times {for the sake of simplicity, we'll do 10 times only}.
# If you would like to use the while loop to do it, it may look like this:

## Using While Loop:
i = 0
while i < 10:
    print(i)# do_something()
    i += 1
'''

r'''
- Actually, the for loop is designed to do more complicated tasks – it can "browse" large collections of data item by item.
- {Q: so for loop is designed to browse through existing collections of data, whereas while loop is not designed for that}
- - Not quite — your summary slightly overstates it in a way that could trip you up. Let's refine it.
- The issue: saying while is "not designed for that" implies while can't loop through collections at all — but it absolutely can,
 it's just not its specialty/strength.

## Using For Loop:
for i in range(10):
     # do_something()
     print(i) # using instead of 'pass'
     # pass # using instead of ' print(i)'
# Q: what does 'pass' do here?  
# A: In this specific code, pass does absolutely nothing — it's a placeholder statement that tells Python "intentionally 
# leave this blank, don't error out." Why does pass even exist? Python requires every block (loops, functions, if-statements, elif, else
# and while etc.) to have something inside it — you can't leave a block completely empty
'''

r'''  
# modest example to illustrate a simple For Loop:
for i in range(10):
    print("The value of i is currently", i)
# [Returns 0 to 9]
'''

r''' 
# The range() function invocation may be equipped with two arguments, not just one:
for i in range(2, 8):
    print("The value of i is currently", i)
# [Returns 2 to 7]
# In this case, the first argument determines the initial (first) value of the control variable.
# The last argument shows the first value the control variable will not be assigned.
# Note: the range() function accepts only integers as its arguments, and generates sequences of integers.
'''

r'''  
# The range() function may also accept 3 arguments – take a look at the code in the editor:
for i in range(2, 8, 3):
    print("The value of i is currently", i)
# The third argument is an increment – it's a value added to control the variable at every loop turn
# the default value of the increment is 1
# [Returns...
## The value of i is currently 2
## The value of i is currently 5 
## only these 2 numbers are retreived bc (5 increment by 3 equals 8 – the number is not within the range from 2 to 8]
'''    

r'''  
for i in range( ):
    print("The value of i is currently", i)
# - This loop won't execute its body at all, bc zero arguments were passed to it.
'''

r'''  
for i in range(1, 1):
    print("The value of i is currently", i)
# This loop won't execute its body at all, bc the 2nd argument is NOT greater than the 1st argument.
# when the range() function accepts exactly two arguments. This means that the range()'s second argument must ALWAYS be greater
#  than the first.
'''

r'''  
for i in range(2, 1):
    print("The value of i is currently", i)
# This loop won't execute its body at all, bc the 2nd argument is NOT greater than the 1st argument.
# when the range() function accepts exactly two arguments. This means that the range()'s second argument must ALWAYS be greater
#  than the first.
'''

r'''  
# This short program is to write some of the first powers of two:
# My first attempt:
power_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in power_list:
    result = pow(2, i)
    #print(result)
    print(f"the power of 2 to the {i} is {result}")
# It works!!
'''
r'''  
# Author's version:
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2
# this version accounts for 16 numbers rather than 10 as mine
# The expo variable is used as a control variable for the loop, and indicates the current value of the exponent. 
# The exponentiation itself is replaced by multiplying by two. Since 20 is equal to 1, then 2 × 1 is equal to 21, 2 × 21 is 
# equal to 22, and so on. What is the greatest exponent for which our program still prints the result? 
'''

r'''  
# 3.2.7 LAB Essentials of the for loop – counting mississippil
Scenario
Do you know what Mississippi is? Well, it's the name of one of the states and rivers in the United States. The Mississippi River is about 2,340 miles long, which makes it the second longest river in the United States (the longest being the Missouri River). It's so long that a single drop of water needs 90 days to travel its entire length!
The word Mississippi is also used for a slightly different purpose: to count mississippily.
If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.
The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three seconds of time! It's often used by children playing hide-and-seek to make sure the seeker does an honest count.
- Your task is very simple here: write a program that uses a for loop to "count mississippily" to five. Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"
Use the skeleton we've provided in the editor.
EXTRA INFO  
- Note that the code in the editor contains two elements which may not be fully clear to you at this moment: the import time statement, and the sleep() method. We're going to talk about them soon.
For the time being, we'd just like you to know that we've imported the time module and used the sleep() method to suspend the execution of each subsequent print() function inside the for loop for one second, so that the message outputted to the console resembles an actual counting. Don't worry - you'll soon learn more about modules and methods.
%
import time
# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# for i in range(5):
for i in range(1, 6):
    print(f"{i} Mississippi")
    time.sleep(1)
    
# Write a print function with the final message.
print("Ready or not, here I come!")

# it works!!!!
'''

r'''  
# Illustrating 'break':
for i in range(5):
    if i == 2:
        break          # exits the ENTIRE loop immediately when i == 2
    print(i)
# Output: 0, 1  (stops completely, never reaches 3 or 4)
'''

r'''  
# Illustrating 'continue':
for i in range(5):
    if i == 2:
        continue       # skips just THIS iteration's print(i), but loop keeps going
    print(i)
# Output: 0, 1, 3, 4  (skips printing 2, but continues through 3 and 4)
'''

r'''  
# A couple more examples regarding the above:
## Another example to illustrate 'break'
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

## Another example to illustrate 'continue'
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

[Returns...
The break instruction:
Inside the loop. 1
Inside the loop. 2
Outside the loop.

The continue instruction:
Inside the loop. 1
Inside the loop. 2
Inside the loop. 4
Inside the loop. 5
Outside the loop.]
'''


# The 'break' and 'continue' statements: more examples
# Let's return to our program that recognizes the largest among the entered numbers. We'll convert it twice, using the break 
# and continue instructions.
# Illustrating 'break':
r''' 
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:  # fyi, this is not part of a nested If statement! Both are at the same indentation level as the rest of the code directly inside the while loop, meaning they're just two separate, sequential if statements sitting one after another inside the loop
        break
    counter += 1
    if number > largest_number:   # fyi, this is not part of a nested If statement! Both are at the same indentation level as the rest of the code directly inside the while loop, meaning they're just two separate, sequential if statements sitting one after another inside the loop
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")
'''

r'''  
# Illustrating 'continue':
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end the program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")
'''

r'''  
# 3.2.9 LAB The break statement – Stuck in a loop
Scenario
- The break statement is used to exit/terminate a loop.
- Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" 
as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, 
and the loop should terminate.
- Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.


secret_word = "chupacabra"
word = input("Enter a word: ")

while secret_word != word:
    word = input("Try again, please: ")
    if secret_word == word:
        print("You've successfully left the loop")
        break # while the code works w/out the 'break'here, there is a practical reason 'break' is preferred method and it's that 
              # 'while True: + break' is often clearer to read.
'''

r'''  
# My Personal Example
i = 5

while i != 0:
    print('Hello mothafudge!')
    # i -= 1
    break 
# {it executes the action at the 1st iteration and then the break exits the loop. Therefore, this only executes 1 action, which
# is printing the message}
'''

r'''  
# 3.2.10 LAB The continue statement – the Ugly Vowel Eater
Scenario
The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.
It can be used with both the while and for loops.
Your task here is very special: you must design a vowel eater! Write a program that uses:
    - a for loop;
    - the concept of conditional execution (if-elif-else)
    - the continue statement.
Your program must:
    - ask the user to enter a word;
    - use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon – don't worry;
    - use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
    - print the uneaten letters to the screen, each one of them on a separate line.
Test your program with the data we've provided for you.
% 
user_word = input("Enter a word: ")
user_word = user_word.upper()
# print(user_word) # to test

for i in user_word:
    if i == 'A':
        continue
        #print(user_word)
    elif i == 'E':
        continue
        #print(user_word)
    elif i == 'I':
        continue
        #print(user_word)
    elif i == 'O':
        continue
        #print(user_word)
    elif i == 'U':
        continue
        #print(user_word)
    else:
        print(i)  # {the i that 'continue' skips to}
        #print(user_word)
#print(user_word)
# see "VIP Lab for analysis - 3.2.10 LAB.docx"

# My personal attempt of the above using multiple ifs:
#%
user_word = input("Enter a word: ")
user_word = user_word.upper()
# print(user_word) # to test

for i in user_word:
    if i == 'A':
        continue
        #print(user_word)
    if i == 'E':
        continue
        #print(user_word)
    if i == 'I':
        continue
        #print(user_word)
    if i == 'O':
        continue
        #print(user_word)
    if i == 'U':
        continue
        #print(user_word)
    else:
        print(i)   # {the i that 'continue' skips to}
        #print(user_word)
#print(user_word)
# - {it worked equally the same as the example before it.}
# Per AI:
- With elif, only ONE branch in the whole chain can ever execute — Python checks them in order and stops at the first match.
- With separate if statements, Python checks every single one, independently, every time — even after one has already matched.
- so in other words, using mutilple Ifs is more taxing than multiple elifs. [Verified by AI]

# author's version:
user_word = input("Enter a word: ")
user_word = user_word.upper()
# print(user_word) # to test

for letter in user_word:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        print(letter) # {the letter that 'continue' skips to}
'''

r''' 
# 3.2.11 LAB The continue statement – the Pretty Vowel Eater
Scenario
Your task here is even more special than before: you must redesign the (ugly) vowel eater from the previous lab and create a better, upgraded (pretty) vowel eater! Write a program that uses:
    - a for loop;
    - the concept of conditional execution (if-elif-else)
    - the continue statement.

Your program must:
    - ask the user to enter a word;
    - use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon - don't worry;
    - use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
    - assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.

- Look at the code in the editor. We've created word_without_vowels and assigned an empty string to it. Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the word_without_vowels variable.
- Test your program with the data we've provided for you.


# My Personal Attempt:
user_word = input("Enter a word: ")
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
    if letter == 'A':
        continue
        #word_without_vowels = word_without_vowels.append(letter) # Bug 1: .append() doesn't exist for strings — that's a list method.
        #print(word_without_vowels)
    elif letter == 'E':
        continue
        #word_without_vowels = word_without_vowels.append(letter)
        #print(word_without_vowels)
    elif letter == 'I':
        continue
        #word_without_vowels = word_without_vowels.append(letter)
        #print(word_without_vowels)
    elif letter == 'O':
        continue
        #word_without_vowels = word_without_vowels.append(letter)
        #print(word_without_vowels)
    elif letter == 'U':
        continue
        #word_without_vowels = word_without_vowels.append(letter)
        #print(word_without_vowels)
    else:
        pass
        # word_without_vowels = word_without_vowels + letter
        # print(word_without_vowels)
        # word_without_vowels = word_without_vowels.append(letter)
        # print(word_without_vowels)
        word_without_vowels = word_without_vowels + letter # Strings in Python are immutable — you can't modify them in place with something like .append(). Instead, you build a new string using concatenation (+), exactly like this!
         
print(word_without_vowels)  # Bug 2: the print() call is inside the loop, printing after every single letter — but you only need to print once, at the very end.

# It worked perfectly with AI help!!!
'''

r'''
# A) 3.2.12 The while loop and the else branch
- There's something strange at the end – the else keyword.
- As you may have suspected, loops may have the else branch too, like ifs.
- The loop's else branch is always executed once, regardless of whether the loop has entered its body or not

i = 1         # starts counting at count i 1
while i < 5:  # a) for as long as count i is < 5...; b)when condition no longer true (aka false), stop this loop and jump to else and run its action code 
    print(i)  # print count i
    i += 1  # adds 1 to count i at each interval 
else:
    print("else:", i) # c) print the message
'''

r'''   
# B) 3.2.12 The while loop and the else branch
# Modify the above a bit so that the loop itself has no chance to execute its body even once:
# i = 1
i = 5 # making the statement return False is correct way to prevent the code from ever running !!!!!
while i < 5:
    break # this is NOT the correct way. 'break' is not ideal because, although partially, it does allow teh code to start at least on the first loop
    print(i)
    i += 1
else:
    print("else:", i)
#[Returns....else: 5 ] # so the loop is prevented from executing but NOT the 'else' branch as it kicks in when the loop is blocked
'''

r'''  
# 3.2.13 The 'for loop' and the 'else' branch
# - for loops behave a bit differently – take a look at the snippet in the editor and run it.
#%
for i in range(5):
    print(i)
else:
    print("else:", i)
[Returns....
0
1
2
3
4
else: 4 ]  # I thought it would've printed 5
Q:
- why doesn't the following print 5 for the else branch?   
A:
After this last iteration, the for loop tries to grab the next value from range(5) — but there isn't one. The sequence is 
exhausted, so the loop ends naturally (no break involved), and Python runs the else block.
Here's the key part: i still holds whatever value it was last assigned inside the loop — which is 4, not 5. The loop doesn't 
advance i to 5 and then stop; it simply runs out of values to give i after 4, and stops right there.
'''

r'''
- modify the above to illustrate another way of creating an empty range:
%
i = 111
for i in range(2, 1): # means: start at 2, stop before reaching 1 — but since 2 is already greater than 1, there's nowhere to go. This creates an empty range, with zero numbers in it at all.
    print(i)
else:
    print("else:", i)

[Returns... else: 111 ]
Q:
- so it's the  "i = 111" really neaded here?
A:
- in this specific example, no, i = 111 isn't required for the code to run without crashing... but it actually matters quite a bit for what gets printed. Let's check both scenarios.
- Without 'i = 111', this would actually crash with a NameError: name 'i' is not defined — because remember, in Python, a variable only exists once it's been assigned a value at least once (we covered this a while back — assignment is creation). Since the for loop's range is empty, i is never assigned by the loop itself, and if there's no prior i = 111 line to fall back on, there's no i at all anywhere in the program.
'''

r''' 
# PENDING LAB:
3.2.14   LAB   Essentials of the while loop
Scenario
Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
The figure illustrates the rule used by the builders:
{see image of pyramid in notes: height = 3 layers; made up of 6 blocks}

blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	

print("The height of the pyramid:", height)
'''

r''' 
# PENDING LAB:
# 3.2.15 LAB Collatz's hypothesis
Scenario

In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

    take any non-negative and non-zero integer number and name it c0;
    if it's even, evaluate a new c0 as c0 ÷ 2;
    otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
    if c0 ≠ 1, go back to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.
Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.
Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
Hint: the most important part of the problem is how to transform Collatz's idea into a while loop – this is the key to success.
Test your code using the data we've provided.
'''

r'''
SUMMARY: 
a)
- the 'while' loop executes a statement or a set of statements as for long as a specified boolean condition is true - re-checking that condition before every iteration.
- IOWs, The 'while' loop repeats one iteration after another, re-evaluating the boolean condition before each iteration, and continues looping only as long as that condition remains true.
- Examples:
%
 # Example 1
while True:
    print("Stuck in an infinite loop.")
%
# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1 
b)
- the 'for' loop executes a set of statements many times; it's used to iterate over a sequence (e.g., a list, a dictionary, a tuple, or a set ) or other iterable objects (e.g., strings). 
- { IOWs, the 'for' loop executes a set of statement(s)/action(s), for each an every item/component/etc that makes up some existing sequence or iterable object (e.g., string) being evaluated} [AI verified]
- You can use the for loop to iterate over a 'sequence of numbers' using the built-in 'range function. Look at the examples below:
%
# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")
%
# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

c)
-  You can use the break and continue statements to change the flow of a loop:
-- You use break to exit a loop, e.g.:
%
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

- You use continue to skip the current iteration, and continue with the next iteration, e.g.:
%
text = "pyxpyxpyx
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

d)
- The 'while' and 'for' loops can also have an 'else' clause in Python. 
- The 'else' clause executes after the loop finishes its execution as long as it has not been terminated by 'break', e.g.:
%
n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

%
for i in range(0, 3):
    print(i)
else:
    print(i, "else")

e)
The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: range(start, stop, step), where:
- 'start' is an optional parameter specifying the starting number of the sequence (0 by default)
- 'stop' is an optional parameter specifying the end of the sequence generated (it is not included),
- and 'step' is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)
- Examples:
%
for i in range(3):
    # print(i)  # prints vertically
    print(i, end=" ")   # Outputs: 0 1 2. prints horizontally, bc of  end=" " (without separating commas)
%
for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2
for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2
[- all 3 arguments genuinely represent real, actual values that get used to generate the sequence. Let's break down exactly what each one means and trace through why you get 6, 4, 2.
- range(start, stop, step) — here, range(6, 1, -2):
-- start = 6 — the sequence begins at 6
-- stop = 1 — the sequence stops before reaching 1 (never includes 1 itself)
-- step = -2 — instead of the usual +1, this time we're counting downward, by 2 at a time]
'''

r'''  
# 3.2.17 SECTION QUIZ

# Question 1: 
# Create a for loop that counts from 0 to 10, and prints odd numbers to the screen:
## My first attempt - using for loop (as required):
for num in range(10):
    if num % 2 == 1:
        print(num)
    # num += 1  # although does NOT break the code, it is unnecessary as this is for a while loop more so.

# The author's way:
for i in range(0, 11):
    if i % 2 != 0:
        print(i)
[AI Verified]

# Question 2:
# Create a while loop that counts from 0 to 10, and prints odd numbers to the screen:
## My first attempt - using while loop:
num = 0

while num != 10:
    if num  % 2 == 1:
        print(num)
    num += 1
[AI Verified]

# Question 3: 
# Create a program with a 'for loop' and a 'break' statement. The program should iterate over characters in an 'email 
# address', 'exit the loop when' it reaches the '@' symbol, and 'print the part before @' on 'one line':
## First attempt:
email = "rod01@gmail.com"

for i in email:
    print(i, end="")
    if i == '@':
        break

## Second attempt:
email = "rod01@gmail.com"

for i in email:
    if i == '@':
        break
    print(i, end="")

# I believe I had done teh 2nd attempt at first, but it wasnt working , I guess bc I was not using spaces properly, bc it wasnt printing anything
# Ai says "That's a really plausible guess, but indentation issues usually cause an IndentationError"

# Question 4: 
# Create a program with a 'for loop' and a 'continue' statement. The program should iterate over a string of digits, 
# replace each 0 with x, and print the modified string to the screen. Use the skeleton below:

string = "0y0y0y0y0y0y0y0y0y0" # original string
new_string = ""   # variable for modified string

for i in string:
    # if i == 0:  # returning wrong output, bc comaparing to 'int' character, when should be comapring to 'string' character
    if i == "0":   
        new_string = new_string + "x" # adds/concatnates "x" every time iteration encounters "0". IOW, replaces "0" w/ "x"
        continue # jumps any following chracters that are not "0". More precisely, it jumps over lines of code in the current iteration. AI: "skips the rest of this iteration's code (the line below), so this '0' never gets copied — then moves on to check the next character in the string"
        #string = string + "x"
        #string = string.append("x")
        # print("x")
        # print(i)
        #print(string)
        #new_string = new_string + "x"
    new_string = new_string + i # AI: "This line runs for every character that is not "0" (since the if block's continue causes this line to be skipped whenever i is "0"). For any other character, this line takes whatever's already been built up in new_string so far, and appends the current character (i) onto the end of it — unchanged, exactly as it appeared in the original string."
print(new_string) # prints the contents of teh modified string

# Question 5: What is the output of the following code?

n = 3
 
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n) 

[ Retruns....
4
3
2
0]  # why is 0 and not 1 included here?

# Question 6: What is the output of the following code?

n = range(4)
 
for num in n:
    print(num - 1)
else:
    print(num) 
[Returns...
-1
0
1
2
3]   # why is 3 included here?

# Question 7: What is the output of the following code?
for i in range(0, 6, 3):
    print(i)
[Returns...
0
3]  
'''

##################### 3.3 Section 3 – Logic and bit operations in Python #######################

r''' 
# 3.3.2 Logical expressions
# - Let's create a variable named var and assign 1 to it. The following conditions are pairwise equivalent:

# Example 1:
var = 1
print(var > 0)  # {Returns True}
print(not (var <= 0))  # {Returns True}


# Example 2:
print(var != 0)   # {Returns True}
print(not (var == 0))  # {Returns True}
'''

r''' 
You may be familiar with De Morgan's laws. They say that:
The negation of a conjunction is the disjunction of the negations.
The negation of a disjunction is the conjunction of the negations.
Let's write the same thing using Python:

#
p = True
q = False

not (p and q) == (not p) or (not q)
not (T and F) == (not T) or (not F)
T == F or T
T == T

#
p = True
q = False

not (p or q) == (not p) and (not q) 
not (T) == F and T
F == F

[AI: So both of your final answers are correct]

'''
