# with open("user.txt", "a") as file:
#     file.write(" by Anup")

# with open("user.txt", "r") as file:
#     content = file.read()
# print(content)


with open("user.txt", "r") as file:
    content = file.readlines()

for loop in content:
    print(loop)


