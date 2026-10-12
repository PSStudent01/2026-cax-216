# Task 1: Using Built-in Modules:
r'''
Task 1: Using Built-in Modules:
Write a Python script (e.g., builtin_usage.py) that:
- Imports the math, random, and platform modules.
- Generates a random integer between 1 and 100 using the random module.
- Calculates the square root of that number using math.sqrt and rounds it down (using math.floor or by converting to an integer).
- Retrieves and prints the system's OS name and Python version using functions from the platform module.
Your program should print descriptive messages for each output (e.g., “Random Number:”, “Square Root (floored):”, “Operating System:”, “Python Version:”).
'''

# //////////////////////////////////// Code Begin:///////////////////////////////////////////////
# Imports the math, random, and platform modules:
import math, random, platform 

# Generates a random integer between 1 and 100 using the random module:
random_num = random.randint(1, 100)
print(f"Random Number: {random_num}")

# Calculates the square root of that number using math.sqrt and rounds it down (using math.floor or by converting to an integer).
r''' 
## Alternative 1:
sqrt_num = math.sqrt(25)
#print(sqrt_num)
sqrt_num = math.floor(sqrt_num)
print(sqrt_num)
## Alternative 2 - More DRY code:
sqrt_num1 = math.floor(math.sqrt(25))
print(sqrt_num1)
'''
## Alternative 3 - using random_num, rather than a literal:
sqrt_num = math.floor(math.sqrt(random_num)) # sqrt of 95 = 9.747, floored = 9.
# print(sqrt_num1)
print(f"Square root of {random_num}: {sqrt_num} (floored)")

# Retrieves and prints the system's OS name and Python version using functions from the platform module:
## System's OS name:
os_name = platform.system()
# print(os_name)
print(f"Operating System: {os_name}")
## Python version:
py_version = platform.python_version()
# print(py_version)
print(f"Python Version: {py_version}")

# //////////////////////////////////// Code End:///////////////////////////////////////////////