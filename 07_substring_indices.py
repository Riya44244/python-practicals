# Practical 7: Indices of all occurrences of a substring

def find_indices(main, sub):
    indices = []
    if sub == "":
        return -1
    start = 0
    while True:
        pos = main.find(sub, start)
        if pos == -1:
            break
        indices.append(pos)
        start = pos + 1
    if len(indices) == 0:
        return -1
    return indices


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(find_indices(s1, s2))
