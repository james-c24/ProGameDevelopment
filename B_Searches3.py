def binary_search(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

products = [1021,2045,3050,4078,5099,6123,7100,8205]
code = int(input("What is the product code of the product you are seraching for? "))
if binary_search(products,code):
    print("Product available.")
else:
    print("Product not available.")
