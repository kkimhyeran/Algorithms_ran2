n = int(input())
matrix = [list(map(int,input())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, num):

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if matrix[nx][ny] == 1 and visited[nx][ny] == False:
            visited[nx][ny] = True
            matrix[nx][ny] = num
            # 재귀 함수
            dfs(nx, ny, num)


num = 1 # 첫번째 단지 부터 순차적으로 번호 부여

for i in range(n):
    for j in range(n):

        if matrix[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True # 방문 처리
            matrix[i][j] = num
            dfs(i, j, num)

            num += 1 # 다음 단지에 붙일 번호



new_matrix = sum(matrix,[]) # 2차원 > 1차원 변환
cnt = max(new_matrix)
result = []
for i in range(cnt):
    result.append(new_matrix.count(i+1))

result.sort()

print(cnt)
[print(i) for i in result]

