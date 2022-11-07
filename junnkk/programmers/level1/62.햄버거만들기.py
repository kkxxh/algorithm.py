def solution(ingredient):

    answer = 0
    stack = []

    for ingre in ingredient:
        stack.append(ingre)
        if len(stack) >= 4:
            if stack[-4:] == [1, 2, 3, 1]:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1

    return answer


# 실패 1 -> 시간 초과
# def solution(ingredient):

#     answer = 0
#     ingredient = ''.join(map(str,ingredient))


#     while '1231' in ingredient:
#         ingredient = ingredient.replace('1231','',1)
#         answer += 1

#     return answer
