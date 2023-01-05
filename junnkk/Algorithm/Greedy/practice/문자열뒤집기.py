import math

s = input()

cnt = 0

if len(s) >1:
    for i in range(1,len(s)):
        if s[i-1] != s[i]:
            cnt +=1

print(math.ceil(cnt/2))
    