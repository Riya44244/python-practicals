# Practical 5: Operations on a string
s = input("Enter a string: ")

# a. Frequency of a character
ch = input("Enter a character to find its frequency: ")
count = 0
for c in s:
    if c == ch:
        count += 1
print("Frequency of", ch, "=", count)

# b. Replace a character by another
old = input("Enter the character to replace: ")
new = input("Enter the new character: ")
print("After replacing:", s.replace(old, new))

# c. Remove first occurrence of a character
rem = input("Enter a character to remove its first occurrence: ")
pos = s.find(rem)
if pos == -1:
    print("Character not found")
else:
    print("After removing first occurrence:", s[:pos] + s[pos + 1:])

# d. Remove all occurrences of a character
rem_all = input("Enter a character to remove all its occurrences: ")
result = ""
for c in s:
    if c != rem_all:
        result += c
print("After removing all occurrences:", result)
