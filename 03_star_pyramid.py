n = int(input("Enter number of rows: "))

print("Half pyramid:")
for i in range(1, n + 1):
    print("*" * i)

print("\nFull pyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("\nInverted pyramid:")
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
