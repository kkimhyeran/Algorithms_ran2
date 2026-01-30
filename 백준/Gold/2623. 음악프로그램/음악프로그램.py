from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n: 가수 수, m: 보조PD 수

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    tmp = list(map(int, input().split()))
    k = tmp[0]
    singers = tmp[1:]

    # k명이면 간선은 k-1개: singers[i] -> singers[i+1]
    for i in range(k - 1):
        a = singers[i]
        b = singers[i + 1]
        graph[a].append(b)
        indegree[b] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

rslt = []
while q:
    curr = q.popleft()
    rslt.append(curr)

    for nxt in graph[curr]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

# 사이클 체크
if len(rslt) != n:
    print(0)
else:
    print("\n".join(map(str, rslt)))
