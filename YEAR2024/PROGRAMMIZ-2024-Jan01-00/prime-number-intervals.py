number_one = int(input("Enter : "))

for loop in range (2, number_one):
    for loop_inner in range (2, loop):
        if (loop % loop_inner) == 0:
            break
    else:
        print(loop)