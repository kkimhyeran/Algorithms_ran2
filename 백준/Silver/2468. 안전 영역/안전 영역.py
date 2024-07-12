import sys
sys.setrecursionlimit(10**6)

n = int(input())

matrix = []
max_height = 0 # 초기 최대 수위 임시 변수

for _ in range(n):
    temp_matrix = list(map(int, input().split()))
    matrix.append(temp_matrix)

    if max_height < max(temp_matrix):
        max_height = max(temp_matrix)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, t):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if matrix[nx][ny] > t:
                visited[nx][ny] = 1
                dfs(nx, ny, t)

result = []


for h in range(0, max_height):
    visited = [[0]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):

            # 수위보다 높고, 아직 방문하지 않았으면 >> 안전영역 대상
            if matrix[i][j] > h  and visited[i][j] == 0:
                cnt += 1
                visited[i][j] = 1
                dfs(i, j, h)


    result.append(cnt)


print(max(result))