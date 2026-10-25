s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

n = 2  # number of characters to swap
new1 = s2[:n] + s1[n:]
new2 = s1[:n] + s2[n:]

print("Before swap:", s1, s2)
print("After swapping first", n, "characters:", new1, new2)
