def binary_search(arr,target):
    left = 0
    right = len(arr) - 1


    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

fruits = ["apple","banana","grape","mango","orange"]
result = binary_search(fruits,"mango")
if result == -1:
    print("Result was not found.")
else:
    print("Result was found at index",result)
