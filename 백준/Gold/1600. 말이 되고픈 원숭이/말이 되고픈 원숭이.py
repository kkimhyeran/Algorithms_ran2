import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
n, m = map(int, input().split())

horses = [list(map(int, input().split())) for _ in range(m)]

dx4 = [1, -1, 0, 0]
dy4 = [0, 0, 1, -1]

kdx = [2, 2, 1, 1, -1, -1, -2, -2]
kdy = [1, -1, 2, -2, 2, -2, 1, -1]

visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]
q = deque()

# 시작 상태 넣기
visited[0][0][0] = True
q.append((0, 0, 0, 0))  # x, y, k_used, dist

while q:
    x, y, k_used, dist = q.popleft()

    if x == m - 1 and y == n - 1:
        print(dist)
        sys.exit(0)

    # 1) 상하좌우 이동
    for i in range(4):
        nx = x + dx4[i]
        ny = y + dy4[i]
        if 0 <= nx < m and 0 <= ny < n and horses[nx][ny] == 0:
            if not visited[nx][ny][k_used]:
                visited[nx][ny][k_used] = True
                q.append((nx, ny, k_used, dist + 1))

    # 2) 나이트 이동
    if k_used < k:
        now_k = k_used + 1
        for j in range(8):
            nx = x + kdx[j]
            ny = y + kdy[j]
            if 0 <= nx < m and 0 <= ny < n and horses[nx][ny] == 0:
                if not visited[nx][ny][now_k]:
                    visited[nx][ny][now_k] = True 
                    q.append((nx, ny, now_k, dist + 1))

print(-1)