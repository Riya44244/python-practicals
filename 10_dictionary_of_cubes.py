n = int(input("Enter a number: "))

cubes = {}
for i in range(1, n + 1):
    cubes[i] = i ** 3

print("Dictionary of cubes:", cubes)

# Same thing using dictionary comprehension
cubes2 = {i: i ** 3 for i in range(1, n + 1)}
print("Using comprehension:", cubes2)

print("Keys:", list(cubes.keys()))
print("Values:", list(cubes.values()))
