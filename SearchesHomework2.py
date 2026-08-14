def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

roll_numbers = [101,105,110,115,120]
x = int(input("Enter the number to search: "))
result = linear_search(roll_numbers,x)

if result == -1:
    print("Result was not found.")
else:
    print("Result was found at index",result)

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

employee_ids = [1001,1005,1010,1015,1020,1025,1030]
y = int(input("Enter the number to search: "))
result = binary_search(employee_ids,y)

if result == -1:
    print("Result was not found.")
else:
    print("Result was found at index",result)
