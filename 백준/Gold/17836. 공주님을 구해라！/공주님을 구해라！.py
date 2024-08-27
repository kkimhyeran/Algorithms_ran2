import sys
from collections import deque

input = sys.stdin.readline
n, m, t = map(int, input().split())

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, z):
    q = deque([(x, y, z)])
    visited[x][y][z] = 1

    while q:
        x, y, z = q.popleft()

        if x == (n-1) and y == (m-1):
            # print(visited[x][y][z])
            return visited[x][y][z] - 1


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            else:
                if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))

                elif graph[nx][ny] == 2 and visited[nx][ny][z] == 0:
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    q.append((nx, ny, 1))

                elif z == 1 and graph[nx][ny] == 1 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))

    return 10e9



result = bfs(0,0,0)
if result > t:
    print("Fail")
else:
    print(result)