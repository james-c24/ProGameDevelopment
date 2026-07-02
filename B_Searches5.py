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

dino_ids = [15,29,37,42,56,63,78,84,99]
dino = int(input("Which dinosaur are you searching for? "))
if binary_search(dino_ids,dino) != -1:
    print("Warning! Dinosaur located! Dinosaur found after",binary_search(dino_ids,dino),"comparisons.")
else:
    print("Area is safe.")
