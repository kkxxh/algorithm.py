def solution(X, Y):
    temp = []
    d_x = [0]*10
    
    for i in range(len(X)):
        d_x[int(X[i])]+=1
    
    for i in range(len(Y)):
        if d_x[int(Y[i])] !=0:
            d_x[int(Y[i])] -= 1
            temp.append(int(Y[i]))
            
    if len(temp) == 0:
        return "-1"
    if sum(temp) == 0:
        return "0"
    
    return ''.join(map(str,sorted(temp, reverse = True)))
    
# 실패1. (시간 초과)    
#     x_list = sorted([i for i in X])
#     y_list = sorted([i for i in Y])
#     temp = []

#     for x in x_list:
#         for i in range(len(y_list)):
#             if x == y_list[i]:
#                 temp.append(int(x))
#                 y_list = y_list[i+1:]
#                 break
#             if x<y_list[i]:
#                 break
                
#     if len(temp) == 0:
#         return "-1"
#     if sum(temp) == 0:
#         return "0"
    
#     return ''.join(map(str,sorted(temp, reverse = True)))
        