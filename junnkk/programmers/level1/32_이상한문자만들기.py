def solution(s):
    sl = list(map(str, s.split(' ')))

    for i in range(len(sl)):
        temp = list(sl[i])

        for j in range(len(temp)):
            if j % 2 == 0:
                temp[j] = temp[j].upper()
            else:
                temp[j] = temp[j].lower()
        sl[i] = ''.join(temp)

    return ' '.join(sl)
