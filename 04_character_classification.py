# Practical 4: Character classification
names = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
         "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly one character")
elif ch.isalpha():
    print(ch, "is a letter")
    if ch.isupper():
        print("It is uppercase")
    else:
        print("It is lowercase")
elif ch.isdigit():
    print(ch, "is a numeric digit")
    print("Name:", names[int(ch)])
else:
    print(ch, "is a special character")
