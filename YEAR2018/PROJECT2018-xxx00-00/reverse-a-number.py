def reverse_number(number):
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number //= 10
    return reversed_number

number = int(input("Enter number : "))

reversed_number = reverse_number(number)

print("The reverse number = ", reversed_number)


