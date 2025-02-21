from collections import deque

def bfs(start, end, mazes, n, m):
    q = deque()
    q.append(start)
    x, y = start
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if mazes[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

                if nx == end[0] and ny == end[1]:  # 도착 지점에 도달하면 거리 반환
                    return visited[nx][ny] -1
            
    return None

def solution(maps):
    mazes = []
    start = []
    lever = []
    exit = []
    
    for i, row in enumerate(maps):
        mazes.append(list(row))
        for j, cell in enumerate(row):
            if cell == 'S':
                start = [i, j]
            elif cell == 'L':
                lever = [i, j]
            elif cell == 'E':
                exit = [i, j]
    
    n = len(mazes)
    m = len(mazes[0])

    # Start -> Lever
    dist1 = bfs(start, lever, mazes, n, m)

    # Lever -> Exit
    dist2 = bfs(lever, exit, mazes, n, m)
    
    if dist1 is None or dist2 is None:
        return -1
    return dist1 + dist2
