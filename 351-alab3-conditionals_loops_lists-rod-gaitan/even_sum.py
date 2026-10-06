
# Creates script even_sum.py

r''' 
# 1)
# Write a script to perform a 'for loop' that:
## Uses a for loop to iterate through the numbers 1 to 50.
## Calculates the sum of all even numbers in that range.
## Prints the result as: "The sum of even numbers from 1 to 50 is X." (where X is the calculated sum).

# even_num = []  # wrong data type variable
even_sum = 0 

for num in range(1, 51): # 'for loop' iterates through the numbers 1 to 50.
                        # to create a range of 1 to 50, the start needs to be 1 and the stop needs to be 51
    if num % 2 == 0:    # 1) conditional structure checks for even integers, and if integer is even...
        # even_num.append(num)
        # print(even_num)
        # even_sum = even_sum + num # This works the same but is longer method!
        even_sum += num # 2) it adds integer to current integer sum/count. Same as above but is shorter method! 
# print(even_sum)
print(f"The sum of even numbers from 1 to 50 is {even_sum}.")



# 2) 
# Modifying the script to perform the same task using a 'while loop' instead of a 'for loop':

num = 1  # variable 'num' declared and initialized to start count number at 1
even_sum = 0 # variable 'even_sum' declared and initialized to start tracking the total sum

while num != 51: # while loop indicating to run iterations for as long as 'num' is not equal to 51
    if num % 2 == 0: # and at each iteration, if 'num' is an even number then...
        even_sum += num # ...add such number to total being tracked by variable 'even_sum'
    num += 1 # manual bump up at each iteration, by a step of 1
print(f"The sum of even numbers from 1 to 50 is {even_sum}.") # positioned the print() function in far left, ALONGSIDE to the 
                                                              # 'While' loop (and not WITHIN the loop) so that ONLY and ONLY
                                                              # when the loop completes, will it print the message stated.
                                                              # If you place it WITHIN the 'While loop' or WITHIN the 'If conditional
                                                              # structure', it will execute according to each of those. 
'''

r'''
Comment:
- Both loop versions produce the same result. However, I found the 'For Loop' to be more beneficial in this case, because:
-- it lets you use the 'range()' function, which I think gives you a bit more control on which numbers are processed. 
-- it also bumps the count/number or whatever is being counted/tracked automatically, whereas using the While loop, you'd 
have to establish that step manually, for example: "num += 1"
-- Also forgetting 'num += 1' will cause an infinite loop.
'''









# /////////////////////// Side Notes:  //////////////////////////////////
'''
- when composing a While loop:
-- i, counter, num, number are essentially the same depending on the context of the requirements
-- thus they all need a start point, for example:
--- i = 0
--- counter = 0
--- num = 0
--- number = 0
[A start point isn't enough on its own. A while loop needs three things:
- Initialize the variable before the loop
- Condition that eventually becomes false
- Update inside the loop (like num += 1)]
'''



# /////////////////////// Attempts ///////////////////////////////////////

r'''
# 1) 
# - how to add 1 to the existing count!

# - [no need for init variable ]   # <----{VIP}

for num in range(1, 51): 
    if num % 2 == 0:
        # num = num + 1  # <----{adds 1 to the current count}
        num += 1 # <----{alternate: adds 1 to the current count}
        print(num, end=", ")  # <----{itc, this is correct position for print()}
#print(num)  # <----{itc, this is INcorrect position for print(), bc we're not looking for sum of numbers}
# [Returns: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, ]


# 2)
# - how to sum items of a range!

even_sum = 0   # <----{VIP}

for num in range(1, 51): 
    if num % 2 == 0:
        # even_sum = even_sum + num    # This works the same but is longer method   <----{VIP}
        even_sum += num   # <----{VIP}
print(even_sum)  # <----{itc, this is correct position for print()}
# [Returns: 650]
'''


r'''  
# First attempt modifying the script to perform the same task using a 'while loop'- Failed!!!!!!!!
even_sum = 0
count = 0
num = 1
# range = range(1, 11)

# while num >= and num <= 51:
while num != 51:
    if num % 2 == 0:
        even_sum += num
        # count = count + 1
        count += 1
        # print(f"The sum of even numbers from 1 to 50 is {even_sum}.")
        # count = count + 1 # causes endless loop
print(f"The sum of even numbers from 1 to 50 is {even_sum}.")
'''