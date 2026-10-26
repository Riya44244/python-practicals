# Practical 6: Swap the first n characters of two strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter n (number of characters to swap): "))

new1 = s2[:n] + s1[n:]
new2 = s1[:n] + s2[n:]

print("Before swap:", s1, "|", s2)
print("After swap :", new1, "|", new2)
