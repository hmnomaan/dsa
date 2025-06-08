def binary_search_with_indices(sorted_pairs, target):
    low, high = 0, len(sorted_pairs) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_pairs[mid][0] == target:
            return sorted_pairs[mid][1]  # Return original index
        elif sorted_pairs[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Unsorted data with original indices
data = [64, 34, 25, 12, 22, 11, 90, 45, 78, 89, 34, 12, 56, 78, 90, 11, 25]
target = 78

# Create a list of (value, original_index) pairs
indexed_data = [(value, idx) for idx, value in enumerate(data)]
print("non-sorted")
print(indexed_data)
# Sort by value
sorted_indexed_data = sorted(indexed_data, key=lambda x: x[0])
print("sorted_old-indexed_data")
print(sorted_indexed_data)
# Perform binary search on sorted pairs
result = binary_search_with_indices(sorted_indexed_data, target)

# if result != -1:
#     print(f"Element found at original index {result}.")
# else:
#     print("Element not found.")
    
    
    
# practice1
def binary_search_index(sorted_arr,target):
    left,right=0,len(sorted_arr)-1
    while(left<=right):
        mid=(left+right)//2
        if sorted_arr[mid][0]==target:
            return sorted_arr[mid][1] #RETURN originl index
        elif sorted_arr[mid][0] <target:
            left=mid+1
        else:
            right=mid-1
    return -1

nums=[2,3,42,34,55,66,33,22,33,3,2,34,54,43,23,44,55,66]
target=66

index_nums=[(value,idx) for idx,value in enumerate(nums)]
print(f"vaule id pair old order : {index_nums}")
sorted_index_nums=sorted(index_nums,key=lambda x:x[0])
print(f"vaule id pair sorted order : {sorted_index_nums}" )
result=binary_search_index(sorted_index_nums,target)

if result != -1:
    print(f"Element {target} , found at index of {result}")
else:
    print("garbar hein , garbar hein")