from collections import deque
import sys

# 1. 입력값
input = sys.stdin.readline
n, m, r = map(int, input().split())
matrix = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    matrix[u].append(v)
    matrix[v].append(u)

# 정렬
for i in range(n+1):
    matrix[i].sort()


# 2. bfs
visited = [0] * (n+1)
visited[r] = 1

q = deque()
q.append(r)

cnt = 2
while q:

    u = q.popleft()

    for v in matrix[u]:

        if visited[v] == 0:
            visited[v] = cnt
            q.append(v)
            cnt += 1

# 3. 출력
for i in visited[1:]:
    print(i)