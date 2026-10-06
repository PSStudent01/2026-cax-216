
# Write a script list_operations.py that:
## Creates a list of at least 5 integers (you can choose them arbitrarily or ask the user to input numbers to populate the list).
## Prints the original list.
## Uses the built-in sorted() function to print a sorted version of the list without modifying the original list.
## Uses the list’s .sort() method to sort the list in place, then prints the list to show it is now sorted.
## Adds a new element to the list (append an integer), then prints the updated list.
## Removes an element from the list (you can remove by value or index), then prints the list again.
## Uses the reverse() method to reverse the list, then prints the reversed list.

print()
int_list = [3, 5, 6, 2, 7, 9, 1, 8]
print("1) Created list of at least 5 integers: int_list = [3, 5, 6, 2, 7, 9, 1, 8]\n")
print(f"2) This is the original list: {int_list}\n")
print(f"3) This is the sorted version without modifying the original list: {sorted(int_list)}\n")
print(f"3a) This is the original list again, to show that it still remains intact: {int_list}\n")
# sorted_list = int_list.sort()
# sorted_list = sorted_list.sort(int_list)
# int_list.sort(int_list)
int_list.sort() # applying the '.sort()' method to the list, so that it physically sorts/modifies the original list. 
print(f"4) This list is now PHYSICALLY sorted, after applying the '.sort()' method to the list: {int_list}\n")
print(f"4a) This is the original list again, to show that its sort order has in fact been modified: {int_list}\n")
# int_list = int_list.append(100) # you have to call the method on its own line, with NO assignment as seen below, otherwise it will return 'None'
int_list.append(100) # appends 100 to the existing 'int_list' list
print(f"5) This is the original list again, but this time showing the appended number of '100': {int_list}\n")
int_list.pop(8) # using the '.pop()' function to remove a particular integer (e.g 100). You must use the integer's index to Id the number you want to target
print(f"6) This is the original list again, but this time WITHOUT the number '100': {int_list}\n")
int_list.reverse() # using the '.reverse()' function to reverse the sort order of the list
print(f"7) This is the original list again, but this time in REVERSED sort order: {int_list}")




