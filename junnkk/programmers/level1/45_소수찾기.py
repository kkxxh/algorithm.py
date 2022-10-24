def solution(n):
    num = [0]*(n+1)
    num[1]=1
    cnt = 0
    
    for i in range(1,n+1):
        if num[i] ==0:
            for j in range(i,n+1,i):
                num[j] = 1
            cnt +=1
    
    return cnt