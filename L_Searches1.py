def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [101,105,110,115,120]
result = linear_search(numbers,115)

if result == -1:
    print("Result was not found.")
else:
    print("Result was found at index",result)
