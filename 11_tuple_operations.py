t = (10, 20, 30, 40, 50, 20)
print("Tuple:", t)

print("Length:", len(t))
print("First element:", t[0])
print("Last element:", t[-1])
print("Slice t[1:4]:", t[1:4])
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Sum:", sum(t))

t2 = (60, 70)
print("Concatenation:", t + t2)
print("Repetition:", t2 * 2)
print("Is 30 in tuple?", 30 in t)

# Tuples cannot be changed, so convert to list to modify
lst = list(t)
lst.append(99)
print("Modified tuple:", tuple(lst))
