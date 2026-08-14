def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

scores = [45,67,23,89,56]

print(linear_search(scores,23))
print(linear_search(scores,90))
