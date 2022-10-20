def solution(n):
    answer = -1
    num = 0
    if n**(0.5) == int(n**(0.5)):
        num = int(n**(0.5))
        answer = (num+1)**2
    return answer