# junnkk
n,m = map(int,input().split())
num_list = []

max = 0

for i in range(n):
    num_list.append(list(map(int,input().split())))
    num_list[i].sort()
    if max < num_list[i][0]:
        max = num_list[i][0]

print(max)



    
# min() 함수 이용
n,m = map(int,input().split())
result = 0

for i in range(n):
    num_list = list(map(int,input().split()))
    min_value = min(num_list)
    result = max(result, min_value)
    
print(result)




# 2중 반복문 구조 이용
n,m = map(int,input().split())
result = 0

for i in range(n):
    num_list = list(map(int,input().split()))
    min_value = 10001
    for num in num_list:
        min_value = min(min_value, num)
    result = max(result, min_value)
    
print(result)