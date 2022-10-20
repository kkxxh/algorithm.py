def solution(s):
    answer = True
    num_p = num_y = 0
    
    s = s.lower()
    for i in s:
        if i == 'p': num_p += 1
        if i == 'y' : num_y += 1
    
    if num_p != num_y:
        answer = False
    
    return answer