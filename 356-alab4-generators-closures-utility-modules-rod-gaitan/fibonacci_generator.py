'''
Task 1: Fibonacci Generator

Write a Python script (e.g., fibonacci_generator.py) that defines a generator function gen_fibonacci(n) which:
Yields the Fibonacci sequence up to the first n numbers. (Recall: Fibonacci sequence starts with 0, 1, 1, 2, 3, 5, …)
Write test code that iterates over the generator (e.g., using a for-loop) and prints each Fibonacci number with a clear label.
'''

''' 
# 1st Attempt:
def gen_fibonacci(n):
    # pass
    # return range(n)
    for i in range(n):
        print(n) 
        # return n  # returns 10
        # return i # returns 0

# print(gen_fibonacci(10))
# gen_fibonacci(10)
print(gen_fibonacci(10)) # Returns: a series of '10' 10x
    #print(gen_fibonacci(10))
'''

'''
# 2nd Attempt:
def gen_fibonacci(n):
    # pass   
    # return range(n)
    numbers = range(n)
    #print(numbers)
    for i in numbers:
        #print(i)
        print(i, end=" ")

# print(range(12))
gen_fibonacci(12) # Returns: the entire list of numbers from '0' to '11'.
'''   

'''
# 3rd Attempt:
def gen_fibonacci(n):
    # pass   
    # return range(n)
    numbers = range(n)
    #print(numbers)
    for i in numbers:
        # print(i)
        # print(i, end=" ")
        # numbers = numbers + i # causes TypeError: unsupported operand type(s) for +: 'range' and 'int'
        # print(numbers[0], end=" ") # prints 0 1 2 3 4 5 6 7 8 9 10 11 0 0 0 0 0 0 0 0 0 0 0 0 
        # print(numbers[i], end=" ") # prints 0 1 2 3 4 5 6 7 8 9 10 11 0 1 2 3 4 5 6 7 8 9 10 11
        print(numbers[i] + numbers[i], end=" ") # 0 1 2 3 4 5 6 7 8 9 10 11 0 2 4 6 8 10 12 14 16 18 20 22 
# print(range(12))
gen_fibonacci(12) # 
'''

# Writing a Python script (e.g., fibonacci_generator.py) that defines a generator function gen_fibonacci(n) which:
# 4th Attempt - It Worked!!:
def gen_fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        yield a   # yield i # Yield the current Fibonacci number
        a, b = b, a + b # Update a and b

# print(gen_fibonacci(12)) # Returns a generator object: <generator object gen_fibonacci at 0x00000174C86DF4C0>

print("First 12 Fibonacci numbers:")

for number in gen_fibonacci(12):
    print(number, end=" ") # Returns: 0 1 1 2 3 5 8 13 21 34 55 89

print()


# ////////////////////////////////// PENDING Optional: ////////////////////////////////////////
'''
- The rubric says the test loop should print each Fibonacci number “with a clear label.” Right now  numbers print on one 
line under a single heading. but it looks like “each number with a label” is what they want:
%
for index, number in enumerate(gen_fibonacci(12), start=1):
    print(f"Fibonacci number {index}: {number}")

That produces:

Fibonacci number 1: 0
Fibonacci number 2: 1
Fibonacci number 3: 1
Fibonacci number 4: 2
...
Fibonacci number 12: 89

OR MAYBE:
The one risk is the rubric's wording: “prints the sequence with clear, accurate labels” and the task says to print 
“each Fibonacci number with a clear label.” A single heading over one line of numbers is a reasonable reading, and the rubric 
only says partial credit for minor labeling issues, so the worst case is a small deduction. If you ever want to remove that 
risk, a one-line change does it:
%
print(f"Fibonacci number {index}: {number}")

inside an enumerate loop, but it's optional.

print(f"Fibonacci number {index}: {number}")
'''