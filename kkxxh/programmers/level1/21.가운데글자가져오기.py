def solution(s):
    answer = ''
    s_len = len(s)
    if s_len %2 ==0 :
        answer = s[int(s_len/2)-1]+s[int(s_len/2)]
    else :
        answer = s[int(s_len/2)]
    return answer