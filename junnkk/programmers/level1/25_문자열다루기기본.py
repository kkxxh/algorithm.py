def solution(s):

    sl = list(s)
    if len(s) != 4 and len(s) != 6:
        return False
    for i in sl:
        if i.isalpha():
            return False
    return True


# 실패 1 -> 문자열 길이 4 또는 6인 걸 확인 안함
#     for i in sl:
#         try:
#             int(i)
#         except:
#             return False
#     return True

# 실패 2 -> 문자열 길이 4 또는 6인 걸 확인 안함
    # nums = [0,1,2,3,4,5,6,7,8,9]
    # for i in sl:
    #     try:
    #         int(i) in nums
    #     except:
    #         return False
    # return True
