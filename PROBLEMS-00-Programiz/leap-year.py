number_one = int(input("Enter : "))

if number_one % 100 == 0:
    if number_one % 400 == 0:
        print("Leap Year !!")
    else:
        print("Not a Leap Year !!")
elif number_one % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# number_one = int(input("Enter : "))
# if (number_one % 100 == 0) and (number_one % 400 == 0):
#     print("Leap Year !!")
# elif (number_one % 4 == 0) and (number_one % 100 != 0):
#     print("Leap Year !!")
# else:
#     print("Not a Leap Year")

