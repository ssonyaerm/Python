num = input().split()
res = []
for num_str in num:
    n = int(num_str)
    for d in range(2, n + 1):
        if n % d == 0:
            res.append(str(d))
            break
print(' '.join(res))
