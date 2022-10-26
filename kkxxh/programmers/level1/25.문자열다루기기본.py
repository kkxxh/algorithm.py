def solution(s):
    answer = True
    
    number = ["1","2","3","4","5","6","7","8","9","0"]
    if len(s) != 4 and len(s) != 6:
        answer = False
    for i in s:
            if i not in number:
                answer = False
    return answer