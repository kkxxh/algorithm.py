def solution(n):
    sum = 0
    for _ in range(1, len(str(n))+1):
        sum += n % 10
        n = n // 10
