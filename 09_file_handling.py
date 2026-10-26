# Practical 9: File handling
# Keep 'sample.txt' in the same folder as this program.
filename = input("Enter file name (e.g. sample.txt): ")

with open(filename, "r") as f:
    content = f.read()

with open(filename, "r") as f:
    lines = f.readlines()

words = content.split()

# a. Total characters, words and lines
print("Total characters:", len(content))
print("Total words:", len(words))
print("Total lines:", len(lines))

# b. Frequency of each character (using a dictionary)
freq = {}
for ch in content:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("Character frequency:", freq)

# c. Words in reverse order
print("Words in reverse order:")
print(" ".join(words[::-1]))

# d. Even lines to File1, odd lines to File2
with open("File1.txt", "w") as f1, open("File2.txt", "w") as f2:
    for i in range(len(lines)):
        line_no = i + 1
        if line_no % 2 == 0:
            f1.write(lines[i])
        else:
            f2.write(lines[i])
print("Even lines copied to File1.txt, odd lines copied to File2.txt")
