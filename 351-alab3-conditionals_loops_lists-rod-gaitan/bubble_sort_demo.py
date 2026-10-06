
# Implement a simple bubble sort in a script bubble_sort_demo.py:
## 1) Use a list of unsorted integers (you can use a fixed example list like [64, 25, 12, 22, 11] or a list of random numbers).
## 2) Implement the bubble sort algorithm using nested loops:
### Loop through the list elements, and for each element, loop through the list again comparing adjacent pairs.
### Swap elements if they are in the wrong order.
### Continue until the list is sorted.
## 3) Print the list at each pass of the outer loop to show the progress of the sorting.
## 4) Finally, print the sorted list.

# bubble_sort_demo.py

nums = [64, 25, 12, 22, 11]
print("Original list:", nums)   # prints original list

for i in range(len(nums) - 1):  # outer loop: one pass per iteration.
                                # 1) counts the number of numbers, minus 1, then for every number in that range, it does the following...
    for j in range(len(nums) - 1 - i):  # inner loop: compare adjacent pairs
                                        # 2) counts the number of numbers, minus 1, minus that number then for every number in that range, it does the following...
        if nums[j] > nums[j + 1]: # If the left neighbor is bigger than the right neighbor,
                                  # the pair is out of order and needs to be swapped.
            nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Swap the two values in one line (Python's tuple swap).
    print(f"After pass {i + 1}:", nums)  # inside outer loop, outside inner loop

print("Sorted list:", nums)    # prints sorted list