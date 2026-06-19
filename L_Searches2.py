def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [2001,2005,2010,2020,2035,2050]
result = linear_search(numbers,2020)

if result == -1:
    print("Employee ID was not found.")
else:
    print("Employee ID was found at position",result)
