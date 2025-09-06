gender = input()
match gender.upper():
    case "M":
        print("Male")
    case "F":
        print("Female")
    case _:
        print("Invalid")
