from collections import deque
f, s, g, u, d = map(int, input().split())


def bfs(f, s, g, u, d):
    q = deque()
    q.append(s)

    visited = [0 for i in range(f)]
    visited[s-1] = 1 # 현재 강호가 위치한 층을 방문 처리

    
    while q:
        now = q.popleft()
        
        if now == g:
            result = visited[now - 1] - 1
            return result
        
        for i in (now + u, now -d):
            if 0 < i <= f and visited[i-1] == 0:
                q.append(i)
                visited[i-1] = visited[now-1] + 1
                
    return 'use the stairs'



print(bfs(f, s, g, u, d))

