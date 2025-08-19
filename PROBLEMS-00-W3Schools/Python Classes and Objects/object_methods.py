class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def manual(self):
        print(f"This is {self.name} and his age is {self.age}")

first_person = person("Rishav", "36")

first_person.manual()
