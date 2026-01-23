while True:
    number = input("Type your number here: ")
    if float(number) % 1 == 0:
        if float(number) % 2 == 0:
            print("This number is even.")
            break
        else:
            print("This number is odd.")
            break
    else:
        print("This is a decimal. Please try again.")
