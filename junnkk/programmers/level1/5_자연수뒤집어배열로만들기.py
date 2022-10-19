def solution(n):
    answer = []

    for i in range(len(str(n))):
        answer.append(n % 10)
        n = n//10
    return answer
