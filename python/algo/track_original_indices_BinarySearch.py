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

if result != -1:
    print(f"Element found at original index {result}.")
else:
    print("Element not found.")