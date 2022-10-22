def solution(array, commands):
    answer = []

    for command in commands:
        temp = sorted(array[command[0]-1:command[1]])
        answer.append(temp[command[2]-1])

    return answer

# 참고 1.
    #  return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# 참고 2. 두 번째 줄처럼 할당 가능
    # for command in commands:
    #     i,j,k = command
    #     answer.append(list(sorted(array[i-1:j]))[k-1])
