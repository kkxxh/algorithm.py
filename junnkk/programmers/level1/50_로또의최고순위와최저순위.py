def solution(lottos, win_nums):

    same = 0
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    win_nums.sort()

    for i in win_nums:
        if i in lottos:
            same += 1

    max_same = same + lottos.count(0)

    return [rank[max_same], rank[same]]
