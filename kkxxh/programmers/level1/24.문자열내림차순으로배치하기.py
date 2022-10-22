def solution(s):
    answer = ''
    arr_s = []
    for i in s :
        arr_s.append(i)
    arr_s.sort(reverse=True)
    answer = "".join(arr_s)
    return answer