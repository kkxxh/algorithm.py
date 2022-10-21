def solution(price, money, count):
    sum = 0
    for i in range(count):
        sum += (i+1) * price

    return (sum - money) if sum > money else 0
