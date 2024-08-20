import sys
import heapq
f = sys.stdin.readline

n = int(f())
m = int(f())

bus_matrix = [[] for _ in range(n+1)]
for i in range(m):
    s, e, c = map(int, f().split())
    bus_matrix[s].append((e, c))

start, end = map(int, f().split())


distance = [int(1e9)for _ in range(n+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:

        from_cost, from_node = heapq.heappop(q)

        if from_cost > distance[from_node]:
            continue

        # print(bus_matrix)
        for i in bus_matrix[from_node]:

            # 연결된 노드와 비용
            to_node = i[0]
            to_cost = i[1]

            if distance[to_node] > from_cost + to_cost:
                distance[to_node] = from_cost + to_cost

                heapq.heappush(q, (distance[to_node], to_node))

        # print(bus_matrix)


dijkstra(start)
print(distance[end])