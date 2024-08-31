# while True:
#     value = int(input("Enter : "))
#
#     if value % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


# value = ""
# while value != "q":
#     value = int(input("Enter : "))
#     if value % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


# count = 1
#
# while count <= 10:
#     print(count)
#     count = count + 1



# count = 10
#
# while count >= 0:
#     print(count)
#     count = count - 1




# string_list = ["one","two","three","four","five","six", "seven", "eight", "nine", "ten","eleven","one","two","three","four","five"]
# while "one" in string_list:
#     string_list.remove("one")
# print(string_list)



# string_list = ["one","two","three","four","five","six", "seven", "eight", "nine", "ten","eleven","one","two","three","four","five"]
# while "eleven" in string_list:
#     break
#     print(string_list)
# print(string_list)


users = []
name = ""

while True:
    name = input("Name : ")
    if name == "exit" or name == "Exit":
        break
    elif name in users:
        continue
    else:
        users.append(name)
print(users)










