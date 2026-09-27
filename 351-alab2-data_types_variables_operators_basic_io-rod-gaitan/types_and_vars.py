
print()
##################################### Part 1 - Python Basics and Output ##################################################
#
name = "Rod Gaitan" # my name
age = 12  # my age in another alien dimension 
height = 1.651 # my height, and yes I did play high school basketball
# print("Hello, my name is " + name + ". I am " + str(age) + " years old and " + str(height) + " meters tall.") #/ long method. Requires Casting
# print(f"Hello, my name is {name}. I am {str(age)} years old and {str(height)} meters tall.")  #/ Casting was not needed, although it worked with it
print(f"Hello, my name is {name}. I am {age} years old and {height} meters tall.")  #/ recommended method. Does not require Casting 
print()


# Modifying the above script to perform some simple calculations and demonstrate different operators:

## Calculating what my age will be in 5 years:
age = age + 5
print(f"In 5 years, I will be {age} years old.")  # calculates age in 5 years, while printing the output simultaneously.
print()

## Calculating the area of a rectangle:
width = 5.5
height = 2
rect_area = height * width # calculating the area of a rectangle
# print(f"The area of a 5.5 x 2 rectangle is {rect_area}") # failed!
print(f"The area of a 5.5 x 2 rectangle is {rect_area}") # renders the calculated rectangle area, given the width & the height.
print()

## Demonstrate the use of at least two different arithmetic operators (e.g., +, -, *, /, //, or %) and one string concatenation or repetition (e.g., using + to join strings or * to repeat a string).
### Calculating APY for the purchase of a CD for a certain term:
principal = 100000   # my initial investment
r = 0.0388 # interest rate CD offers, itc 3.88% (aka 3.88 / 100) 
n = 2   # number of times interest compounds per year (12 = monthly, 4 = quarterly, 365 = daily, 1 = annually), itc semi-annually
t = 1  # the term of the investment on a year basis, itc 1 year.

total_earnings = float(principal) * (1 + r/n)**(n*t) # calculates the APY for a CD that returns some interest for a certain term 
# print(total_earnings) # correct, but not polished enough!
# print(round(total_earnings, 2)) # correct, but not polished enough!
print(f"My initial investment of ${principal} will generate a total of ${round(total_earnings, 2)} in the term of {t} year(s \non a CD with {r} APY!")
print("yoohoo! " * 5)
