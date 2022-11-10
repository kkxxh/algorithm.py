N
money = [500,100,50,10]
answer = 0
for m in money:
    answer += N//m
    N %= m