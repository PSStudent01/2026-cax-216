'''
Task 2: Multiplier Closure
Write a Python script (e.g., multiplier_closure.py) that defines a function make_multiplier(factor) which:
    Returns a 'closure' that takes an input x and returns x * factor.
Demonstrate the closure by:
    Creating 2 multiplier functions (e.g., times3 = make_multiplier(3) and times10 = make_multiplier(10)).
    Calling these functions with sample inputs (e.g., print times3(7) and times10(7)) to show the correct outputs.
'''

def make_multiplier(factor):
    # pass
    def multiply(x): # this becomes the 'closure', because it uses 'factor' from the outer function 'make_multiplier(factor)'. 
        return x * factor # what the closure {aka 'inner function'} returns
    return multiply # what the 'outer function' returns.
                    # this line gives back to the inner function ('multiply(x))' itself {in this case 'multiply'}.
                    # you write 'multiply' with no parentheses, bc with parentheses ('multiply()') you’d be calling it.

times3 = make_multiplier(3) # Returns 21
                            # storing the call to function ' make_multiplier(3)' inside variable 'times3', making 'times3' the 
                            # new call ('times3()') to function 'make_multiplier(factor)'
times10 = make_multiplier(10) # Returns 70
                              # storing the call to function ' make_multiplier(10)' inside variable 'times10', making 'times10' the 
                              # new call ('times10()') to function 'make_multiplier(factor)'
# print(times3(7)) # calling function 'make_multiplier(factor)' via 'times3(7))' while passing argument '7'.
# print(times10(7)) # calling function 'make_multiplier(factor)' via 'times10(7))' while passing argument '7'

# More polished:
print()
## Shows closures produce the expected results:
print("Shows closures produce the expected results:")
print(f"times3(7) = {times3(7)}")      # times3(7) = 21
print(f"times10(7) = {times10(7)} \n")    # times10(7) = 70

## Shows each closure keeps its own factor across multiple calls, in other words, "retains the factor":
print("Shows each closure keeps its own factor across multiple calls, in other words, 'retains the factor':")
print(f"times3(5) = {times3(5)}")     # 15
print(f"times10(5) = {times10(5)} \n")   # 50

## Edge cases. These show it works with zero, negatives, and decimals:
print("Edge cases. These show it works with zero, negatives, and decimals:")
print(f"times3(0) = {times3(0)}")        # 0
print(f"times3(-4) = {times3(-4)}")      # -12
print(f"times10(2.5) = {times10(2.5)} \n")  # 25.0

## This shows make_multiplier can create as many independent closures as you like:
print("This shows make_multiplier can create as many independent closures as you like:")
times0 = make_multiplier(0)
print(f"times0(99) = {times0(99)}")      # 0


# //////////////////////////////////// Side Notes /////////////////////////////////////////////////

'''  
Q:
What is a closure, what is it used for?
A:
- A closure is a function that remembers variables from the place where it was created, even after that place has finished 
running.
- In your lab, make_multiplier(3) runs and returns the inner function. Normally, once make_multiplier finishes, its variables
 (like factor) would be gone. But the inner function still needs factor, so Python keeps it alive and attached to the inner 
 function. That attached memory is the 'closure'.
'''

'''
Per AI:
- times3 = make_multiplier(3) calls make_multiplier once with 3. It returns the inner multiply function, and times3 now holds that
function.
- times3(7) calls multiply (the inner function, via the name times3), not make_multiplier. It computes 7 * 3.
- So times3 and times10 are two separate copies of multiply, one remembering 3 and the other remembering 10. That’s the whole 
idea of the lab, so it’s worth getting the comments right.
%
def make_multiplier(factor):
    def multiply(x):  # closure: it uses 'factor' from the outer function
        return x * factor
    return multiply   # return the function itself (no parentheses), not a call to it


# make_multiplier runs once per line; each result is a multiply function remembering its own factor
times3 = make_multiplier(3)    # times3 is a function that multiplies by 3
times10 = make_multiplier(10)  # times10 is a function that multiplies by 10

print(times3(7))   # calls multiply with x = 7, factor = 3 -> 21
print(times10(7))  # calls multiply with x = 7, factor = 10 -> 70

'''