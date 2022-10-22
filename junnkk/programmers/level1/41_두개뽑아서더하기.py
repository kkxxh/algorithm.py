from itertools import combinations


def solution(numbers):
    combination = list(combinations(numbers, 2))
    answer = sorted({sum(c) for c in combination})

    return answer
