n, a = map(int, input().split())
c = 0
x = a
while c < n:
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
        print(x, end=' ')
        c += 1
    x += 1
