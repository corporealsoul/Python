side_one = int(input("Enter : "))
side_two = int(input("Enter : "))
side_three = int(input("Enter : "))

semi_perimeter = (side_one + side_two + side_three) / 2

triangle_area = (semi_perimeter * (semi_perimeter-side_one) * (semi_perimeter-side_two) * (semi_perimeter-side_three)) ** .5

print(triangle_area)