import math
x, y = map(float, input().split())

l = math.ceil(x)
r = math.floor(y)

if l <= r:
    cnt = r - l + 1
else:
    cnt = 0
print(cnt)
