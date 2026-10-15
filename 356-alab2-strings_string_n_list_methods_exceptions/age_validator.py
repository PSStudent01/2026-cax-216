
r'''
Task 3: Custom Exception Test (Age Validator)

    Write a function validate_age(age) that:
        Accepts a parameter age.
        Raises a ValueError with an appropriate message if the age is not between 0 and 120 (inclusive).
    Write a short script (e.g., age_validator.py) that:
        Prompts the user to enter their age.
        Calls validate_age with the input value.
        Uses try/except to catch the exception if the age is invalid, printing the error message.
        If no exception is raised, prints a message indicating that the age is accepted.
'''

r''' 
Attempt 1 - Works, but buggy:
def validate_age(age):
    # try: # 1) Improperly placed, moved it to 'main()' function
    try:
        if age >= 0 and age <= 120:
            print("Age is accepted!")
        #else:
            #print("Invalid Input: Age outside of age range. Age not accepted!")
    # except ValueError:  # 2) Improperly placed, moved it to 'main()' function
        # print("Invalid input: Enter age as a whole number") # 3) Improperly placed, moved it to 'main()' function
    except ValueError:
        print("Invalid input: Enter age between 0 and 120")

# validate_age(20)

def check_age(age):
    if not (age >= 0 and age <= 120):
    # if score < 0 or score > 150: 
        raise ValueError("Score must be between 0 and 120 (inclusive).")

def main():
    try:
        age = int(input("Enter age: "))
        validate_age(age)  # <------------------{Executes, but seems to stop here and not execute the next line}
        check_age(age) 
    # except ValueError:
        # print("Invalid input: Enter age as a whole number")
    # except ValueError:
        # print("Invalid input: Enter age between 0 and 120")
    except ValueError as e:
        print(e)
main()
'''

r'''  
# Attempt 2 - It works, except it renders the generic .py message when user enters value of wrong data type :
def validate_age(age):
    # try: # 1) Improperly placed, moved it to 'main()' function
    try:
        if age >= 0 and age <= 120:
            print("Age is accepted!")
        #else:
            #print("Invalid Input: Age outside of age range. Age not accepted!")
    except ValueError:  # 2) Improperly placed, moved it to 'main()' function
        print("Invalid input: Enter age as a whole number") # 3) Improperly placed, moved it to 'main()' function

   
#except ValueError:
#print("Invalid input: Enter age between 0 and 120")
#print("Invalid input: Enter age as a whole number")


# validate_age(20)

# Raising an exception specifically for when age is outside of range, rather than using 'else' statement:
def check_age(age):
    if not (age >= 0 and age <= 120):
    # if score < 0 or score > 150: 
        raise ValueError("Score must be between 0 and 120 (inclusive).")


def main():
    try:
        age = int(input("Enter age: "))
        validate_age(age)  
        check_age(age) 
    # except ValueError:
        # print("Invalid input: Enter age as a whole number")
    # except ValueError:
        # print("Invalid input: Enter age between 0 and 120")
    except ValueError as e:
        print(e)
        # print("Invalid input: Enter age as a whole number")
main()
'''

r''' 
# Attempt 3 - this was a total bust!!!!!:
def validate_age(age):
    # try: # 1) Improperly placed, moved it to 'main()' function
    #try:
    if age >= 0 and age <= 120:
        print("Age is accepted!")
    #else:
        #print("Invalid Input: Age outside of age range. Age not accepted!")
    #except ValueError:  # 2) Improperly placed, moved it to 'main()' function
        #print("Invalid input: Enter age as a whole number") # 3) Improperly placed, moved it to 'main()' function


# except ValueError:
# print("Invalid input: Enter age between 0 and 120")
# print("Invalid input: Enter age as a whole number")


# validate_age(20)

# Raising an exception specifically for when age is outside of range, rather than using 'else' statement:
def check_age(age):
    if not (age >= 0 and age <= 120):
    # if score < 0 or score > 150: 
        raise ValueError("Score must be between 0 and 120 (inclusive).")


def main():
    try:
        age = int(input("Enter age: "))
        #validate_age(age)  
        check_age(age) 
    except ValueError:
        print("Invalid input: Enter age as a whole number")
        # return

    try:
        validate_age(age)
        #print("Age is accepted!")
    # except ValueError:
        # print("Invalid input: Enter age between 0 and 120")
    except ValueError as e:
        print("Error: ", e)
        # print("Invalid input: Enter age as a whole number")
main()
'''


# Attempt 4 - It works, except it renders the generic .py message when user enters value of wrong data type rendering [invalid literal for int() with base 10: 'e']:
def validate_age(age):
    # try: # 1) Improperly placed, moved it to 'main()' function
    try:
        if age >= 0 and age <= 120:
            print("Age is accepted!")
        #else:
            #print("Invalid Input: Age outside of age range. Age not accepted!")
    except ValueError:  # 2) Improperly placed, moved it to 'main()' function
        print("Invalid input: Enter age as a whole number") # 3) Improperly placed, moved it to 'main()' function

  
# except ValueError:
# print("Invalid input: Enter age between 0 and 120")
# print("Invalid input: Enter age as a whole number")


# validate_age(20)

# Raising an exception specifically for when age is outside of range, rather than using 'else' statement:
def check_age(age):
    if not (age >= 0 and age <= 120):
    # if score < 0 or score > 150: 
        raise ValueError("Age must be between 0 and 120 (inclusive).")


def main():
    try:
        age = int(input("Enter age: "))
        validate_age(age)  
        check_age(age) 
    # except ValueError:
        # print("Invalid input: Enter age as a whole number")
    # except ValueError:
        # print("Invalid input: Enter age between 0 and 120")
    except ValueError as e:
        print(e)
main()

r''' 
# ///////////////////////////// Side Notes /////////////////////////
#
# VIP:  YOU PLACE THE 'Try' handler around that which causes (raises) the error message to beging with!!!!!!

#
- Per AI the fix to that generic error message is as follows. I havs test this option eventually:
def validate_age(age):
    # Raise an error if the age is outside the allowed range (0-120 inclusive)
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120 (inclusive).")


def main():
    # Step 1: convert the input (fails if it isn't a whole number)
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input: Enter age as a whole number")
        return

    # Step 2: validate the range (fails if outside 0-120)
    try:
        validate_age(age)
        print("Age is accepted!")
    except ValueError as e:
        print("Error:", e)


main()

'''