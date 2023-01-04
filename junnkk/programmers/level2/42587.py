# 프린터
# 리스트를 사용해서 문제를 풀었지만 deque를 사용한다면 효율성이 향상될 것이므로 다시 풀어보기


# from collections import deque 

def solution(priorities, location):
    answer = 0
    temp = [(i,p) for i, p in enumerate(priorities)]
    
    while(priorities):
        priorities_list = [(i,p) for i, p in temp]
        for (i, p) in priorities_list:
            # 만약 최댓값이 아니라면 뒤로 보내기
            if max(priorities)>p: 
                priorities.append(priorities.pop(0))
                temp.append(temp.pop(0))
            # 만약 최댓값이라면
            else:
                priorities.pop(0) 
                temp.pop(0)
                answer+=1
                if location == i:
                    priorities = []
                    break
        
    return answer