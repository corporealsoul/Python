def use_finally():
    try:
        listing = [1,2,3,4,5]
        your_choice = int(input("Enter choice : "))
        print(listing[your_choice])
        return 1
    except:
        print("Some error !")
        return 0

    finally:
        print("Always executed")

execute = use_finally()
print(execute)