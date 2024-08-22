from collections import deque

# 1. 입력값 받기
n, m = map(int, input().split())
graph = [[]for _ in range(n)]

for i in range(n):
    row = list(map(int, input()))
    graph[i] = row



# 2. 방문 여부 확인을 위한 3차원 배열 생성
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x,y,z):
    
    q = deque()
    q.append([0, 0, 0])
    visited[x][y][z] = 1
    
    while q:
        x, y, z = q.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
    
            else:
                if graph[nx][ny] == 1 and z == 0:
                    # 이동 횟수 업데이트
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append([nx, ny, 1])
    
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx, ny, z])
    return -1


print(bfs(0,0,0))