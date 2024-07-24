record = []

for loop in range (1, 21):
    if loop % 3 == 0 and loop % 5 == 0:
        record.append("fizzbuzz")
    elif loop % 3 == 0:
        record.append("fizz")
    elif loop % 5 == 0:
        record.append("buzz")
    else:
        record.append(loop)

print(record)