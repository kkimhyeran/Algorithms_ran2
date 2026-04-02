import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

INF = 10 ** 9


def dfs(cur, parent):
    child_count = 0
    total = 0

    for nxt, cost in graph[cur]:
        if nxt == parent:
            continue
        child_count += 1
        sub = dfs(nxt, cur)
        total += min(cost, sub)

    # 1번 섬 제외 리프라면
    if child_count == 0:
        return INF

    return total

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    # 만약 섬이 1개라면?
    if n == 1:
        print(0)
        continue

    print(dfs(1, 0))


