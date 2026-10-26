# Practical 8: Cubes of even integers from a list (may have other types)
lst = [1, 2, "hello", 4, 5.5, 6, 7, 8, "10", 10, 3.0, True]
print("Input list:", lst)

# a. Using 'for' loop
cubes1 = []
for x in lst:
    if type(x) == int and x % 2 == 0:
        cubes1.append(x ** 3)
print("Using for loop:", cubes1)

# b. Using list comprehension
cubes2 = [x ** 3 for x in lst if type(x) == int and x % 2 == 0]
print("Using list comprehension:", cubes2)
