To remove duplicates from an array without using built-in functions like `set()`, you can use a manual approach with a list to track unique elements and a set to efficiently check for duplicates. Here's how to implement it:

### Solution Code
```python
def remove_duplicates(arr):
    unique_elements = []  # List to store unique elements
    seen = set()          # Set to track elements we've already added
    for element in arr:
        if element not in seen:
            unique_elements.append(element)  # Add to result if not seen
            seen.add(element)                # Mark as seen
    return unique_elements

# Example usage
data = [64, 34, 25, 12, 22, 11, 90, 45, 78, 89, 34, 12, 56, 78, 90, 11, 25]
result = remove_duplicates(data)
print("Array with duplicates removed:", result)
```

### Explanation
1. **Initialize Data Structures**:
   - `unique_elements`: A list to store elements without duplicates.
   - `seen`: A set to keep track of elements that have already been added to `unique_elements`.

2. **Iterate Through the Array**:
   - For each element in the input array, check if it exists in the `seen` set.
   - If the element is **not** in `seen`, add it to both `unique_elements` and `seen`.
   - If the element is already in `seen`, skip it.

3. **Return the Result**:
   - The `unique_elements` list contains the original array's elements without duplicates, preserving the order of their first occurrence.

### Output
```
Array with duplicates removed: [64, 34, 25, 12, 22, 11, 90, 45, 78, 89, 56]
```

### Key Notes
- **Time Complexity**: O(n) due to the single pass through the array and O(1) average-time complexity for set operations.
- **Space Complexity**: O(n) for storing unique elements and tracking seen elements.
- **Order Preservation**: The order of elements in the output matches their first occurrence in the input array.