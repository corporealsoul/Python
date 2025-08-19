class person:
    def __init__(selfie, name, age):
        selfie.name = name
        selfie.age = age

    def manual(selfie):
        print(f"This is {selfie.name} and his age is {selfie.age}")

first_person = person("Rishav", "36")

first_person.age = 40

first_person.manual()
