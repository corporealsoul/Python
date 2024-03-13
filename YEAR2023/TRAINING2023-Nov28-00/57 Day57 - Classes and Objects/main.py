# class Person:
#     name = "Anup"
#     occupation = "DevOps"
#     networth = 5000
#
# profile = Person()
# print(profile.name, profile.occupation)




# class Person:
#     name = "Anup"
#     occupation = "DevOps Engineer"
#     networth = 5000
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
#
# profile = Person()
# profile.info()




class Person:
    name = "Default"
    occupation = "Default"
    networth = 0000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

anup = Person()
anup.name = "Anup Kumar Mondal"
anup.occupation = "DevOps"
anup.networth = 5000

rishav = Person()
rishav.name = "Rishav Mondal"
rishav.occupation = "Student"
rishav.networth = 500000

barnali = Person()
barnali.name = "Barnali Mondal"
barnali.occupation = "Home maker"
barnali.networth = 5000

anup.info()
rishav.info()
barnali.info()







