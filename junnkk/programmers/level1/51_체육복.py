def solution(n, lost, reserve):

    students = [1]*(n+2)
    cnt = 0

    for l in lost:
        students[l] -= 1

    for r in reserve:
        students[r] += 1

    for i in range(1, len(students)-1):
        if students[i] == 1:
            cnt += 1
        elif students[i] == 2:
            if students[i-1] == 0:
                students[i-1] += 1
                students[i] -= 1
                cnt += 1
            elif students[i+1] == 0:
                students[i+1] += 1
                students[i] -= 1
            cnt += 1

    return cnt
