from itertools import combinations


def solution(nums):
    cnt = 0
    combination = list(combinations(nums, 3))

    for c in combination:
        for i in range(2, sum(c)):
            if sum(c) % i == 0:
                break
            if i == sum(c)-1:  # 이 부분을 참고1과 같이 for-else문으로 대체 가능
                cnt += 1

    return cnt

# 참고1 -> for-else 문
# def solution(nums):
#     from itertools import combinations as cb
#     answer = 0
#     for a in cb(nums, 3):
#         cand = sum(a)
#         for j in range(2, cand):
#             if cand%j==0:
#                 break
#         else:
#             answer += 1
#     return answer
