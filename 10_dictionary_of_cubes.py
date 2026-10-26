# Practical 10: Dictionary of cubes (keys 1 to 5)

def print_cubes():
    d = {}
    for i in range(1, 6):
        d[i] = i ** 3
    print(d)


print_cubes()
