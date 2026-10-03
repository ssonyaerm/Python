с = 0
for i in range(3):
    word, n = input().split()
    с += len(word) * int(n)
print(с)
