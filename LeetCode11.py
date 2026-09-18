string = "abcdefghijklmnopqrstuvwxyz"
def check_panagram(string):
    count = 0
    string = string.lower()
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(string)):
        if string[i] in alphabet:
            alphabet.remove(string[i])
            count += 1
    if count == 26:
        print("This is a panagram.")
    else:
        print("This is not a panagram.")

check_panagram(string)
