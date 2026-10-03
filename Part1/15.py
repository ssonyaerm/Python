a, b = map(int, input().split())
while b != 0:
    t = a
    a = b
    b = t % b  
print(a)
