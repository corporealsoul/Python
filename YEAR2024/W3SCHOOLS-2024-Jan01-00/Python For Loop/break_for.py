character_string = "Pyhton For LOOP"
print("List : ", character_string, "which is ", type(character_string))

for loop in character_string:
    if loop == " ":
        break
    print(loop)
