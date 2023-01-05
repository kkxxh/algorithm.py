def solution(s):
    #     s_list = [i for i in s]
    #     print(s_list)
    #     s_list.sort()
    #     print(s_list)

    #     return str(s_list).join('')
    return ''.join(reversed(sorted(s)))
