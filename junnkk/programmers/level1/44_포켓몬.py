def solution(nums):
    temp = []
    
    for n in nums:
        if len(temp) == len(nums)//2:
            break
        if n not in temp:
            temp.append(n)

    return len(temp)

# 참고1
# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))
