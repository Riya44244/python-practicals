ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly one character")
elif ch.isalpha():
    if ch.lower() in "aeiou":
        kind = "Vowel"
    else:
        kind = "Consonant"
    case = "Uppercase" if ch.isupper() else "Lowercase"
    print("It is an alphabet:", kind, "-", case)
elif ch.isdigit():
    print("It is a digit")
elif ch.isspace():
    print("It is a whitespace")
else:
    print("It is a special character")
