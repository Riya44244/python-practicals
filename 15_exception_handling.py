# Practical 15: Exception handling for a name

class InvalidNameError(Exception):
    pass


def check_name(name):
    for ch in name:
        if not (ch.isalpha() or ch == " "):
            raise InvalidNameError("Name contains digits or special characters: '" + ch + "'")
    if name.strip() == "":
        raise InvalidNameError("Name cannot be empty")


try:
    name = input("Enter your name: ")
    check_name(name)
    print("Hello,", name)
except InvalidNameError as e:
    print("Error:", e)
