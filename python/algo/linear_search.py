# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Return index if found
#     return -1  # Return -1 if not found

# # Example
# nums = [4, 2, 7, 1, 9]
# print(linear_search(nums, 7))  # Output: 2 (index of 7)

#practice1

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

nums=[2,3,4,1,33,22,11]
print(linear_search(nums,33))

# practice 2

# will make a function named linear search

def linear_search(arr,target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i #it should be indices, so that we can return the index value
    return -1

numbers=[7,3,4,9,10,22,223,56,78]
print(linear_search(numbers,223))
    
    
    
    
# Practice 3 ---let's try with different approach with enumerate function 

def linear_search_enum(arr,target):
    for index,value in enumerate(arr):
        if(value==target):
            return index
    return -1 

numb=[33,22,44,55,66,77,88]
target=77
result=linear_search_enum(numb,target)

print(f"index of {target} is : {result}" )