
import heapq

n, d = map(int, input().split())

# 시작, 종료, 거리 정보가 든 배열 선언
short_road = [[] for _ in range(d+1)]
for i in range(d):
    short_road[i].append([i+1, 1])

for i in range(n):
    start, end, dist = map(int, input().split())
    if end > d:
        continue

    short_road[start].append([end, dist])


# 시작(0) 부터 각 i 위치까지의 최단 거리는 큰값으로 저장
distance = [1000000 for i in range(d + 1)]

queue = []

# 시작노드, 비용
heapq.heappush(queue, (0, 0))
# distance[start] = 0

while queue:
    # dist: 시작 - 현재 노드 까지의 최단 거리
    dist, start = heapq.heappop(queue)

    if dist > distance[start]:
        continue

    for i in short_road[start]:
        cost = dist + i[1]
        end = i[0]

        if distance[end] > cost:
            distance[end] = cost

            # distance[d] = distance[end] + (d - end)
            heapq.heappush(queue, (cost, end))

print(distance[d])