class dog:
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
    def bark(self):
        print(f"Woof!, This is {self.breed} and I'm {self.age} Years old.")

fido = dog("Labra", 3)
buddy = dog("Golden", 5)

fido.bark()
