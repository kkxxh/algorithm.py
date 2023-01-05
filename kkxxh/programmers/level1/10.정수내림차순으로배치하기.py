def solution(n):
    answer = 0
    list_n = list(str(n))
    list_n.sort(reverse=True)
    answer = "".join(list_n)
    answer = int(answer)
    return answer