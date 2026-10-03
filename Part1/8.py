w = input().split()
a = w[0]
b = w[1]
c = w[2]
if len(a) > len(b) and len(a) > len(c):
    print(a)
elif len(b) > len(a) and len(b) > len(c):
    print(b)
else:
    print(c)
