import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 빙산 덩어리 개수 세기
def count_components(icebeargs, n, m):
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if icebeargs[i][j] > 0 and not visited[i][j]:
                cnt += 1
                q = deque([(i, j)])
                visited[i][j] = True

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if icebeargs[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
    return cnt

# 빙산 녹이기
def melt_one_year(icebeargs, n, m):
    melt = [[0] * m for _ in range(n)]

    # 감소량 계산
    for i in range(n):
        for j in range(m):
            if icebeargs[i][j] > 0:
                sea = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and icebeargs[nx][ny] == 0:
                        sea += 1
                melt[i][j] = sea

    # 한 번에 적용
    for i in range(n):
        for j in range(m):
            if icebeargs[i][j] > 0:
                icebeargs[i][j] = max(0, icebeargs[i][j] - melt[i][j]) # 마이너스 값 처리

# 입력값 받기
n, m = map(int, input().split())
icebeargs = [list(map(int, input().split())) for _ in range(n)]

years = 0
while True:
    comp = count_components(icebeargs, n, m)
    if comp >= 2:
        print(years)
        break
    if comp == 0:
        print(0)
        break

    melt_one_year(icebeargs, n, m)
    years += 1
