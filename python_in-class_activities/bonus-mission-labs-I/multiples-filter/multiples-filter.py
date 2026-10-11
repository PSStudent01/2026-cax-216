r'''
#
The Multiples Filter (Loops & Lists)
Goal: Practice iterating through data with a for loop and building a new list on the fly.
Your Mission
Create a list of numbers from 1 to 20.
Create a second, empty list called multiples_of_three.
Use a for loop to look at every number in your first list. If a number is perfectly divisible by 3, append it to your second list.
Print the final multiples_of_three list.

Hint: To check if a number is perfectly divisible by something, use the modulo operator (%), which calculates the remainder of a 
division. If num % 3 == 0, it's a multiple of 3!
'''

#r'''  
# METHOD 1 - For_Loop - Successful:
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

multiples_of_three = []

for num in num_list:
    if num % 2 == 1:
        # multiples_of_three = multiples_of_three.append(num)
        multiples_of_three.append(num)
print(multiples_of_three)
#'''

r'''  
# METHOD 2 - While_Loop - Successful:
multiples_of_three = []

num = 0

while num < 20:
    if num % 2 == 1:
        multiples_of_three.append(num)
    num = num + 1
print(multiples_of_three)
'''

r'''  
# METHOD 3 - While_Loop - Failed:
multiples_of_three = []

num = 20 # <----{num/count starts from 20, rather 0}

while num < 20:
    if num % 2 == 1:
        multiples_of_three.append(num)
    num = num - 1 # <----{counter counts backwards since starting from a higher num other than zero}
    # num += 1
print(multiples_of_three)
'''