n = int(input())
adventurers = list(map(int ,input().split()))

adventurers.sort(reverse=True)

cnt = 0
idx = 0
while idx<n:
    idx = idx + adventurers[idx] 
    cnt+=1

print(cnt)