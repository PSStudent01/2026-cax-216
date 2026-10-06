
# Part 1: Conditional Execution

# Write a script grade_checker.py that:
## Asks the user to input a numeric grade (0-100).
## Uses an if-elif-else structure to convert the numeric grade to a letter grade based on a typical scale:
### 90-100: A
### 80-89: B
### 70-79: C
### 60-69: D
### 0-59: F
## Prints the letter grade. For example: "Your grade is: B"
## Includes a final message using a conditional expression (for example, if the grade is passing (A-C) congratulate the user, if it is a D or F, encourage them to try again).
## Make sure to handle edge cases (like inputting 100 or 0) so that they fall into the correct letter grade. You can assume the user enters a valid number for this task.

score = int(input("Please enter your score(0-100): ")) # asks the user to input a numeric grade (0-100) and casts it to int 
                                                       # data type. Then stores the data into variable 'score'

# if-elif-else structure to convert the score to a letter grade based on a typical scale and render a message depending on grade:
if score <= 100 and score > 89: 
    print("Your grade is: A") 
elif score <= 89 and score > 79:
    print("Your grade is: B")
elif score <= 79 and score > 69:
    print("Your grade is: C") 
elif score <= 69 and score > 59:
    print("Your grade is: D") 
#elif score <= 59 and score >= 0:
#   print("Your grade is: F") 
else:
    print("Your grade is: F") 

# final message so that if the grade is passing (A-C),it congratulates the user. Otherwise if it is a D or F, it 
# encourages the user to try again).
if score <= 100 and score > 69:
    print("Congrats, you've passed the course!")
else:
    print("Unfortunately, you'll need to retake the course!")











# ////////////////////////////////////// Side Notes:  ////////////////////////////////////// 

# My version checks for 'int' data validity, so it will yell if score is > 100 or < 10
r''' 
score = int(input("Please enter your score(0-100): ")) # asks the user to input a numeric grade (0-100) and casts it to int 
                                                       # data type. Then stores the data into variable 'score'

# if-elif-else structure to convert the score to a letter grade based on a typical scale and render a message depending on grade:
if score <= 100 and score > 89: 
    print("Your grade is: A \nCongrats, you've passed the course!")
    # print("Congrats, you've passed the course!") 
elif score <= 89 and score > 79:
    print("Your grade is: B \nCongrats, you've passed the course!") 
    # print("Congrats, you've passed the course!")
elif score <= 79 and score > 69:
    print("Your grade is: C \nCongrats, you've passed the course!") 
    # print("Congrats, you've passed the course!")
elif score <= 69 and score > 59:
    print("Your grade is: D \nUnfortunately, you'll need to retake the course!")
    # print("Unfortunately, you'll need to retake the course!")
elif score <= 59 and score >= 0:
    print("Your grade is: F \nUnfortunately, you'll need to retake the course!")
    #print("Unfortunately, you'll need to retake the course!")
else:
    print("Invalid score. Please enter a number between 0 and 100.") # for a more robust app, this line tests for 'int' data validity
'''




r'''  
- Wanted to test for valid data by adding something like this:
else:
    print("Invalid score. Please enter a number between 0 and 100.")
...but eventhough it worked it kept returning either of the other 2 optional messages:
- "Congrats, you've passed the course!"
- "Unfortunately, you'll need to retake the course!"
...unless I purposely entered either of the optional 2 messages into each if/elif/else branches, where appropiated
'''