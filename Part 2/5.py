import math
n, m, c, k = map(int, input().split())

s = n * m

if k >= s:
    print("0")
else:
    s = s - k
    pac = math.ceil(s / 200) 
    res = pac * c
    print (res)
