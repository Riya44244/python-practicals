text = input("Enter the main string: ")
sub = input("Enter the substring to find: ")

indices = []
start = 0
while True:
    pos = text.find(sub, start)
    if pos == -1:
        break
    indices.append(pos)
    start = pos + 1

if indices:
    print("Substring found at indices:", indices)
else:
    print("Substring not found")
