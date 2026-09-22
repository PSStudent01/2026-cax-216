print(4+9)
print(4.7 / 2)
print("Hello World, " * 3)
print("Hello World, " * 3, end =' ') # so end =' ' is like saying ignore teh <Return> action
print('4' * 9) # returns 444444444
# print('4' + 9) # generates traceback error
print('4' + str(9))  # generates '49' NOT '13' bc you're adding strings, not intergers
print(int('4') + 9) # generates '13' NOT 49 bc you're adding intergers, not strings
print('h', 'e', 'l', 'l', '0', sep='-')
print('h', 'e', 'l', '\n', 'l', '0', sep='-') # '\' = stop processing here; 'n' = start a new line ; also we did '\n' bc we're using a method here.
print('Twinkle twinkle little star, \nHow I wonder what you are! \nUp above the world so high, \nLike a diamond in the sky.') # '\n' aka Escape 'n' character. It is used to break a message into different pieces