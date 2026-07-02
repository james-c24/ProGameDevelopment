def search_player(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return "Player selected."
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "Player not selected."

shirts = [1,2,4,5,7,8,10,11,14,16,18]
shirt = int(input("Which player are you searching for? "))
print(search_player(shirts,shirt))
