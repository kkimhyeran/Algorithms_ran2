from collections import deque


m, n = map(int, input().split())

box = []
for _ in range(n):
    box.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1(익은 토마토가 있는 좌표 저장)
q = deque()

def dfs():

    while q:
        x, y = q.popleft()

        # 익은 토마토
        # -1: 토마토가 없는 칸, 0: 안 익은 토마토
        if box[x][y] > 0:

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    # 익은 토마토 근처에 안익은 토마토가 있으면
                    if box[nx][ny] == 0:
                        box[nx][ny] = box[x][y] + 1
                        q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i, j])

dfs()

result = sum(box,[])
if 0 in result:
    print(-1)
else:
    print(max(result)-1)