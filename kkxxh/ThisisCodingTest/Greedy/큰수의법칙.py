# N개의 자연수, 입력으로 주어지는 K는 M보다 작거나 같다
N,M,K = map(int,input().split())

num = list(map(int,input().split()))
num.sort(reverse=True)

answer = 0

answer = (num[0]*K +num[1])*M//(K+1)+num[0]*M%(K+1)



