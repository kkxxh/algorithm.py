def solution(left, right):
    answer = 0
    div_list = []
    
    for num in range(left, right+1):
        for i in range(1,num+1):
            if num % i == 0:
                div_list.append(i)
        if len(div_list) % 2 == 0 : 
            answer += num
        else : 
            answer -= num
        div_list = []

    return answer