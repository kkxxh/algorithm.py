n, m = map(int, input().split())
a, b, d = map(int, input().split())

game_map = []
cnt = 1

# 북, 동, 남, 서
direction = [0, 1, 2, 3]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for _ in range(m):
    game_map.append(list(map(int, input().split())))

while True:
    for i in range(len(direction)):
        # 현재 방향 direction[d-1]
        d = d-1
        nx = a + dx[d%4]
        ny = b + dy[d%4]
        
        if game_map[nx][ny] == 0:
            game_map[nx][ny] = 1
            a, b = nx, ny
            cnt += 1
            break
    if a != nx or b != ny:
        nx = a - dx[d%4]
        ny = b - dy[d%4]
        if game_map[nx][ny] == 1:
            break
        else :
            game_map[nx][ny] = 1
            a, b = nx, ny
            cnt += 1


print(cnt)
