def solution(price, money, count):
    answer = -1
    sum = 0
    for i in range(count+1):
        sum += price * i
    
    answer = money- sum
    if answer >= 0 :
        answer = 0
    else : answer = -(answer)
    return answer