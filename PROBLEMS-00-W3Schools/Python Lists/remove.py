number_list = [1, 2, "three", 4, 5, 6, 7, 8, 9, 10]
print("List : ", number_list, "which is ", type(number_list))

number_list.insert(0,"Zero")
print("List : ", number_list, "which is ", type(number_list))

number_list.remove(10)
print("List : ", number_list, "which is ", type(number_list))

number_list.pop()
print("List : ", number_list, "which is ", type(number_list))

del number_list[3]
print("List : ", number_list, "which is ", type(number_list))

number_list.clear()
print("List : ", number_list, "which is ", type(number_list))

number_list = list((1, 2, "three", 4, 5, 6, 7, 8, 9, 10))
print("List : ", number_list, "which is ", type(number_list))

