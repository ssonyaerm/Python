s = input()
w = s.split()
nw = []
for word in w:
    nw.append(word[::-1])
res = ' '.join(nw)
print(res)
