## Can't take strings
# which = input("Enter the number: ")
# print(f"Multiplication table of {which} is: ")
# for loop in range(1, 11):
#     print(f"{int(which)} X {loop} = {int(which)*loop}")
#
# print("End of program !")



# which = input("Enter the number: ")
# print(f"Multiplication table of {which} is: ")
# try:
#     for loop in range(1, 11):
#         print(f"{int(which)} X {loop} = {int(which) * loop}")
# except Exception as e:
#     print(e)
#
# print("End of program !")



try:
    numbers_input = int(input("Enter integer : "))
except ValueError:
    print("Not and Integer !")



