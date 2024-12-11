import sys
sys.setrecursionlimit(10**6)

# 1. 입력값
n = int(input())
matrix = [list(input()) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j):
    for k in range(4):
        nx = dx[k] + i
        ny = dy[k] + j

        if 0 <= nx < n and 0 <= ny < n:
            if matrix[nx][ny] == chk_clr and visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny)


# 2. 일반인이 보는 구역 수 구하기
visited = [[False]*n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            chk_clr = matrix[i][j]
            cnt1 += 1
            dfs(i, j)


# 3. 적록색약이 보는 구역 수 구하기
# 빨강+초록 같은 색깔로 봄 > 빨강을 그린으로 바꾸기
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'


visited = [[False]*n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            chk_clr = matrix[i][j]
            cnt2 += 1
            dfs(i, j)


print(cnt1, cnt2)


