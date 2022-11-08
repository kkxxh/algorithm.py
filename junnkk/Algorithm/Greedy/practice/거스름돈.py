n = int(input())

coin = [500, 100, 50, 10]
answer = 0

for c in coin:
    answer += n//c
    n = n % c

print(answer)
