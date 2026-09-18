arr1 = [2,4,7,10]
arr2 = [2,3]

arr1_length = len(arr1)
arr2_length = len(arr2)

for i in range(len(arr2)):
    arr1.append(arr2[i])

for i in range(len(arr1)):
    for j in range(len(arr1)-1):
        if arr1[j] > arr1[j+1]:
            temp = arr1[j]
            arr1[j] = arr1[j+1]
            arr1[j+1] = temp

new_arr1 = []
new_arr2 = []

for i in range(arr1_length):
    new_arr1.append(arr1[i])

for i in range(arr2_length):
    new_arr2.append(arr1[i+arr1_length])

print(new_arr1)
print(new_arr2)
print(arr1)
