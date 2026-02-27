input = input("Input a string to check if it is a tautogram: ")

str = []
for char in input:
    str.append(char)

tautogram = True

for i in range(len(str)):
    if str[i] == ' ':
        if str[i+1] != str[0]:
            tautogram = False
        else:
            continue
    else:
        continue
        
if tautogram == True:
    print("This is a tautogram.")
if tautogram == False:
    print("This is not a tautogram.")
