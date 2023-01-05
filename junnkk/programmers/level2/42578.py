# 위장
# 딕셔너리 리스트 초기화 방법 알기

def solution(clothes):

    answer = 1

    d = {clothes[i][1]: [] for i in range(len(clothes))}

    for i in range(len(clothes)):
        d[clothes[i][1]] += [clothes[i][0]]

    for key in d:
        answer *= (len(d[key])+1)

    return answer - 1
