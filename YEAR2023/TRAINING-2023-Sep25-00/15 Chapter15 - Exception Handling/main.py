# print(10*2)
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Trying 0 ?")
# print(10+2)
# print(10-2)


with open("user.txt", "r") as file:
    content = file.readlines()

for loop in content:
    print(loop)