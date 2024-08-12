import sys
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
matrix = [[0]*m for _ in range(n)]

for _ in range(k):
    i, j = map(int, input().split())
    matrix[i-1][j-1] = 1


dx = [0,0,-1,1]
dy = [1, -1,0,0]

def dfs(i, j):
    global size
    size += 1

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                dfs(nx, ny)



size_list = []
size = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            matrix[i][j] = 0
            dfs(i, j)

            size_list.append(size)
            size = 0

print(max(size_list))
