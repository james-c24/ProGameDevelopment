fares = [250,180,450,320,150,450,275,600,210]

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        else:
            continue
    return -1

def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            else:
                continue

def top_three(arr):
    print("The top three fares are: {}, {} and {}.".format(arr[0],arr[1],arr[2]) )

def find_fare(arr):
    target = int(input("Which fare are you looking for? "))
    if target in arr:
        print("The fare {} is found at the index {}.".format(target,linear_search(arr,target)))

def top_three_sum(arr):
    print("The sum of the top three fares is {}.".format(arr[0]+arr[1]+arr[2]))

def over_limit(arr,limit):
    count = 0
    for i in range(len(arr)):
        if arr[i] > limit:
            count += 1
        else:
            continue
    print("{} people paid over {}.".format(count,limit))

sort(fares)
print(fares)
top_three(fares)
find_fare(fares)
top_three_sum(fares)
over_limit(fares,300)
