number_list = [1, 2, "three", 4, 5, 6, 7, 8, 9, 10]
print("List : ", number_list, "which is ", type(number_list))

if "three" in number_list:
    print("Present")

for loop in number_list:
    print(loop)
    if loop == "three":
        print(loop, "Present")