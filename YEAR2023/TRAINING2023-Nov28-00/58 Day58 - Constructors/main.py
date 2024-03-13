# class student:
#     grade = "Three"
#     name = "Default"
#     section = "Default"
#     roll = 0000
#
#     def info(self):
#         print(f"{self.name} is from class {self.grade}, {self.section} section and his Roll number is {self.roll}")
#
#
# rishav = student()
# rishav.name = "Rishav"
# rishav.section = "A"
# rishav.roll = 1
#
#
# rishav.info()





class three:
    def __init__(self, naming, grading, sectioned, rolled):
        print("Here the details of :")
        self.name = naming
        self.grade = grading
        self.section = sectioned
        self.roll = rolled

    def info(self):
        print(f"{self.name} is from class {self.grade}, {self.section} section and his Roll number is {self.roll}")


rishav = three("Rishav", "Three", "A", 1)
rishav.info()