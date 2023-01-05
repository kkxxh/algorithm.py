def solution(s):
    # 최종
    return s.lower().count('p') == s.lower().count('y')
#     s = s.lower()
#     p_cnt = 0
#     y_cnt = 0

#     for i in list(s):
#         if i == 'p':
#             p_cnt +=1
#         elif i == 'y':
#             y_cnt +=1
#     # if y_cnt != p_cnt:
#     #      return False
#     # return True
#     return p_cnt == y_cnt
