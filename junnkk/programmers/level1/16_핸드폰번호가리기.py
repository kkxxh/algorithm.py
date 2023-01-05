def solution(phone_number):
    cnt = 0
    reversed_pn_list = list(reversed(phone_number))
    for i in range(len(reversed_pn_list)):
        if cnt >= 4:
            reversed_pn_list[i] = '*'
        cnt += 1
    reversed_pn_list.reverse()
    return str(''.join(reversed_pn_list))
