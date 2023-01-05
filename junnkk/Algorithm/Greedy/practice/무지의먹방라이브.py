## 우선순위큐로 우선 순위 낮은 거 제거..??
def solution(food_times, k):
    answer = 0
    
    dic = dict()
    for i, food_time in enumerate(food_times):
        dic[i] = food_time


    
    return answer



# # 실패 1 -> 효율성 + tc 20
# def solution(food_times, k):
#     answer = 0
    
#     idx = 0
#     length = len(food_times)

#     if k >= length * min(food_times):
#         k -= length * min(food_times)
#         food_times = [(food_times[i] - min(food_times) )for i in range(length)]
#     # print(food_times)
#     # print(k)
    
#     while k>=0:
#         if k == 0 and max(food_times) == 0:
#             return -1
#         if food_times[idx%length] != 0:
#             food_times[idx%length] -= 1
#             k -=1
#             answer = idx%length +1
#         idx +=1  
        
        
#     return answer