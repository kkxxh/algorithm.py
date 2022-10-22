def solution(n):
    n_list = []
    while n > 0:
        n_list.append(str(n % 3))
        n = n//3

    temp = ''.join(n_list)

    return int(temp, 3)
