# Practical 3: Pyramid and reverse pyramid of '*'
n = int(input("Enter number of rows: "))

print("Pyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("\nReverse pyramid:")
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
