from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

miro = []
fire = deque()
visited_fire = [[-1]*c for _ in range(r)]
visited_j = [[-1]*c for _ in range(r)]

# 입력 받기
for i in range(r):
    row = list(input().rstrip())
    for j in range(c):
        if row[j] == 'F':
            fire.append((i, j))
            visited_fire[i][j] = 0  # 불 시작점
        elif row[j] == 'J':
            jx, jy = i, j
            visited_j[i][j] = 0  # 지훈 시작점
    miro.append(row)

# 방향 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 1. 불 퍼지는 시간 계산 BFS
while fire:
    x, y = fire.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            # 벽이 아니고 아직 불이 안 갔고
            if miro[nx][ny] != '#' and visited_fire[nx][ny] == -1:
                visited_fire[nx][ny] = visited_fire[x][y] + 1
                fire.append((nx, ny))


# 2. 지훈 BFS
q = deque()
q.append((jx, jy))

while q:
    x, y = q.popleft()

    # 만약 가장자리에 도달했다면 탈출 성공
    if x == 0 or x == r-1 or y == 0 or y == c-1:
        print(visited_j[x][y] + 1)
        exit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            # 이동 가능한 조건:
            # 1) 벽 X
            # 2) 아직 방문 X
            # 3) 불이 도착하지 않았거나, 지훈이 더 빨리 도착할 수 있어야 함
            if miro[nx][ny] != '#' and visited_j[nx][ny] == -1:
                # 지훈의 다음 이동시간
                next_time = visited_j[x][y] + 1

                # 불이 아예 안 오거나, 불보다 먼저 도착하는 경우에만 이동 가능
                if visited_fire[nx][ny] == -1 or next_time < visited_fire[nx][ny]:
                    visited_j[nx][ny] = next_time
                    q.append((nx, ny))

# 탈출 못함
print("IMPOSSIBLE")