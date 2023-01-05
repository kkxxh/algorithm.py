from itertools import combinations

def solution(number):
    answer = 0
    combination = list(combinations(number, 3))
    for c in combination:
        if sum(c) == 0:
            answer+=1
    return answer