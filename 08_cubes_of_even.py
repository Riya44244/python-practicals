n = int(input("Enter the upper limit: "))

print("Cubes of even integers from 1 to", n)
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "->", i ** 3)

# Same thing using a list
cubes = [i ** 3 for i in range(1, n + 1) if i % 2 == 0]
print("List of cubes:", cubes)
