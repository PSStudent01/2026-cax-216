
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
print("Original list:", nums)  

for i in range(len(nums) - 1):  # outer loop: one pass per iteration
    for j in range(len(nums) - 1 - i):  # inner loop: compare adjacent pairs
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]  # swap
    print(f"After pass {i + 1}:", nums)  # inside outer loop, outside inner loop

print("Sorted list:", nums)