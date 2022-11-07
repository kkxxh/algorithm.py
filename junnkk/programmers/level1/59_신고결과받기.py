def solution(id_list, report, k):
    d = {}
    cnt = {}
    for id in id_list:
        d[id] = []
        cnt[id] = 0

    report = list(set(report))

    for i in range(len(report)):
        a, b = map(str, report[i].split())
        d[a].append(b)
        cnt[b] += 1

    answer = [0]*len(id_list)

    for i, id in enumerate(id_list):
        for j in range(len(d[id])):
            if cnt[d[id][j]] >= k:
                answer[i] += 1
    return answer
