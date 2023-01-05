# 오류

def solution(s):
    answer = []
    s_list = list(map(list,s.split()))
    
    for i in s_list :
        for j in range(len(i)) :
            if j % 2 == 0:
                i[j] = i[j].upper()
            else :
                i[j] = i[j].lower()
        x = "".join(i)
        answer.append(x)
        
    answer = " ".join(answer)
    return answer