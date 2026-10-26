# Practical 11: Tuple operations
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
print("t1 =", t1)

# a. Print half of the values in one line and the other half in the next line
mid = len(t1) // 2
print("First half :", t1[:mid])
print("Second half:", t1[mid:])

# b. Another tuple with only the even numbers
evens = tuple(x for x in t1 if x % 2 == 0)
print("Even numbers tuple:", evens)

# c. Concatenate t2 with t1
t2 = (11, 13, 15)
t3 = t1 + t2
print("After concatenation:", t3)


# d. Return maximum and minimum value
def max_min(t):
    return max(t), min(t)


maximum, minimum = max_min(t3)
print("Maximum:", maximum)
print("Minimum:", minimum)
