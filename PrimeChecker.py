while True:
    number = int(input("Type your number here: "))
    divisors = 0
    for i in range(1,int(number)+1):
        if number % i == 0:
            divisors += 1
        else:
            pass
    if int(number) == 0 or int(number) == 1:
        print("This number is neither prime nor composite.")
        print()
    elif divisors == 2:
        print("This number is prime.")
        print()
    else:
        print("This number is composite.")
        print()
