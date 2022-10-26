def solution(dartResult):

    temp = []

    for i, d in enumerate(dartResult):
        if d.isdigit():
            if i != 0 and dartResult[i-1].isdigit():
                temp[-1] = int(dartResult[i-1:i+1])
            else:
                temp.append(int(d))
        elif d.isalpha():
            if d == "D":
                temp[-1] = temp[-1]**2
            elif d == "T":
                temp[-1] = temp[-1]**3
        else:
            if d == "*":
                if len(temp) != 1:
                    temp[-1] = temp[-1]*2
                    temp[-2] = temp[-2]*2
                else:
                    temp[-1] = temp[-1]*2
            else:
                temp[-1] = temp[-1]*(-1)

    return sum(temp)
