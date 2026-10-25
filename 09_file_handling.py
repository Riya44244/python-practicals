filename = "sample.txt"

# Write to file
with open(filename, "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("Python file handling practical.\n")
print("File written.")

# Append to file
with open(filename, "a") as f:
    f.write("This line was appended.\n")
print("Line appended.")

# Read the whole file
print("\nFile contents:")
with open(filename, "r") as f:
    print(f.read())

# Read line by line
print("Line by line:")
with open(filename, "r") as f:
    for number, line in enumerate(f, start=1):
        print(number, ":", line.strip())
