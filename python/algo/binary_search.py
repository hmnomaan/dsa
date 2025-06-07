# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1  # Not found

# # Example (List must be sorted)
# sorted_nums = [1, 2,8, 3, 4, 7, 9]
# print(binary_search(sorted_nums, 7))  # Output: 4

#Practice 1

def binary_Search(arr,target):
    left,right=0, len(arr)-1
    
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]< target:
            left= mid+1
        else:
            right= mid-1
    return -1

sorted_arr=[1,2,3,4,5,6,7,8,11,12]
result=binary_Search(sorted_arr,8)

print(f"index found to the target value:{result}")

#Practice 2

def b_s(arr,tg):
    l,r=0,len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==tg:
            return mid
        elif arr[mid]<tg:
            l=mid+1
        else:
            r=mid-1     
    return -1

n_arr=[2,3,4,5,6,7,8]
result=b_s(n_arr,7)

print(f"index of the number: {result}")
    
    
    

#Practice 3


def binary_search(array,target):
    high,low=0,len(array)-1
    while low>=high:
        mid=(low+high)//2
        if(array[mid]==target):
            return mid
        elif(array[mid]>target):
            low=mid-1
        else:
            high=mid+1
            
    return -1

nums=[1,2,3,4,5,6,7,8,9]
result=binary_search(nums,9)

print(f"target number is in {result}")
            
            
            
    
    
