
r'''
Task 1: String Manipulation Challenge
Write a Python script (e.g., string_manipulation.py) that:
-- Prompts the user to enter a sentence.
-- Converts the entire sentence to uppercase and prints the result.
-- Prints the sentence in reverse order.
-- Counts and displays the number of vowels (a, e, i, o, u, regardless of case) present in the sentence.
-- Replaces every space in the sentence with a hyphen (-) and prints the modified string.
Ensure that each output is clearly labeled (for example, “Uppercase:”, “Reversed:”, etc.).
'''

new_string = ""
string = input("Enter a sentence: ") # Prompts the user to enter a sentence.

string = string.upper() # Converts the entire sentence to uppercase.
print("Uppercase: ", end = "")
print(string) # prints the result.
# sentence = print(reversed(sentence))
# sentence = "".join(sentence)
# print(sentence)
print("Reversed: ", end = "")
print(string[::-1]) # Prints the sentence in reverse order.
# print("Reversed:", string[::-1]) # ALTERNATIVE: You could combine them into one line
# print(len(sentence)) # baseline count of all charcaters in the string.
# print(sentence)
# sentence = sentence.lower() # 1) if you apply '.lower()' here, it not only makes the letter case-INSENSITIVE, but it also
                             # CONVERTS the letters to lower case

# Counts and displays the number of vowels (a, e, i, o, u, regardless of case) present in the sentence:
r'''
# ATTEMPT 1 - Kept failing now fixed: 
# for letter.lower() in sentence: # applying .lower() here makes app fail
for letter in string:
    #if letter == '':
    if letter.lower() in "aeiou": # 2) interesting!!! by applying '.lower()' here it does make letters case-insensitive but never 
                                  # changes their CAP status
        # listt = listt + letter
        # new_string = new_string + letter
        # print(new_string)
        # print(letter)
        # print(len(letter))
        new_string = new_string + letter
        # print(new_string)
        #print(len(new_string))
print(len(new_string)) # <------{kept failing until I removed indentaiton from this line}
''' 
#r'''
#ATTEMPT 2 - Worked
for letter in string:
    if letter.lower() in "aeiou":
        new_string = new_string + letter
        # print(len(new_string))
        # print(new_string[letter])
        # print(new_string[letter])
        # print(len(new_string[letter]))
        # print(int(len(new_string[letter])))
print("Total count of vowels in string: ", end = "")
print(len(new_string)) 
#'''

r'''  
# OPTIONAL METHOD:
vowel_count = 0
for letter in string:
    if letter.lower() in "aeiou":
        vowel_count += 1

print("Total count of vowels in string:", vowel_count)
'''


# Replaces every space in the sentence string with a hyphen (-) and prints the modified string.
r'''  
# 1st Attempt: 
for letter in string:  
    if letter == " ":
        # print(letter, sep="-")
        # print(string, sep="-") # The sep argument only works when print gets two or more items. With a single item (string) 
                               # there's nothing to separate, so sep="-" does nothing.
''' 
r''' 
# Method 1 - less simplified:
result = ""
for letter in string:
    if letter == " ":
        result = result + "-"
    else:
        result = result + letter
#print(result)
print("Hyphenated: ", end = "")
print(result)
'''

#r'''
# Method 2 - more simplified:
# print("Hyphenated: ", end = " ")
print("Hyphenated: ", end = "")
print(*string.split(" "), sep="-")
#'''

# sentence - "Hello my friend"