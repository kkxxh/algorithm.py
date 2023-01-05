def solution(board, moves):
    stack = []
    cnt = 0

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                if len(stack) != 0 and board[j][moves[i]-1] == stack[-1]:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break
    return cnt
