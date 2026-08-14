def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

jerseys = [7,10,23,11,5]

print(linear_search(jerseys,23))
print(linear_search(jerseys,99))
