def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Unsorted data
data = [64, 34, 25, 12, 22, 11, 90, 45, 78, 89, 34, 12, 56, 78, 90, 11, 25]
target = 78

# Sort the data first
sorted_data = sorted(data)
print(sorted_data)
# Perform binary search
result = binary_search(sorted_data, target)

if result != -1:
    print(f"Element found at index {result} in the sorted array.")
else:
    print("Element not found.")
    


# output:

# F:\0_codings\07-DSA\dsa>python .\python\algo\unsort_BinarySearch.py
# [11, 11, 12, 12, 22, 25, 25, 34, 34, 45, 56, 64, 78, 78, 89, 90, 90]
# Element found at index 12 in the sorted array.


def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Unsorted data
data = [64, 34, 25, 12, 22, 11, 90, 45, 78, 89, 34, 12, 56, 78, 90, 11, 25]
target = 78

# Perform linear search
result = linear_search(data, target)

if result != -1:
    print(f"Element found at index {result} in the original array.")
else:
    print("Element not found.")
    
    
    # output 
    # Element found at index 8 in the original array.