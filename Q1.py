def binary_check(string):
    for i in range(len(string)):
        if string[i] != "0" and string[i] != "1":
            return False
    return True

string = input("Input string to check if it is binary: ")
print(binary_check(string))
