import heapq

# n, k = 5, 17
n, k = map(int, input().split())
INF = int(1e9)
distance = [INF] * 1000001


def dijkstra(start):
    distance[start] = 0 # 시작 위치 시간 초기화
    q = []
    heapq.heappush(q, (0, start))

    while q:

        time, node = heapq.heappop(q)

        if node == k:
            break

        if distance[node] < time:
            continue

        for i, j in [(node*2, time), (node+1, time+1), (node-1, time+1)]:
            if 0 <= i <= 100000 and distance[i] > j:
                distance[i] = j
                heapq.heappush(q, (j, i))


dijkstra(n)
print(distance[k])