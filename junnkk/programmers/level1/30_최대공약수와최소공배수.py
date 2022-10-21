import math


def solution(n, m):
    return [math.gcd(n, m), n*m/math.gcd(n, m)]

# math.lcm은 파이썬 3.9 이상에서만 사용 가능
    # return [math.gcd(n,m), math.lcm(n,m)]
