def solution(n):
    #     x = 0
    #     for i in range(2,n):
    #         if n%i == 1:
    #             x = i
    #             break

    #     return x

    return [x for x in range(1, n+1) if n % x == 1][0]
