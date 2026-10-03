a, b, c = map(int, input().split())
left = min(a, b)
right = max(a, b)
if c < left:
    print(left - c)
elif c > right:
    print(c - right)
else:
    print(0)
