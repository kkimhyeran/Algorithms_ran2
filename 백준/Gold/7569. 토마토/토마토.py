import sys
from collections import deque
input = sys.stdin.readline

# 1. 입력 받기
m, n, h = map(int, input().split())
tomato_boxes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 6방향 (상, 하, 좌, 우, 위, 아래)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 2. BFS 준비 (익은 토마토들 큐에 삽입)
q = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato_boxes[z][y][x] == 1:
                q.append((z, y, x))

# 3. BFS 진행
while q:
    z, y, x = q.popleft()
    for i in range(6):
        nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if tomato_boxes[nz][ny][nx] == 0:   # 안 익은 토마토만 익힘
                tomato_boxes[nz][ny][nx] = tomato_boxes[z][y][x] + 1
                q.append((nz, ny, nx))

# 4. 결과 계산
days = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato_boxes[z][y][x] == 0:  # 아직 안 익은 토마토가 있으면
                print(-1)
                sys.exit(0)
            days = max(days, tomato_boxes[z][y][x])

# 5. 정답 출력 (최소 일수)
print(days - 1)