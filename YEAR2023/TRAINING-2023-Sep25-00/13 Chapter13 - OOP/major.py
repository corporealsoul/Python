# class Account:
#     def __init__(self, account_number, account_balance, account_password):
#         self.acc_no = account_number
#         self.acc_bal = account_balance
#         self.__acc_pass = account_password
#     def reset_password(self):
#         print(self.__acc_pass)
#
# account_one = Account("00000", "400000", "abcd00000")
# print(account_one.acc_no)
# print(account_one.acc_bal)
# # print(account_one.acc_pass)




# class Car:
#     @staticmethod
#     def start():
#         print("Started")
#
#     @staticmethod
#     def stop():
#         print("Stopped")
#
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name
#
# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type
#
# car_one = Fortuner("Disel")
# print(car_one.start())







# class A:
#     varA = "Welcome to class A"
#
# class B:
#     varB = "Welcome to class B"
#
# class C(A, B):
#     varC = "Welcome to class C"
#
#
# c_object = C()
#
# print(c_object.varA)
# print(c_object.varB)
# print(c_object.varC)











# class Car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("Started")
#     @staticmethod
#     def stop():
#         print("Stopped")
# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()
#
# car_one = ToyotaCar("Fortuner", "Electric")
# print(car_one.type)









# class Person:
#     name = "Anonymous"
#
#     def changename(self, name):
#         # self.name = name
#         # Person.name = name
#         self.__class__.name = "Rishav"
#
# persion_one = Person()
# persion_one.changename("Anup")
# print(persion_one.name)
# print(Person.name)




class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

        #percentage

student_one = Student(89, 92,96)
print(student_one.percentage)

student_one.phy =
















