def solution(sizes):
    max_w, max_h = 0, 0

    for i in range(len(sizes)):
        sizes[i].sort()
        max_w = max(max_w, sizes[i][0])
        max_h = max(max_h, sizes[i][1])

    return max_w*max_h

# 참고할 풀이
# return max(max(x) for x in sizes) * max(min(x) for x in sizes)
