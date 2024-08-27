import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)



def bfs(i):
    visited = [0] * (n+1)
    visited[i] = 1

    cnt = 0

    q = deque([i])

    while q:
        node = q.popleft()

        for now in graph[node]:
            if not visited[now]:
                visited[now] = 1 # 방문 처리
                cnt += 1
                q.append(now)

    return cnt


result = []
max_cnt = 0
for i in range(1, n+1):
    cnt = bfs(i)
    if max_cnt < cnt:
        max_cnt = cnt
        result.clear()
        result.append(i)
    elif max_cnt == cnt:
        result.append(i)

# 출력
print(*result)
