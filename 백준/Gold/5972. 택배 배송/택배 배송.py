import heapq
import sys

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, n, graph):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (비용, 노드)
    
    while pq:
        cost, node = heapq.heappop(pq)
        
        if dist[node] < cost:
            continue
        
        for nxt, w in graph[node]:
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
    
    return dist


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = dijkstra(1, N, graph)
print(dist[N])

