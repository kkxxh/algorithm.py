n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()

answer = (num[-1]*k+num[-2])*(m//(k+1)) + num[-1]*(m % (k+1))

print(answer)
