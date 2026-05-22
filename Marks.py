marks = [78,45,89,62,90,55,38,76]
below_60 = []
count = 0
for mark in marks:
    if mark > 75:
        count += 1
    else:
        continue
print(count,"students scored more than 75.")
for mark in marks:
    if mark < 60:
        below_60.append(mark)
print(below_60)
