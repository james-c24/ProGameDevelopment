def fibonacci(n,a=0,b=1):
    count = n
    if count != 0:
        print(a,end=" ")
        count -= 1
        return fibonacci(count,b,a+b)
    else:
        return ""
print(fibonacci(998))
