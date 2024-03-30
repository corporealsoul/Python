number_one = int(input("Enter : "))

flag = 1

for loop in range (2, number_one - 1):
    if number_one % loop == 0:
        flag = 0
        break

if flag == 0:
    print("Not Prime")
else:
    print("Prime")