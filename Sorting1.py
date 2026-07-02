set = [2,1,6,4,5,7,9]
def sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sort(set)
if binary_search(set,7) != -1:
    print("Target found after",binary_search(set,7),"comparisons.")
else:
    print("Target not found.")
