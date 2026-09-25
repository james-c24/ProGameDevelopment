def count_down(start):
    count = start
    if count != 0:
        output = "{}".format(count)
        print(output, end=" ")
        count -= 1
        return count_down(count)
    else:
        return ""
    
print(count_down(5))
