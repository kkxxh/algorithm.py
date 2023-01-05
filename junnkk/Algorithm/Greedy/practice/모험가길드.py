# junnkk

# fail

# n = int(input())
# adventurers = list(map(int ,input().split()))

# adventurers.sort(reverse=True)

# cnt = 0
# idx = 0
# while idx<n:
#     idx = idx + adventurers[idx]
#     cnt+=1

# print(cnt)


n = int(input())
adventurers = list(map(int, input().split()))

adventurers.sort()


cnt = 0
member_num = 0

for adventurer in adventurers:
    member_num += 1
    if member_num >= adventurer:
        cnt += 1
        member_num = 0

print(cnt)
