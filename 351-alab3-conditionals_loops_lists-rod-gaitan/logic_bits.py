
# Create a short script logic_bits.py that:
## Demonstrates the use of logical operators: for example, ask the user for two boolean inputs (True/False or 1/0) and show the results of and, or, and not on those inputs.
## Demonstrates bitwise operators (&, |, ^, ~, <<, >>) on two small integers (for example, 5 and 3). Print the results in binary form using bin() to show what is happening at the bit level.
# This task is for exploration and will not be heavily graded; it is to encourage you to play with these operators and see their effects.

###################################### MY DRAFT: ##########################################

age_approval  = input("Are you over 21 or over?  ") # takes input and stores as string
print()
residency_approval = input("Are you a resident of NYC?  ")  # takes input and stores as string
print()

# Converts the user's typed answer into a True or False boolean value for 'age_approval'
if age_approval in ('y', 'Y', 'yes', 'YES', 'Yes'): # Checks for amost every possible spelling of 'yes'
    age_approval = True
elif age_approval in ('n', 'N', 'no', 'NO', 'No'):
    age_approval = False
# else:
    # print("Invalid input, please try again!")

# Converts the user's typed answer into a True or False boolean value for 'residency_approval'
if residency_approval in ('y', 'Y', 'yes', 'YES', 'Yes'): # Checks for amost every possible spelling of 'yes'
    residency_approval = True
elif residency_approval in ('n', 'N', 'no', 'NO', 'No'):
    residency_approval = False
# else:
    # print("Invalid input, please try again!")


# Scenario where BOTH answers must be True for qualification:
if age_approval == True and residency_approval == True: # Notice, evaluating specific boolean vales here for both variables
    print("Decision: Subject qualifies for the next vetting stage.")
else:
    print("Decision: Subject is disqualified from moving forward in the vetting process.")

r''' 
# Scenario where AT LEAST 1 answer must be True for qualification:
if age_approval or residency_approval:  # Here I used 'truthy' concept for evaluating specific boolean values.
    print("Subject qualifies for the next vetting stage.")
else:
    print("Subject is disqualified from moving forward in the vetting process.")
'''

r'''
# Scenario where user answers yes to NOT being 21 or over:
print("Not 21 or over (not):", not age_approval) # if user answers yes here, it gets converted to False 

# Scenario where user answers yes to NOT being from NYC:
print("Not an NYC resident (not):", not residency_approval) #  if user answers yes here, it gets converted to False 
''' 

############################################ AI Draft: ##################################################

r''' 
# - try to consolodate all 3 case scenarios, so that I don't have to comment out all other scenarios while running one scenario
age_input = input("Are you 21 or over? (y/n): ")
residency_input = input("Are you a resident of NYC? (y/n): ")

age_approval = age_input.strip().lower() in ("y", "yes")
residency_approval = residency_input.strip().lower() in ("y", "yes")

print("Both (and):", age_approval and residency_approval)
print("At least one (or):", age_approval or residency_approval)
print("Not 21 or over (not):", not age_approval)
print("Not an NYC resident (not):", not residency_approval)
'''

###################################### Analysis of bits for 5 and 3: ##########################################

# Demonstrates bitwise operators (&, |, ^, ~, <<, >>) on two small integers (for example, 5 and 3). Print the results in binary 
# form using bin() to show what is happening at the bit level.

x = 5
y = 3

print("\n--- Bitwise operators ---")
print(f"x = {x} -> {bin(x)}")
print(f"y = {y} -> {bin(y)}")

print(f"x & y  = {x & y} -> {bin(x & y)}")      # AND: 1 only where both bits are 1
print(f"x | y  = {x | y} -> {bin(x | y)}")      # OR: 1 where either bit is 1
print(f"x ^ y  = {x ^ y} -> {bin(x ^ y)}")      # XOR: 1 where the bits differ
print(f"~x     = {~x} -> {bin(~x)}")            # NOT: equals -x - 1
print(f"x << 1 = {x << 1} -> {bin(x << 1)}")    # shift left: doubles the number
print(f"x >> 1 = {x >> 1} -> {bin(x >> 1)}")    # shift right: halves it, drops remainder



# ///////////////////////////////Side Notes: //////////////////////////////

r'''  
# AI Version:
# Pre-approval Application

age_input = input("Are you 21 or over? (y/n): ")
residency_input = input("Are you a resident of NYC? (y/n): ")

# Convert text to booleans; anything that isn't a yes counts as False
age_approval = age_input.strip().lower() in ("y", "yes")
residency_approval = residency_input.strip().lower() in ("y", "yes")

print("\nage_approval:", age_approval)
print("residency_approval:", residency_approval)

# and: BOTH must be True
print("Both (and):", age_approval and residency_approval)

# or: AT LEAST ONE must be True
print("At least one (or):", age_approval or residency_approval)

# not: flips the value
print("Not 21 or over (not):", not age_approval)
print("Not an NYC resident (not):", not residency_approval)

if age_approval and residency_approval:
    print("Subject qualifies for the next vetting stage.")
else:
    print("Subject is disqualified from moving forward in the vetting process.")
'''