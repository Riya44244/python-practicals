def get_name():
    name = input("Enter your name: ").strip()
    if name == "":
        raise ValueError("Name cannot be empty")
    if not name.replace(" ", "").isalpha():
        raise ValueError("Name must contain only letters")
    return name


try:
    name = get_name()
    print("Hello,", name)
except ValueError as e:
    print("Error:", e)
finally:
    print("Program finished.")
