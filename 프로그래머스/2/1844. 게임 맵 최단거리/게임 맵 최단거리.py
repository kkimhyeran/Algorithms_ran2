from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    queue = deque([(0, 0)]) # 시작 위치 큐에 저장
    maps[0][0] = 1  
    
    while queue:
        x, y = queue.popleft()
        
        # 도착하면 결과 return
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        
        # 상하좌우 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    return -1
