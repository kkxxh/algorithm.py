n, m = map(int, input().split())
balls = list(map(int, input().split()))

d = [0]*(m+1)

for i in range(n):
    d[balls[i]] += 1
    

cnt = 0

for i in range(1,m+1):
    if d[i] !=0:
        for j in range(i+1,m+1):
            cnt += d[i]*d[j]

print(cnt)
