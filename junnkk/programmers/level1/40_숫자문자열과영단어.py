def solution(s):
    str_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
               'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    answer = []
    temp = ''

    for i in s:
        if i.isdigit():
            answer.append(i)
        else:
            temp += i
            if temp in str_num:
                answer.append(str_num[temp])
                temp = ''

    return int(''.join(map(str, answer)))


# 참고 1.
# def solution(s):
#     words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

#     for i in range(len(words)):
#         s = s.replace(words[i], str(i))

#     return int(s)
