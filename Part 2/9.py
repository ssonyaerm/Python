s = input()
t = 0
for char in s:
    if char.isdigit():
        t += int(char)
print(t)
