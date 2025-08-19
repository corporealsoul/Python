# number_one = int(input("Enter : "))
# number_two = int(input("Enter : "))
#
# bowl = number_one
#
# number_one_actual = number_one
# number_two_actual = number_two
#
# number_one = number_two
# number_two = bowl
#
# print(f"Before swap {number_one} was : {number_one_actual}")
# print(f"Before swap {number_two} was : {number_two_actual}")






# number_one = int(input("Enter : ")) # 4
# number_two = int(input("Enter : ")) # 5
#c
# number_one_actual = number_one
# number_two_actual = number_two
#
# number_one = number_one + number_two # 9
#
# number_two = number_one - number_two # 9 - 4 = 5
# number_one = number_one - number_two
#
# print(f"Before swap {number_one} was : {number_one_actual}")
# print(f"Before swap {number_two} was : {number_two_actual}")







number_one = int(input("Enter : ")) # 4
number_two = int(input("Enter : ")) # 5

number_one_actual = number_one
number_two_actual = number_two

number_one , number_two = number_two , number_one

print(f"Before swap {number_one} was : {number_one_actual}")
print(f"Before swap {number_two} was : {number_two_actual}")
