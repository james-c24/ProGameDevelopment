str = input("Input a string to check if it is a palindrome: ")

chars = []
rev = []

for char in str:
    chars.append(char)

for i in range(len(chars)):
    rev.append(chars[len(chars)-1-i])

if chars == rev:
    print("This is a palindrome.")
if chars != rev:
    print("This is not a palindrome.")
