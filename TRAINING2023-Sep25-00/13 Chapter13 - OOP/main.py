# class student:
#     name = "Anup"
# class cars:
#     name = "Honda"
#
# student_class_variable = student()
# car_class_variable = cars()
#
# print(student_class_variable.name, car_class_variable.name)





# class student:
#     name = "Anup"
#
# student_1 = student()
# print(student_1.name)
#
# student_2 = student()
# print(student_2.name)





# class cars:
#     name = "Honda"
#     color = "Blue"
#     model = "Accord"
#     brand = "Honda"
#
# honda = cars()
# print(cars.name)
# print(cars.color)
# print(cars.model)
# print(cars.brand)





### CONSTRUCTOR
# class cars:
#
#     garage_name = "Anup's garage" # class attribute
#
#
#     print("Cars in my garage !")
#
#     ### Default constructor
#     def __init__(self):
#         pass
#
#     ### Parameterized constructor
#     def __init__(self, pass_name, pass_model, pass_color):
#         self.name = pass_name # object attribute
#         self.model = pass_model
#         self.color = pass_color
#
#     def welcome():
#         print("Welcome to my garage")
#
# bmw = cars("BMW", "Racing", "Green")
# print(bmw.name,"-", bmw.model,",", bmw.color)
#
# mercedes = cars("Mercedes", "Racing", "Yellow")s aw  w s
# print(cars.garage_name, "-", mercedes.garage_name, "-", mercedes.name,"-",  mercedes.model,",", mercedes.color)









# class student:
#
#     def __init__(self, name, math_marks, physics_marks, chemistry_marks):
#         self.name = name
#         self.math_marks = math_marks
#         self.physics_marks = physics_marks
#         self.chemistry_marks = chemistry_marks
#
#     def get_average(self):
#         average_marks = (math_marks + physics_marks + chemistry_marks) / 3
#         print(f"Hi, {name} , your average is {average_marks}")
#
# student_one = student("anup", 20, 30, 40)
# student_one.get_average()










# class Student:
#
#     def __init__(self, name, math_marks, physics_marks, chemistry_marks):
#         self.name = name
#         self.math_marks = math_marks
#         self.physics_marks = physics_marks
#         self.chemistry_marks = chemistry_marks
#
#     def calculate_average(self):
#         average_marks = (self.math_marks + self.physics_marks + self.chemistry_marks) / 3
#         return average_marks
#
# student_one = Student("Anup", 20, 30, 40)  # Capitalize name for consistency
# average = student_one.calculate_average()
# print(f"{student_one.name}'s calculated average is {average:.2f}")








# class student:
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def calculate_ave(self):
#         sum = 0
#         for loop in self.marks:
#             sum = sum + loop
#         print("Hi", self.name, "Your average is", sum/3)
#
#     # def hello(self):
#     #     print("Hello!")
#
#     @staticmethod
#     def hello():
#         print("Hello!")
#
#
# student_one = student("Anup", [20, 30, 40])
# student_one.calculate_ave()
# student_one.hello()









# class car:
#     def __init__(self):
#         self.accelator = False
#         self.brake = False
#         self.clutch = False
#     def start(self):
#         self.accelator = True
#         self.brake = True
#         self.clutch = True
#         print("Car started !")
# car1 = car()
# car1.start()







# class Account:
#     def __init__(self, account_namber, account_balance):
#         self.acc_no = account_namber
#         self.acc_bal = account_balance
#     def debit(self, ammount):
#         self.acc_bal = self.acc_bal - ammount
#         print("Rs.", ammount , "Was debited")
#         print("Balance left", self.left())
#
#     def credit(self, ammount):
#         self.acc_bal = self.acc_bal + ammount
#         print("Rs.", ammount , "Was credited ")
#         print("Balance left", self.left())
#
#     def left(self):
#         return self.acc_bal
#
# account_one = Account(0000, 10000000)
# account_one.debit(1000)
# account_one.credit(10000)







class Employee:
    def __init__(self, name, email, dept, salary):
         self.name = name
         self.email = email
         self.dept = dept
         self.salary = salary

    def show(self):
        print(f"Name : {self.name}")


employee_one = Employee("Name", "email@gmail.com", "Operation", "100000000")
print(employee_one.name, employee_one.dept)

employee_one.show()







