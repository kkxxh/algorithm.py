# junnkk
n = int(input())

# direction = list(map(str, input().split()))
direction = input().split()

nx, ny = 1, 1

for d in direction:
    if d == 'L' and ny != 1:
        ny -= 1
    elif d == 'R' and ny != n:
        ny += 1
    elif d == 'U' and nx != 1:
        nx -= 1
    elif d == 'D' and nx != n:
        nx += 1


print(nx, ny)


# 답안 예시
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny


print(x, y)
