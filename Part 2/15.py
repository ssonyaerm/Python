n = int(input())
sumprofit = 0

for _ in range(n):
    inc, cost = map(int, input().split())
    profit = inc - cost
    if profit > 0:
        sumprofit += profit

print(sumprofit)
