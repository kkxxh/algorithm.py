
def solution(n):
    answer = []
    str_n = str(n)
    for i in str_n:
        answer.append(int(i))
    answer = answer[::-1]
    return answer