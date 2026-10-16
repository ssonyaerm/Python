n = int(input())
summ = 0

for d in range(1, n):
    if n % d == 0:
        summ += d

print(summ)
