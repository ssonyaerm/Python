import math
n, m, k = map(int, input().split())
s = n * m
box = math.ceil(s / k)
print (box)
