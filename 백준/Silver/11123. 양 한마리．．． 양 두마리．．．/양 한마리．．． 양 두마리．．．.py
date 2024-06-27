import sys
sys.setrecursionlimit(10**6)


t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    # h, w = 3, 5

    grid = [list(input()) for _ in range(h)]
    # grid = [['#', '#', '#', '.', '#'],
    #         ['.','.', '#', '.', '.'],
    #         ['#','.','#','#','#']]
    #
    visited = [[0]*w for _ in range(h)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    sheap_cnt = 0

    def dfs(i, j):
        visited[i][j] = 1
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if not (0 <= nx < h and 0 <= ny < w):
                continue

            if grid[nx][ny] == '#' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny)


    for i in range(h):
        for j in range(w):

            if grid[i][j] == '#' and visited[i][j] == 0:
                sheap_cnt += 1
                
                dfs(i, j)

                # print("{},{} 에서 양 무리 수: {}".format(i, j, sheap_cnt))

    print(sheap_cnt)
