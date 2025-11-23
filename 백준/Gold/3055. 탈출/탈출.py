from collections import deque

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

water_q = deque()
hedgehog_q = deque()

# 위치 찾기
for i in range(r):
    for j in range(c):
        # 고슴도치 위치
        if graph[i][j] == 'S':
            hedgehog_q.append((i, j, 0))  # (x, y, time)

        # 물있는 칸
        elif graph[i][j] == '*':
            water_q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
while hedgehog_q:
    # 1. 물 먼저 확장
    for _ in range(len(water_q)):
        wx, wy = water_q.popleft()
        for i in range(4):
            nx, ny = wx + dx[i], wy + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    water_q.append((nx, ny))

    # 2. 그 다음 고슴도치 확장
    for _ in range(len(hedgehog_q)):
        x, y, t = hedgehog_q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위
            if 0 <= nx < r and 0 <= ny < c:
                # 비버 굴 도착
                if graph[nx][ny] == 'D':
                    print(t + 1)
                    exit(0)

                # 이동 가능한 빈 칸
                if graph[nx][ny] == '.':
                    graph[nx][ny] = 'S'
                    hedgehog_q.append((nx, ny, t + 1))

# 탈출 불가능
print("KAKTUS")