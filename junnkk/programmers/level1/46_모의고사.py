def solution(answers):
    answer = []
    ans1 = [1, 2, 3, 4, 5] * (len(answers)//5+1)
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8+1)
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10+1)
    cnt1, cnt2, cnt3 = 0, 0, 0

    for i in range(len(answers)):
        if answers[i] == ans1[i]:
            cnt1 += 1
        if answers[i] == ans2[i]:
            cnt2 += 1
        if answers[i] == ans3[i]:
            cnt3 += 1

    max_cnt = max(cnt1, cnt2, cnt3)
    if max_cnt == cnt1:
        answer.append(1)
    if max_cnt == cnt2:
        answer.append(2)
    if max_cnt == cnt3:
        answer.append(3)

    return answer
