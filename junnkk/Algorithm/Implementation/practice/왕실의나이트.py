## junnkk
position = input()

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

# print(ord('a'))  # 97
# print(ord('h'))  # 104

x = ord(position[0])
y = int(position[1])

cnt = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 97 <= nx <= 104 and 1 <= ny <= 8:
        cnt += 1

print(cnt)





## 답안 예시
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])-int(ord('a'))) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
