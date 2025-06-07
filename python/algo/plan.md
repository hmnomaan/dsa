Great! Now that you're ready to start learning **key algorithms**, let's dive deeper into each of these with **Python implementations**, **explanations**, and **practical examples**.  

---

# **5 Essential Algorithms in Python (For DSA Beginners)**

## **1. Linear Search**  
**What it does:** Checks each element in a list one by one until the target is found.  
**Time Complexity:** `O(n)` (worst case).  

### **Python Code**  
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

# Example
nums = [4, 2, 7, 1, 9]
print(linear_search(nums, 7))  # Output: 2 (index of 7)
```

---

## **2. Binary Search**  
**What it does:** Efficiently searches a **sorted** list by repeatedly dividing the search range in half.  
**Time Complexity:** `O(log n)`.  

### **Python Code (Iterative)**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found

# Example (List must be sorted)
sorted_nums = [1, 2, 3, 4, 7, 9]
print(binary_search(sorted_nums, 7))  # Output: 4
```

---

## **3. Bubble Sort**  
**What it does:** Repeatedly swaps adjacent elements if they are in the wrong order.  
**Time Complexity:** `O(n²)` (inefficient for large lists).  

### **Python Code**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        if not swapped:  # Early exit if already sorted
            break
    return arr

# Example
nums = [5, 3, 8, 4, 2]
print(bubble_sort(nums))  # Output: [2, 3, 4, 5, 8]
```

---

## **4. Selection Sort**  
**What it does:** Selects the smallest element and swaps it into the correct position.  
**Time Complexity:** `O(n²)`.  

### **Python Code**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
    return arr

# Example
nums = [64, 25, 12, 22, 11]
print(selection_sort(nums))  # Output: [11, 12, 22, 25, 64]
```

---

## **5. Insertion Sort**  
**What it does:** Builds the final sorted list one element at a time (like sorting playing cards).  
**Time Complexity:** `O(n²)` (but efficient for small or nearly sorted lists).  

### **Python Code**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example
nums = [12, 11, 13, 5, 6]
print(insertion_sort(nums))  # Output: [5, 6, 11, 12, 13]
```

---

## **When to Use Which Algorithm?**
| Algorithm | Best Case | Worst Case | Use Case |
|-----------|----------|------------|----------|
| **Linear Search** | `O(1)` (first element) | `O(n)` | Unsorted lists |
| **Binary Search** | `O(1)` (mid element) | `O(log n)` | Sorted lists |
| **Bubble Sort** | `O(n)` (if already sorted) | `O(n²)` | Learning, small lists |
| **Selection Sort** | `O(n²)` | `O(n²)` | Small lists |
| **Insertion Sort** | `O(n)` (if nearly sorted) | `O(n²)` | Small or partially sorted lists |

---

## **Next Steps**
1. **Practice these algorithms** on [LeetCode](https://leetcode.com/) or [HackerRank](https://www.hackerrank.com/).  
2. **Compare their speeds** using `time.time()` in Python.  
3. **Learn more efficient sorts** like **Merge Sort** and **Quick Sort**.  

🚀 **Now you’re ready to implement these in your DSA journey!** Let me know if you need further explanations. Happy coding! 😊