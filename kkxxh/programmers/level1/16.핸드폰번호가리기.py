def solution(phone_number):
    answer = ''
    len_pn = len(phone_number)
    for i in range(len_pn-4):
        answer+= '*'
    answer += phone_number[len_pn-4:]
    return answer