from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))

price = [0]*1000000


for i in range(n):
    comb = list(combinations(coins,i+1))
    for c in comb:
        price[sum(c)] += 1

for i in range(1,len(price)):
    if price[i] == 0:
        print(i)
        break