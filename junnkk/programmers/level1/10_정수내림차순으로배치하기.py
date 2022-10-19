def solution(n):
    # n_list = list(map(int,str(n)))
    # n_list.sort(reverse=True)
    # answer = ''.join(list(map(str,n_list)))
    # return int(answer)
    return int(''.join(sorted(str(n), reverse=True)))
