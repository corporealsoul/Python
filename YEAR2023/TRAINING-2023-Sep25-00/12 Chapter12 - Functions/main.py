# def function_declation(name, id = None):
#     print(f"Functions by {name}, id : {id}")
#
# function_declation("Anup", 21)
# function_declation("Rishav", 20)
# function_declation("Barnali")



# def function_declation(name, id = None, *hobbies):
#     print(f"Functions by {name}, id : {id}, hobbies : {hobbies}")
#
# function_declation("Anup", 21, "Sketching", "Cricket", "Computer")
# function_declation("Rishav", 20, "Football", "Karate")
# function_declation("Barnali", 22, "Cooking")


# user_book = []
# def user_details(name, *details):
#     user_data = [name] + list(details)
#     user_book.append(user_data)
#
# user_details("Anup", 21, "Sketching", "Cricket", "Computer")
# user_details("Rishav", 21, "Sketching", "Cricket", "Computer")
# print(user_book)



# def user_details(name, **user_details):
#     print(f"Name - {name}")
#     for key, value in user_details.items():
#         print(f"{name} : {value}")
#
# user_details("Ravi", age = "18")
# user_details("Narendra", age = "56")



def addition (num1, num2):
    return num1 + num2

result = addition(2, 3)
print(result)



